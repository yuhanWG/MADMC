import numpy as np

#Q2
# génère un ensemble de n vecteurs où chaque composante est tirée aléatoirement selon une loi normale d'espérance m et d'écart-type m/4.
# return type:ndarray de talle [n,2]
def vecteur_alea(n,m):
    vect=np.random.normal(m,m/4,[n,2])
    return vect

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
    print(domine_index)
    non_dominer_index = [x for x in non_dominer_index if x not in domine_index]
    
    return non_dominer_index