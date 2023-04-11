import subprocess
import tqdm
import time
import os
from tqdm import tqdm

stats = os.stat('main.py')
if stats == stats:
    for i in tqdm(range(0, 1023), total = 1023,
                desc ="Téléchargement de la mise à jour"):
        time.sleep(0.00000000000000000000009)
    time.sleep(1)
    print("Installation de la mise à jour...")
    time.sleep(3)
    resultCLS = subprocess.run(['cls'], capture_output=True, shell=True)
    print(cls)
else :
    None

os.system("title Multi Tools V1 - Version 0.1")

def num_class():
    print("Multi Tools V1 - Made By Legoshii レゴシイ#3660\n")
    time.sleep(2)

    choix_fonction = input("""
[0] Informations du logiciel
[1] Mise à jour automatique des logiciels
[2] Voir les IP
[3] Suppression du cache des DNS
[4] Voir les informations du système.

[99] Fermer le logiciel

Choix > """)

    if choix_fonction == '1':
        print("Veuillez patienter pendant que nous éxecutons la commande ...")
        result = subprocess.run(['winget', 'upgrade', '--all'], capture_output=True)
        print(result.stdout.decode('utf-8'))
    elif choix_fonction == '0':
        print(""" 
- Version [0.1]
- Créer par Legoshii レゴシイ#3660
- Version Python : 3.10
- Site web : https://legoshii.fr
- Support : SOON
        """)
    elif choix_fonction == '2':
        result = subprocess.run(['ipconfig'], capture_output=True)
        print(result.stdout.decode('utf-8'))
    elif choix_fonction == '3':
        result = subprocess.run(['ipconfig', '/flushdns'], capture_output=True)
        print(result.stdout.decode('utf-8'))
    elif choix_fonction == '4':
        result = subprocess.run(['systeminfo'], capture_output=True)
        print(result.stdout.decode('utf-8'))
    elif choix_fonction == '69':
        print("`\nNice :)")
    elif choix_fonction == '99':
        result = subprocess.run(['exit'], capture_output=True, shell=True)
    else:
        print("Choix invalide")

num_class()