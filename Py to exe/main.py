import subprocess
import time
import os
import importlib
from random import *
import sys
import requests


#Début du logiciel
os.system("title Multi Tools - Vérification en cours...")
version_date = "18/05/23"
version = "1.2"



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
    
def is_rich_installed():
    try:
        importlib.import_module('rich')
        return True
    except ImportError:
        return False
    

# Test pour savoir si `pip` les modules sont installer
if is_pip_installed() and is_tqdm_installed() and is_requests_installed() and is_rich_installed():
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
    
    if not is_rich_installed():
        print("Le module rich n'est pas installé. Installation en cours...")
        subprocess.check_call(['pip', 'install', 'rich'])
        print("Le module rich a été installé avec succès.")
        time.sleep(1)
        os.system("cls")
    
from rich import print
def verif_module():
    from rich.progress import Progress
    print('⚙️ [blue]Vérification en cours')
    with Progress() as progress:
        task1 = progress.add_task("[green]tqdm", total=100)
        task2 = progress.add_task("[green]requests", total=100)
        task3 = progress.add_task("[green]rich", total=100)
        while not progress.finished:
            progress.update(task1, advance=0.9)
            progress.update(task2, advance=0.8)
            progress.update(task3, advance=0.9)
            time.sleep(0.02)
    os.system("cls")

verif_module()

def verif_previous_version():
    # Vérifie si une version précédente est installer :
    if os.path.exists("Multi_Tools_Last_Version.exe"):
        print("⚙️ Une ancienne version a été détectée, merci de patienter...")
        time.sleep(2)
        from tqdm import trange
        print("[green] ⚙️ Configuration en cours...")
        os.remove("Multi_Tools_Last_Version.exe")
        print("✅ Supression de la dernière version terminer.")
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
            print("✅ Le fichier actuel a été renommé en Multi_Tools_Last_Version.exe")

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
        from rich.progress import track
        for _ in track(range(100), description='[green]Téléchargement'):
            time.sleep(0.02)
        print('⚙️ [green]Configuration en cours')
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
        
        print("""
⚠️ [red]: Nouvelle version détectée
⌛ : Merci de pantienter...
        """)
        # Calculer la taille du fichier actuel
        size_actuel = os.path.getsize("Multi_Tools.exe")
        # Télécharger le nouveau fichier
        response = requests.get(url)

        # Vérifier si la taille du nouveau fichier est différente de celle de l'actuel
        if len(response.content) != size_actuel:
            choix_next = input("""Souhaitez vous la télécharger ? (Y/N) """)
            if choix_next == "Y" or choix_next == "y":
                update_logiciel()
            if choix_next == "N" or choix_next == "n":
                os.system("cls")
            else:
                print("Choix invalide :/")

verif_update_logiciel()

def uninstall_logiciel():
    from rich.console import Console
    from rich.markdown import Markdown

    url = "https://archive.legoshii.fr/multi_tools/download/latest/README.md"
    response = requests.get(url)
    markdown_content = response.text

    markdown = Markdown(markdown_content)
    print(markdown)
    choix_next = input("""❓ [yellow] Souhaitez-vous désinstaller le logiciel ? """)
    if choix_next == "Y" or choix_next == "y":
        print("En cours de développement ...")
    if choix_next == "N" or choix_next == "n":
        os.system("cls")
        num_class()



def num_class():
    os.system("title Multi Tools V1.2 - Made By Legoshii レゴシイ#3660")
    print("Multi Tools V1.2 - Made By Legoshii レゴシイ#3660\n")
    time.sleep(1)

    choix_fonction = input("""
[0] Informations du logiciel.
[1] Mise à jour automatique des logiciels installés.
[2] Voir les IP.
[3] Suppression du cache des DNS.
[4] Voir les informations du système.

[98] Mettre à jour le logiciel
[99] Désinstaller le logiciel
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
    elif choix_fonction == '98':
        update_logiciel()
    elif choix_fonction == '99':
        uninstall_logiciel()
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