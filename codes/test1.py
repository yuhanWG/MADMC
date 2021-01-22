import numpy as np
from fonctions import *
import time
import matplotlib.pyplot as plt
import sys

def plot_figure(x,tn,tl):
	print("??")
	plt.figure(figsize=(10,5))
	plt.style.use('ggplot')
	plt.title("La courbe du temps d'exécution")

	plt.xlabel("taille d'ensemle des solutions")
	plt.ylabel("temps")
	#plt.yticks((np.arange(0,max(tn)+1,0.1)))

	plt.plot(x,tn,color='r',label="recherche exhaustive")
	plt.plot(x,tl,color='b',label="recherche lexicographique")
	plt.grid(True)
	plt.legend()
	plt.show()

if __name__=="__main__":
	if len(sys.argv)!=4:
		raise Exception("veuillez verifier paramatres! python test1.py -Nb_vecteur -step nb_trial")
	N = int(sys.argv[1])
	step = int(sys.argv[2])
	nb_trial = int(sys.argv[3])

	#N = 10000
	m = 1000
	#nb_trial = 50
	temps_moyen_lex=[]
	temps_moyen_naif=[]
	x = np.arange(200,N+1,step)

	for n in range(200,N+1,step):
		tmp_naif=0
		tmp_lex=0
		for i in range(nb_trial):
			test_set = vecteur_alea(n,m)
			time_naif_start = time.time()
			d1=recherche_exhaustif(test_set,True)
			time_naif_end = time.time()
			tmp_naif += time_naif_end-time_naif_start

			time_lex_start = time.time()
			d2=recherche_lexicographique(test_set, True)
			time_lex_end = time.time()
			tmp_lex += time_lex_end-time_lex_start
			if(len(set(d1).difference(set(d2)))!=0):
				raise Exception("error in algorithme!")

		temps_moyen_naif.append(tmp_naif/nb_trial)
		temps_moyen_lex.append(tmp_lex/nb_trial)

	#print(temps_moyen_naif)
	#print(temps_moyen_lex)
	plot_figure(x,temps_moyen_naif,temps_moyen_lex)
