Différentier HTTP et HTTPS

Lorsque l'utilisateur interagit avec un site internet, il envoie une requête, découpée en paquets. Ces paquets sont envoyés jusqu'au serveur, traités, et il renvoie une réponse composée d'un code de statut, d'une description, et éventuellement d'un body.

Problème posé par ce protocole: les transferts et retours ne sont pas sécurisés.
3 risques majeurs:
- confidentialité: si quelqu'un peut observer le trafic, cette personne peut lire le contenu envoyé ou reçu
- intégrité: cette personne peut modifier la réponse du serveur
- authenticité: on n'a donc pas de garantie qu'on s'adresse au bon serveur

On a donc ajouté une couche supplémentaire avec le HTTPS, qui inclue, en plus du protocole HTTP, un protocole TSL (anciennement SSL), qui permet de chiffrer et signer le contenu de chaque paquet envoyé au serveur, d'éviter les altérations non détectées, et donc une forme de vérification.

Comprendre la structure HTTP

Structure d'une requête:
- une ligne de départ qui contient:
    - une méthode (GET, HEAD, POST,...)
    - la cible (URL)
    - le code de statut
- des en-têtes (headers): 
    - des métadonnées, comme le type de contenu accepté, l'authentification, le cache, etc...

Structure d'une réponse:
- Une ligne de statut: 
    - code statut
    - phrase descriptive
- contenu envoyé, cache, cookies...

Méthodes HTTP principales:

GET
Requête pour accéder à une ressource. En principe, cette méthode ne modifie pas l'état du serveur

POST
Envoi de données pour traitement. Ex: envoi de formulaire, login...

PUT
remplacement/mise à jour complète d'une ressource à une URL donnée.

DELETE
Suppression de la ressource ciblée

Liste des codes de status HTTP:

200: OK
La requête a été bien reçue traitée et renvoyée par le serveur.

304 NOT MODIFIED
la ressource demandée n'a pas changé depuis la dernière visite. Elle a été mise en cache, donc inutile de la télécharger de nouveau.

302 FOUND
Redirection temporaire, signifie que la ressource demandée se trouve temporairement ailleurs. Ex: maintenance temporaire

101 Switching Protocols
Signifie que le serveur accepte de changer de protocole pour maintenir la communication. La connexion ne se fait plus via HTTP mais grâce à un autre protocole plus performant.

Exemple: 

HTTP fonctionne en mode:
Requête -> réponse -> fin

WebSocket:
Connexion ouverte -> échanges continus