import sys
from cx_Freeze import setup, Executable

setup(
    name = "Multi Tools",
    version = "1.1",
    description = "Multi Tools est un programme qui peut être interactif, offrant des options à l'utilisateur, ou il peut être automatisé pour exécuter des commandes en arrière-plan sans intervention de l'utilisateur.",
    executables = [Executable("main.py", base = "Win32GUI")])
