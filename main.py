# from tqdm import tqdm #Usage du module pour faire des barres de progressions
import subprocess
import time
import os
import importlib
from random import *
import sys

#Début du logiciel
os.system("title Multi Tools V1 - Version 0.1 - Free")
version_date = "12/04/23"
version = "0.1"


# Définition pour voir si `pipp` et que les modules sont installer
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


# Test pour savoir si `pip` les modules sont installer
if is_pip_installed() and is_tqdm_installed():
    print("pip et les modules sont déjà installés.")
    os.system("cls")
else:
    if not is_pip_installed():
        print("pip n'est pas installé. Installation en cours...")
        subprocess.check_call(['python', '-m', 'ensurepip', '--default-pip'])
        print("pip a été installé avec succès.")
        os.system("cls")

    if not is_tqdm_installed():
        print("Le module tqdm n'est pas installé. Installation en cours...")
        subprocess.check_call(['pip', 'install', 'tqdm'])
        print("Le module tqdm a été installé avec succès.")
        os.system("cls")

def verif_module():
    from tqdm import trange
    for i in trange(2, desc='Vérification des modules'):
        time.sleep(0.01)
        for x in trange(randint(0,15), desc=f'Module {i}'):
            time.sleep(.1)
    time.sleep(1)
    os.system("cls")

verif_module()


def num_class():
    print("Multi Tools V1 - Made By Legoshii レゴシイ#3660\n")
    time.sleep(1)

    choix_fonction = input("""
[0] Informations du logiciel.
[1] Mise à jour automatique des logiciels.
[2] Voir les IP.
[3] Suppression du cache des DNS.
[4] Voir les informations du système.

[*] Fermer le logiciel

Choix > """)

    if choix_fonction == '1':
        os.system("winget upgrade --all")
        next()
    elif choix_fonction == '0':
        print("\n- Dernière mise à jour le", version_date ,"\n- Version :", version ,"- Free \n- Créer par Legoshii レゴシイ#3660\n- Version Python :",sys.version, "\n- Site web : https://legoshii.fr\n- Liste des mise à jour : https://legoshii.fr/multi-tools/update\n- Support : SOON\n")
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
        print("\nNice :)")
        next()
    elif choix_fonction == '*':
        os.system("exit")
    else:
        print("Choix invalide")

def next():
    time.sleep(1)
    choix_next = input("""Continuer ? (Y/N) """)
    if choix_next == "Y" or choix_next == "y":
        os.system("cls")
        num_class()
    if choix_next == "N" or choix_next == "n":
        next()
    else:
        print("Choix invalide :/")
        next()

num_class()