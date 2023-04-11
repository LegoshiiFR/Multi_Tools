import subprocess
import time
import os
import urllib.request
import importlib

# Définition pour voir si `pipp` et que `tqdm` sont installer
def is_pip_installed():
    try:
        importlib.import_module('pip')
        return True
    except ImportError:
        return False
    
def is_tqdm_installed():
    try:
        importlib.import_module('tqdm')
        return True
    except ImportError:
        return False

# Stock de l'url de la dernière version du logiciel
url = "https://archive.legoshii.fr/Multi_Tools/download/main.py"

# Définition pour installer les indépendances
def install_dep():
    print("Téléchargement des modules...")
    os.system("pip install tqdm")
    os.system("cls")
    from tqdm import tqdm

# Test pour savoir si `pip` et `tqdm` sont installer
if is_pip_installed() and is_tqdm_installed():
    print("pip et le module tqdm sont déjà installés.")
    os.system("cls")
else:
    if not is_pip_installed():
        print("pip n'est pas installé. Installation en cours...")
        subprocess.check_call(['python', '-m', 'ensurepip', '--default-pip'])
        print("pip a été installé avec succès.")
        os.system("cls")
        install_dep()

    if not is_tqdm_installed():
        print("Le module tqdm n'est pas installé. Installation en cours...")
        subprocess.check_call(['pip', 'install', 'tqdm'])
        print("Le module tqdm a été installé avec succès.")
        os.system("cls")

# Mise à jour automatique
stats = os.stat('main.py')
#print(stats..st_size, "octets") #Affichage de la taille du fichier
"""if stats != 3579: #Si le fichier n'est pas égale à la valeur de la taille du fichier de la dernière mise à jour alors:
    for i in tqdm(range(0, 3579), total = 3 579, #3 579 ici = Taille du fichier de la dernière mise à jour
                desc ="Téléchargement de la mise à jour"):
        time.sleep(.1)
    time.sleep(1)
    urllib.request.urlretrieve(url, "main.py")
    print("Installation de la mise à jour...")
    time.sleep(3)
    os.system("cls")
else :
    None
"""

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