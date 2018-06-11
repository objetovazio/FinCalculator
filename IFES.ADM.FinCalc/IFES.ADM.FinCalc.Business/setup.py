#Arquivo usado para criar o executável .exe usando cx_Freeze.
#Comando no cmd: python setup.py build
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"includes" : ["sty"] }

setup(
    name = "FinCalc",
    version = "1.0",
    description = "Calculadora Financeira.",
    options = {"build_exe": build_exe_options},
    executables = [Executable("Main.py", base = "Console")])
