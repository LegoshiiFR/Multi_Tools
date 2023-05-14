import subprocess
import time
import os
import importlib
from random import *
import sys
import requests


#Début du logiciel
os.system("title Multi Tools - Vérification en cours...")
version_date = "14/05/23"
version = "1.1"


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

def is_requests_installed():
    try:
        importlib.import_module('requests')
        return True
    except ImportError:
        return False
    
'''def is_win10toast_installed():
    try:
        importlib.import_module('win10toast')
        return True
    except ImportError:
        return False
'''

# Test pour savoir si `pip` les modules sont installer
if is_pip_installed() and is_tqdm_installed() and is_requests_installed():
    print("pip et les modules sont déjà installés.")
    os.system("cls")
else:
    if not is_pip_installed():
        print("pip n'est pas installé. Installation en cours...")
        subprocess.check_call(['python', '-m', 'ensurepip', '--default-pip'])
        print("pip a été installé avec succès.")
        time.sleep(1)
        os.system("cls")

    if not is_tqdm_installed():
        print("Le module tqdm n'est pas installé. Installation en cours...")
        subprocess.check_call(['pip', 'install', 'tqdm'])
        print("Le module tqdm a été installé avec succès.")
        time.sleep(1)
        os.system("cls")

    if not is_requests_installed():
        print("Le module requests n'est pas installé. Installation en cours...")
        subprocess.check_call(['pip', 'install', 'requests'])
        print("Le module requests a été installé avec succès.")
        time.sleep(1)
        os.system("cls")
    
    '''if not is_win10toast_installed():
        print("Le module win10toast n'est pas installé. Installation en cours...")
        subprocess.check_call(['pip', 'install', 'win10toast'])
        print("Le module win10toast a été installé avec succès.")
        time.sleep(1)
        os.system("cls")
    '''

def verif_module():
    from tqdm import trange
    for i in trange(3, desc='Vérification des modules'):
        time.sleep(0.01)
        for x in trange(randint(0,15), desc=f'Module {i}'):
            time.sleep(.1)
    time.sleep(1)
    os.system("cls")

verif_module()

def verif_previous_version():
    # Vérifie si une version précédente est installer :
    if os.path.exists("Multi_Tools_Last_Version.exe"):
        print("Une ancienne version a été détectée, merci de patienter...")
        time.sleep(2)
        from tqdm import trange
        for i in trange(1, desc='⚙️ Configuration en cours...'):
            time.sleep(0.01)
            '''for x in trange(randint(0,15), desc=f' {i}'):
                time.sleep(.1)'''
        time.sleep(1)
        os.remove("Multi_Tools_Last_Version.exe")
        print("❌ Supression de la dernière version terminer.")
        time.sleep(1)
        os.system("cls")
    else:
        print("✅ Pas d'ancienne version détecter.")
        time.sleep(1)
        os.system("cls")

verif_previous_version()

def update_logiciel():
    # Définir l'URL du fichier à télécharger
    url = "https://archive.legoshii.fr/multi_tools/download/latest/Multi_Tools.exe"

    # Vérifier si le fichier existe déjà dans le répertoire actuel
    if os.path.exists("Multi_Tools.exe"):
        # Calculer la taille du fichier actuel
        size_actuel = os.path.getsize("Multi_Tools.exe")

        # Télécharger le nouveau fichier
        response = requests.get(url)

        # Vérifier si la taille du nouveau fichier est différente de celle de l'actuel
        if len(response.content) != size_actuel:
            # Renommer le fichier actuel
            os.rename("Multi_Tools.exe", "Multi_Tools_Last_Version.exe")
            print("Le fichier actuel a été renommé en Multi_Tools_Last_Version.exe")

            # Écrire le contenu du nouveau fichier dans un fichier local
            with open("Multi_Tools.exe", "wb") as f:
                f.write(response.content)

            print("Le nouveau fichier a été téléchargé avec succès.")
            os.startfile("Multi_Tools.exe")
            os.system("exit")
        else:
            print("✅ Vous possèdez la dernière version :)")
    else:
        # Télécharger le fichier car il n'existe pas dans le répertoire actuel
        response = requests.get(url)

        # Écrire le contenu du fichier dans un fichier local
        with open("Multi_Tools.exe", "wb") as f:
            f.write(response.content)

        print("✅ Le fichier a été téléchargé avec succès.")


def verif_update_logiciel():
    # Définir l'URL du fichier à télécharger
    url = "https://archive.legoshii.fr/multi_tools/download/latest/Multi_Tools.exe"

    # Vérifier si le fichier existe déjà dans le répertoire actuel
    if os.path.exists("Multi_Tools.exe"):
        # Calculer la taille du fichier actuel
        size_actuel = os.path.getsize("Multi_Tools.exe")

        # Télécharger le nouveau fichier
        response = requests.get(url)

        # Vérifier si la taille du nouveau fichier est différente de celle de l'actuel
        if len(response.content) != size_actuel:
            '''from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("⚙️ Mise à jour", "⚠️ : Une nouvelle version à était détecter. Souhaitez-vous l'installer ?")
            toaster.notification_click = update_logiciel'''


            print("⚠️ : Nouvelle version détectée")
            choix_next = input("""Souhaitez vous la télécharger ? (Y/N) """)
            if choix_next == "Y" or choix_next == "y":
                update_logiciel()
            if choix_next == "N" or choix_next == "n":
                os.system("exit")
            else:
                print("Choix invalide :/")

verif_update_logiciel()

def num_class():
    os.system("title Multi Tools V1.1 - Made By Legoshii レゴシイ#3660")
    print("Multi Tools V1.1 - Made By Legoshii レゴシイ#3660\n")
    time.sleep(1)

    choix_fonction = input("""
[0] Informations du logiciel.
[1] Mise à jour automatique des logiciels installés.
[2] Voir les IP.
[3] Suppression du cache des DNS.
[4] Voir les informations du système.

[99] Mettre à jour le logiciel
[*] Fermer le logiciel

Choix > """)

    if choix_fonction == '1':
        os.system("winget upgrade --all")
        next()
    elif choix_fonction == '0':
        print("\n- Dernière mise à jour le", version_date ,"\n- Version :", version ,"- Free \n- Créer par Legoshii レゴシイ#3660\n- Version Python :",sys.version_info.major,".",sys.version_info.minor,".",sys.version_info.micro, "\n- Site web : https://legoshii.fr\n- Liste des mise à jour : https://legoshii.fr/multi-tools/update\n- Support : https://legoshii.fr/multi-tools/support\n")
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
    elif choix_fonction == '99':
        update_logiciel()
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
        print("Fermeture du logiciel...")
        time.sleep(1.5)
        os.system("exit")        
    else:
        print("Choix invalide :/")
        next()

num_class()