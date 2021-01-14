# Projet MADMC-M2-Androide
### Sélection bi-objectif avec coefficients intervalles

Ce projet étudie deux différentes procédures pour trouver le point minimax parmi un ensemble des objets valué par bi-objectifs(minimiser) et compare leur efficacité. On implémente aussi les algorithmes naif et lexicographique pour trouver les points non-dominés
au sens de Pareto. Ce projet a été dévelopé en langage Python.


### Procédure1
- déterminer les points non dominés par programmation dynamique
- déterminer un point minimax parmi ceux-ci

### Procédure2
- déterminer les points non I-dominés
- déterminer un point minimax parmi ceux-ci
*** 
### Environnement pré-requis
Python

***

### Installation
Télécharger le dossier, les fichiers dedans sont exécutables, correspondent à de différentes expérimentations.

***

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
 
***
### Auteurs:
Yuhan WANG - ywang1525@gmail.com
