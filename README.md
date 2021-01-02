# fr-boamp-api-extractor
## Description
fr-boamp-api-extractor permet d'extraire les offres de marchés publics publiées au bulletin officiel des annonces des marchés publics (BOAMP).
Le script ignore les appels d'offres dont la date limite de réponse est dépassée.

## Utilisation
Renseignez les mots-clés de recherches dans le fichier "search.txt" (Un mot ou expression par ligne).

Lancez le script "main.py".
Les appels d'offres correspondants seront écrits dans le fichier "annonce.txt".

Il est possible d'exclure les appels d'offres contenants certains mots-clés.
Pour cela, renseignez les mots interdits dans le fichier "reject.txt" (Un mot ou expression par ligne).
Les appels d'offres exclus par ce biais seront tout de même inscrits dans le fichier "rejectAnnonce.txt".

