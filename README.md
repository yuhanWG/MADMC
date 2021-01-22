# Projet MADMC-M2-Androide
### Sélection bi-objectif avec coefficients intervalles

Ce projet étudie deux différentes procédures pour trouver le point minimax parmi un ensemble des objets valué par bi-objectifs(minimiser) et compare leur efficacité. On implémente aussi les algorithmes naif et lexicographique pour trouver les points non-dominés au sens de Pareto. Les deux procédures sont des suivantes:  

Procédure1
- déterminer les points non dominés par programmation dynamique
- déterminer un point minimax parmi ceux-ci  

Procédure2
- déterminer les points non I-dominés
- déterminer un point minimax parmi ceux-ci

### Environnement pré-requis
Python(numpy, matplotlib)

### Installation
Télécharger le dossier, les fichiers dedans sont exécutables, correspondent à de différentes expérimentations.

### Contenu
- images: les images produites par les algorithmes
- fonctions.py: y compris toutes les fonctions nécessaires pour ce projet 
- Q5-experimentation1.ipynb: expéimentations de question5
- Q12-experimentation2.ipynb: expérimentation de question12
- rapport.pdf
- test1.py: comparer les complexités des algoritghmes naifs et lexicographiques, traçer les courbes des temps d'exécutions respectifs

### Exemple1
Dans l'exemple, on va d'abord générer un ensemble des solutions aléatoirement de taille 4, et puis on déterminer les solutions non dominées au sens Pareto par l'algorithme naif et l'algorithme lexicographique, ensuite on calcule des solutions minimax en utilisant les deux procédures décrites. Les codes complètes sont dans test_fonctions2.ipynb 
```Python
import numpy as np
from fonctions_projet import *
# générer un ensemble de n vecteurs aléatoirements
ens = vecteur_alea(4,10)
print(ens)
```
output:  
```Python
array([[ 8.05946829, 12.11360171], 
       [11.93753551, 12.63934177], 
       [ 9.34453515, 10.34922359], 
       [ 8.15463349, 14.02778414]])
```
algorithme naif:
```Python
ND = recherche_exhaustif(ens,MIN=True) #recherche exhausif
print(ND)
```
output:
```Python
array([0,2]) # index des solutions non dominees
```
algorithme lexicographique:
```Python
recherche_lexicographique(ens_vecteur, MIN=True) #recherche lexicographique

```
output:
```Python
array[(0,2)] # index des solutions non dominees
```
Procedure1: déterminer une solution minimax en qui contient 1 objet
```Python
minimax_deux_temps(ens,k=1,alpha_min=0.2,alpha_max=0.5,MIN=True)
```
Procedure2: 
```Python
minimax_I_dominance(ens,k=1,alpha_min=0.2,alpha_max=0.5,MIN=True)
```
output:
```Python
(array([[[ 9.34453515, 10.34922359]]]), #image de solution minimax
 10.14, # fI(y)
 array([[[0., 0., 1., 0.]]])) #vecteur x ou 1 represente l'objet est choisi,0 sinon
```
### Exemple2-expérimentation1
Exécuter le fichier test1.py directement dans un terminal, en lui passant les paramètres nécessaires pour simuler l'expérimentation de la question5. Les courbes des temps sont affichées. Ici on prend un exemple: le nombre de vecteurs varie de 200 à N=400 par pas de step=50, pour chaque valeur on fera une moyenne du temps sur 20 ensembles tirés.
```Python
# Python test1.py N step nb_trial
Python test1.py 400 50 1
```
![Les courbes de résolution](https://github.com/yuhanWG/MADMC/blob/master/images/Figure_1.png)

### Exemple3-expérimentation2
Exécuter test2.py dans un terminal, en lui passant les paramètres la première et la seconde procédure de résolution, en faisant varier espilon de 0.025 à 0.5 par step=0.0.25, pour chaque intervalle, on fera une moyenne du temps d'exécution nb_trial=50.
```Python
# Python test2.py step nb_trial
Python test1.py 0.025 50
```
![](https://github.com/yuhanWG/MADMC/blob/master/images/Q12.png)




### Liste des fonctions
- **vecteur_alea(n,m)**: générer un ensemble de n vecteurs tirés aléatoirement selon la loi normale(m,m/4)
- **compare(a,b,MIN=True)**: déterminer si vecteur a est dominée par vecteur b en cas de minimisation
- **recherche_exhaustif(ens_vecteur,MIN=True)**: implémentation de l'algorithme naif, qui procède avec des comparaisons systématiques
- **tri_lexicographique(ens_vecteur)**: effectuer un tri lexicographique des vecteurs
- **recherche_lexicographique(ens_vecteur, MIN=True)**: un seul parcours de la liste, identifier les objets non dominés
- **prog_dynamique(ens_vecteur,k,MIN=True)**: déterminer les images des sous-ensembles Pareto-optimaux de taille k par la programmation dynamique
- **image(ens_vecteur,ens_index)**: projecter le point depuis l'espace de décision vers l'espace de critères
- **minimax_deux_temps(ens_vecteur,k,alpha_min,alpha_max,MIN=True)**: implémentation de procédure1
- **transform(ens_vecteur,alpha_min,alpha_max)**: réduire une instance du problème I-dominance en une instance du problème de Pareto
- **minimax_I_dominance(ens_vecteur,k,alpha_min,alpha_max,MIN=True)**: implémentation de procédure2
 
### Auteurs:
Yuhan WANG - ywang1525@gmail.com
