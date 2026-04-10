"""
Ressources utilises dans le nav: password list file(raw), sha1 generator pour les tests

Ce programme permet de retrouver un mot de passe à partir de son empreinte SHA-1.
Il fonctionne en testant un par un les mots de passe contenus dans un fichier 
texte (dictionnaire) jusqu'à trouver celui qui correspond au code secret (le hash) fourni.
"""

import hashlib
def convert_text_to_sha1(text):
    hasher = hashlib.sha1(text.encode()).hexdigest()
    return hasher


def main():
    user_sha1 = input('Entrez le sha1 a cracker:')
    clear_user_sha1 = user_sha1.strip().lower()

    with open('passwords.txt') as f:
        for line in f:
            password = line.strip()
            converted_password = convert_text_to_sha1(password)

            if clear_user_sha1 == converted_password:
                print(f"Mot de passe trouvé: {password}")
                return
    print("Mot de passe introuvable!")

if __name__ == '__main__':
    main()

