import numpy as np
from fonctions import *
import time
import matplotlib.pyplot as plt

if __name__=="__main__":
	N,step,nb_trial= sys.argv
	#N = 10000
	m = 1000
	#nb_trial = 50
	temps_moyen_lex=[]
	temps_moyen_naif=[]

	for n in range(200,N+1,200):
		tmp_naif=0
		tmp_lex=0
		for i in range(nb_trial):
			print(n)
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

	print(temps_moyen_naif)
	print(temps_moyen_lex)
