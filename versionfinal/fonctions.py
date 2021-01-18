import numpy as np

def vecteur_alea(n,m):
	#il faut eliminer les composants identiques
	c1=[]
	c2=[]
	for i in range(n):
		a=np.random.normal(m,m/4)
		b=np.random.normal(m,m/4)
		while((a in c1) and (b in c2)):
			a=np.random.normal(m,m/4)
			b=np.random.normal(m,m/4)
		c1.append(a)
		c2.append(b)

	c1=np.array(c1).reshape(-1,1)
	c2=np.array(c2).reshape(-1,1)
	vect=np.hstack((c1,c2))
	return vect

'''
def compare2(a,b,MIN):
    if(MIN):
        #need check the fonction np.all
        if((a<=b).all()):
            result='a'
        elif((b<=a).all()):
            result='b'
        else:
            result='incomparable'
    return result 
   '''
def compare(a,b,MIN):
	result = False
	if(MIN):
	#need check the fonction np.all
		if b[0]<a[0] and b[1]<=a[1] :
			return True
		if b[0]<=a[0] and b[1]<a[1] :
			return True
	return result


def tri_lexicographique(ens_vecteurs):
	#bi-objectif
	D = ens_vecteurs.shape[1]
	#un ordre de comparaison, exemple pour D=2, lex=[0,1] ou [1,0]
	lex=[0,1]
	a = ens_vecteurs[:,lex[0]]
	b = ens_vecteurs[:,lex[1]]
	ens_lex = np.lexsort((b,a))#tri by a, then by b
	#print(ens_lex)
	return ens_lex


def recherche_exhaustif(ens_vecteurs,MIN):
	res = []
	for i in range(len(ens_vecteurs)):
		state = False
		for j in range(len(ens_vecteurs)):
			if compare(ens_vecteurs[i,:],ens_vecteurs[j,:],MIN):
				state = True
		if state == False:
			res.append(i)
	return np.array(res)

def recherche_lexicographique(ens_vecteurs, MIN):
	ordre_lex = tri_lexicographique(ens_vecteurs)
	non_domine_index=[]
	for l in range(len(ordre_lex)):
		if(l==0):
			non_domine_index.append(ordre_lex[0])
		else:
		#index de la solution non domine
			dernier = non_domine_index[-1]
			actuel = ordre_lex[l]
			a = np.array(ens_vecteurs[dernier,:])
			b = np.array(ens_vecteurs[actuel,:])
			domine = compare(b,a,True)
			#if(domine == 'incomparable'):
			if not domine:
				non_domine_index.append(actuel)

	return np.array(non_domine_index)


def image(ens_vecteurs,ens_index):

	#print(ens_index.shape)
	for i in range(ens_index.shape[0]):
		t = np.where(ens_index[i,:]==1)
		if(i==0):
		#print(ens_vecteurs[t])
			images = np.sum(ens_vecteurs[t], axis=0)

		else:
			images = np.vstack((images,np.sum(ens_vecteurs[t], axis=0)))

	return images.reshape((-1,2))


def prog_dynamique(ens_vecteurs,k,MIN):
    #on voudrais creer un tableau qui permet de realiser le programmation dynamique
    #une case(i,j) represnete des sous-ensemble pareto-optimal de taille i dans {1..j}
    N = ens_vecteurs.shape[0]
    D = ens_vecteurs.shape[1]
    dym = np.zeros((k+1,N))
    #une list imbriquee
    list_index=[[]]*((k+1)*N)
    #initialisation:
    for i in range(N):
        #choisir 0 objets parmi ensemble de taille i
        list_index[i]=np.zeros(N)
        
   # print("init", list_index)
    
    for i in range(1,k+1):
        for j in range(N):
            #print(i,j)
            if((i==1) and (j==0)):
                init=np.zeros(N)
                init[0]=1
                list_index[N]=init
            else:   
                if(i-1==j):
                    index = np.zeros(N)
                    #choisir j objets dans j objets, la seule solution est de tout prendre
                    index[0:i]=1
                    list_index[i*N+j]=index
                if(i-1>j):
                    list_index[i*N+j]=np.zeros(N)
                    #print("impossible")
                if(i-1<j):
                    #if i-1<j, alors F et G exsite
                    #si on prend pas j
                    indexG = list_index[i*N+(j-1)]
                    
                    #si on prend j
                    indexF = list_index[(i-1)*N+(j-1)]
                    #print(indexG,indexF)
                        
                    indexG=np.array(indexG).reshape(-1,N)
                    indexF=np.array(indexF).reshape(-1,N)
                    
                    #print(indexF.shape)
                    
                    indexF[:,j]=1
                    
                    #print("G",i,j-1,indexG)
                    #print("F",i-1,j-1,indexF)
                    
                    #compare all the possibilities
                    ens_index = np.vstack((indexG,indexF))
                    
                    #print("ens_index",ens_index)
                    #print("shape",ens_index.shape)
                    
                    ens_images=image(ens_vecteurs,ens_index)
                    
                    #print("images",ens_images)
                    
                    index_opt = recherche_lexicographique(ens_images,True)
                    
                    #mettre a jour cette case
                    list_index[i*N+j] = ens_index[index_opt]
    
    result = np.array(list_index[-1])
                                      
    return result



def minimax_deux_temps(ens_vecteurs,k,alpha_min,alpha_max,MIN=True):
    #return les points minimax en choisissant k objets parmi un ensemble des vecteurs
    ens_index = prog_dynamique(ens_vecteurs,k,MIN)
    ens_pareto = image(ens_vecteurs,ens_index)
    points_minimax = []
    for p in ens_pareto:
        if(p[0]<p[1]):
            #y1<y2, alpha_min maximise FI
            points_minimax.append(p[0]*alpha_min+p[1]*(1-alpha_min))
        else:
            if(p[0]>p[1]):
                #y1>y2, alpha_max maximise FI
                points_minimax.append(p[0]*alpha_max+p[1]*(1-alpha_max))
            else:
                points_minimax.append(p[0]+p[1])
    minimax = np.min(np.array(points_minimax))
    index_point_minimax = np.where(np.array(points_minimax)==minimax)
    
    return ens_pareto[index_point_minimax,:], minimax, ens_index[index_point_minimax,:]

def transform(ens_vect,alpha_min,alpha_max):
    nb_vect,dim = ens_vect.shape
    ens_trans = np.zeros((nb_vect,dim))
    for i in range(nb_vect):
        x,y = ens_vect[i,:]
        x_trans = alpha_min*x+(1-alpha_min)*y
        y_trans = alpha_max*x+(1-alpha_max)*y
        ens_trans[i,:]= np.array([x_trans,y_trans])
    return ens_trans


def minimax_I_dominance(ens_vect,k,alpha_min,alpha_max,MIN=True):
    ens_trans = transform(ens_vect,alpha_min,alpha_max)
    index = prog_dynamique(ens_trans,k,MIN)
    images = image(ens_trans,index)
    images_real = image(ens_vect,index)
    points_minimax =[]
    #print(images.shape)
    for i in range(images.shape[0]):
        #print(images[i,:])
        y1,y2 = images_real[i,:]
        if y1<=y2:
            points_minimax.append(images[i,0])
        else:
            points_minimax.append(images[i,1])


    minimax = np.min(np.array(points_minimax))
    index_point_minimax = np.where(np.array(points_minimax)==minimax)
    return images_real[index_point_minimax,:], minimax,index[index_point_minimax,:]