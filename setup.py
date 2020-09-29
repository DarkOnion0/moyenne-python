"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Moyenne",
    version = "3.0.0",
    description = "Ce programme calcul votre moyenne",
    executables = [Executable("moyenne-console.py")],
)