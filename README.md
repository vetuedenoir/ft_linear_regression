# ft_linear_regression
## Présentation du projet
ft_linear_regression est une implémentation simple d’une régression linéaire avec une seule variable explicative : le kilométrage d'une voiture.
Ce projet comprend deux programmes : l’un pour entraîner le modèle et l’autre pour prédire le prix d’une voiture en fonction de son kilométrage.

Le projet est une introduction aux bases de l’apprentissage automatique et explore des concepts fondamentaux tels que les gradients,
les paramètres du modèle, et l'optimisation.

## Objectifs pédagogiques
Ce projet vise à :

Comprendre et implémenter une régression linéaire simple.
Manipuler des formules mathématiques liées à l’optimisation (gradient descent).
Explorer la visualisation des données pour mieux interpréter les résultats.

## Fonctionnement des programmes
### Programme d'entraînement
Le programme d'entraînement, model_training.py, ajuste les paramètres theta0 et theta1
​à partir des données fournies dans un fichier CSV.
Ces paramètres sont ensuite enregistrés dans un fichier pour être utilisés par le programme de prédiction.
### Programme de prédiction
Le programme de prédiction, car_price_estimateur.py, utilise les paramètres calculés pour estimer le prix d’une voiture en fonction de son kilométrage.
### Bonus : Évaluation des performances
Le programme bonus, estimate_precision.py, évalue la précision du modèle avec le score 𝑅 au carre
 , en comparant les prédictions aux données réelles.
