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
- fonctions.py: y compris toutes les fonctions nécessaires pour ce projet 
- fichiers jupyternotebook: expéimentations faites dans le projet

### Démarrage
Dans les codes suivants, on va d'abord générer un ensemble des solutions aléatoirement de taille 4, et puis on déterminer les solutions non dominées par l'algorithme naif et l'algorithme lexicographique, ensuite on calcul des solutions minimax en utilisant les deux procédures décrites ci-dessus. Les codes complètes sont dans test_fonctions2.ipynb 
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
tri_lexicographique(ens) #tri lexicographique
recherche_lexicographique(ens_vecteur, MIN=True) #recherche lexicographique

```
output:
```Python
array[(0,3,1,2)]
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
