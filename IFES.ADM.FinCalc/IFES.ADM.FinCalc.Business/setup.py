#Arquivo usado para criar o executável .exe usando cx_Freeze. Comando no cmd: python setup.py build
import sys
from cx_Freeze import setup, Executable

setup(
    name = "FinCalc",
    version = "1.0",
    description = "Calculadora Financeira.",
    executables = [Executable("Main.py", base = "Console")])
