import numpy as np

#Q2
# génère un ensemble de n vecteurs où chaque composante est tirée aléatoirement selon une loi normale d'espérance m et d'écart-type m/4.
# return type:ndarray de talle [n,2]
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


def compare(a,b,MIN):
    if(MIN):
        #need check the fonction np.all
        if((a<=b).all()):
            result='a'
        elif((b<=a).all()):
            result='b'
        else:
            result='incomparable'
    return result


#Q3
#ens_vecteurs: type np.ndarray
#min=true if it is a minimisation problem
def recherche_exhaustif(ens_vecteurs, MIN):
    #normalement un vecteur contient 2 composants, N=2
    D = ens_vecteurs.shape[1]
    N = ens_vecteurs.shape[0]
    non_dominer_index=[]
    domine_index=[]
    for i in range(N):
        for j in range(i+1,N):
            a=np.array(ens_vecteurs[i,:])
            b=np.array(ens_vecteurs[j,:])
            domine=compare(a,b,MIN)
            #if a isn't stored
            #print(i,j,a,b,domine)
            if(domine=='a'):
                if(not(i in non_dominer_index)):
                    non_dominer_index.append(i)
                if(j in non_dominer_index):
                    non_dominer_index.remove(j)
                    #print(non_dominer_index)
                if(not(j in domine_index)):
                    domine_index.append(j)
            elif(domine=='b'):
                if(not(j in non_dominer_index)):
                    non_dominer_index.append(j)
                if(i in non_dominer_index):
                    non_dominer_index.remove(i)
                if(not(i in domine_index)):
                    domine_index.append(i)
            #incomparable
            elif(domine=='incomparable'):
                if not(i in non_dominer_index):
                    non_dominer_index.append(i)
                if not(j in non_dominer_index):
                    non_dominer_index.append(j)
    #print(domine_index)
    non_dominer_index = [x for x in non_dominer_index if x not in domine_index]
    
    return np.array(non_dominer_index)

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
            domine = compare(a,b,True)
            if(domine == 'incomparable'):
                non_domine_index.append(actuel)
             
    return np.array(non_domine_index)