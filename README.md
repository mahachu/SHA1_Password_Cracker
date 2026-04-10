# 🛡️ SHA-1 Password Cracker

Ce script Python permet de retrouver un mot de passe en clair à partir de son empreinte (hash) **SHA-1** en utilisant une méthode d'attaque par dictionnaire.

## 📝 Description

Le programme compare un hash SHA-1 fourni par l'utilisateur à une liste de mots de passe contenus dans un fichier texte. Pour chaque mot de passe du fichier, le script génère son hash SHA-1 et vérifie s'il correspond à celui recherché.

### Ressources utilisées :
* **Générateur SHA-1 :** Pour créer des hashs de test.
* **Wordlist :** Un fichier de mots de passe en clair (ex: `passwords.txt`).

## ⚙️ Fonctionnement du code

Le script suit les étapes suivantes :
1. Lecture du hash SHA-1 cible via l'entrée utilisateur.
2. Ouverture du fichier `passwords.txt`.
3. Pour chaque ligne (mot de passe potentiel) :
   * Encodage du texte en SHA-1.
   * Comparaison avec le hash cible.
4. Affichage du résultat si une correspondance est trouvée.

## 🛠️ Installation et Utilisation

### 1. Prérequis
* [Python 3.x](https://www.python.org/) installé.
* Un fichier nommé `passwords.txt` dans le même dossier que le script, contenant une liste de mots de passe (un par ligne).

### 2. Téléchargement
Cloner le repôt
### 3. Execution
Lancer le script:
```bash:
  python3 main.py
```
