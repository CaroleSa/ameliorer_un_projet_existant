# **Plateforme web Pur Beurre**

**__**OpenClassrooms Projet 8**__**

Le site internet de Pur Beurre a été créé dans le but de proposer une alternative aux aliments caloriques du quotidien. 
Il utilise les données de l'A.P.I. d'Open Food Facts.

Ce site donne accès, suite au choix d'un aliment, à d'autres aliments d'une même catégorie et à leur nutriscore.
L'utilisateur a alors la possibilité de cliquer sur un aliment pour obtenir plus de détail sur ce dernier. 
Il peut également l'enregistrer dans ses favoris sous la condition qu'il ai été authentifié.

L'utilisateur peut créer un compte, se connecter et se déconnecter.
S'il est authentifié, il pourra :
- accéder à ses informations de compte 
- enregistrer des aliments dans ses favoris
- accéder à la liste de ses aliments favoris enregistrés
- et les supprimer s'il le souhaite.

Démarrage :
Ces instructions vous permettrons de prendre connaissance des pré-requis 
et d’installer le projet afin de pouvoir développer et tester localement.

    Pré-requis : 
        Python 3.7
        PostgreSQL : la base de données attendue est une base nommée purbeurre.
    
    Installation :
        Créer un dossier au nom de "purbeurre" sur votre disque
        
        Cloner le dépôt dans le dossier "purbeurre" avec la commande :
        git clone https://github.com/CaroleSa/AppliPurBeurre.git
        
        Initialiser un dépôt git avec la commande :
        git init

        Installer et activer un environnement virtuel
        
        Installer les requirements avec la commande :
        pip install -r requirements.txt

    Indiquer les données configurables :
        obligatoires :
            purbeurre/settings.py
            USER ligne 88 : nom utilisateur PostgreSQL 
            PASSWORD ligne 89 : mot de passe
        
        optionnelles :
            food/classes/database.py
            categories_food ligne 33 : liste contenant le nom des catégories d'aliments 
                                       utilisées par le programme
    
    Créer les tables dans la base de données grâce à la commande :
        python manage.py migrate
        
    Activer le serveur en local avec la commande :
        python manage.py runserver

Ce projet est accessible à cette adresse : 
http://carolepurbeurre.herokuapp.com/

Auteur :
Carole Sartori
