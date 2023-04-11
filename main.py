# from tqdm import tqdm #Usage du module pour faire des barres de progressions
import subprocess
import time
import os
import urllib.request
import importlib
import hashlib

# Définition pour voir si `pipp` et que les modules sont installer
def is_pip_installed():
    try:
        importlib.import_module('pip')
        return True
    except ImportError:
        return False
    
"""
def is_tqdm_installed():
    try:
        importlib.import_module('tqdm')
        return True
    except ImportError:
        return False
"""  

def is_requests_installed():
    try:
        importlib.import_module('requests')
        return True
    except ImportError:
        return False

# Stock de l'url de la dernière version du logiciel
url = "https://archive.legoshii.fr/Multi_Tools/download/main.py"
# Définie le fichier dans lequel nous somme
local_filename = 'main.py'

# Définition pour installer les indépendances
def install_dep():
    print("Vérifications des modules...")
    os.system("cls")
    

# Test pour savoir si `pip` les modules sont installer
if is_pip_installed() and is_requests_installed():
    print("pip et les modules sont déjà installés.")
    os.system("cls")
else:
    if not is_pip_installed():
        print("pip n'est pas installé. Installation en cours...")
        subprocess.check_call(['python', '-m', 'ensurepip', '--default-pip'])
        print("pip a été installé avec succès.")
        os.system("cls")
        install_dep()

    """if not is_tqdm_installed():
        print("Le module tqdm n'est pas installé. Installation en cours...")
        subprocess.check_call(['pip', 'install', 'tqdm'])
        print("Le module tqdm a été installé avec succès.")
        os.system("cls")
        install_dep()"""

    if not is_requests_installed():
        print("Le module requests n'est pas installé. Installation en cours...")
        subprocess.check_call(['pip', 'install', 'requests'])
        print("Le module requests a été installé avec succès.")
        os.system("cls")

# Mise à jour automatique
stats = os.stat('main.py')
#print(stats..st_size, "octets") #Affichage de la taille du fichier
# Obtenir le hash MD5 du fichier distant
import requests
response = requests.get(url)
remote_file_hash = hashlib.md5(response.content).hexdigest()

# Calculer le hash MD5 du fichier local
with open(local_filename, 'rb') as f:
    local_file_hash = hashlib.md5(f.read()).hexdigest()

# Comparer les deux hashes et télécharger le fichier distant s'ils sont différents
if remote_file_hash != local_file_hash:
    print("Le fichier local est différent du fichier distant. Téléchargement en cours...")
    response = requests.get(url)
    with open(local_filename, 'wb') as f:
        f.write(response.content)
    print("Le fichier a été téléchargé avec succès.")
else:
    print("Le fichier local est identique au fichier distant. Aucun téléchargement nécessaire.")

#Début du logiciel
os.system("title Multi Tools V1 - Version 0.1")

def num_class():
    print("Multi Tools V1 - Made By Legoshii レゴシイ#3660\n")
    time.sleep(1)

    choix_fonction = input("""
[0] Informations du logiciel
[1] Mise à jour automatique des logiciels
[2] Voir les IP
[3] Suppression du cache des DNS
[4] Voir les informations du système.

[99] Fermer le logiciel

Choix > """)

    if choix_fonction == '1':
        os.system("winget upgrade --all")
        next()
    elif choix_fonction == '0':
        print(""" 
- Version [0.1]
- Créer par Legoshii レゴシイ#3660
- Version Python : 3.10
- Site web : https://legoshii.fr
- Support : SOON
        """)
        next()
    elif choix_fonction == '2':
        os.system("ipconfig")
        next()
    elif choix_fonction == '3':
        os.system("ipconfig /flushdns")
        next()
    elif choix_fonction == '4':
        os.system("systeminfo")
        next()
    elif choix_fonction == '69':
        print("`\nNice :)")
        next()
    elif choix_fonction == '99':
        os.system("exit")
    else:
        print("Choix invalide")

def next():
    time.sleep(1)
    choix_next = input("""Continuer ? (Y/N) """)
    if choix_next == "Y":
        os.system("cls")
        num_class()
    if choix_next == "N":
        next()
    else:
        print("Choix invalide :/")
        next()

num_class()