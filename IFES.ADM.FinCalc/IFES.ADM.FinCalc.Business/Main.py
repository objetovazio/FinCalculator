import sys
from Operacoes import *
import os

clear = lambda: os.system('cls')

def floatInput(message):
        return float(input(message).replace(",", "."));
#end floatInput

def printOptions():
    print("\nSelecione a operação desejada: ");
    print("  1. Juros Simples");
    print("  2. Juros Compostos");
    print("  3. Desconto Simples Comercial");
    print("  4. Desconto Simples Racional");
    print("  0. Sair")
#end printOptions

def intTryParse(val):
    try:
        return True, int(val);
    except:
        return False, -1;
#end intTryParse

def JurosCalculate(this, function, message):
    print("\n * Operação de " + message + " foi selecionada.\n")
    try:
        capital = floatInput("> Digite o valor do capital: ");
        taxa = floatInput("> Digite o valor da taxa em %: ");
        periodo = floatInput("> Digite o periodo: ");

        resposta = function(capital, taxa, periodo);
        print("\nJuros: %.2f | Montante: %.2f" % (resposta, capital + resposta))

        print("\nDeseja realizar essa operação novamente? (S ou N)")
        
        if(input("\n> ").upper() == "S"):
            clear()
            this(this, function, message)
        #endIf
    except:
        clear()
        print("\nInsira apenas dados numéricos válidos.")
        this(this, function, message)
    #End TryCatch
#End JurosCalculate

def Juros(operacao, typeOperation):
    if(typeOperation == 1):
        JurosCalculate(JurosCalculate, operacao.JurosSimples, "Juros Simples")
    else:
        JurosCalculate(JurosCalculate, operacao.JurosCompostos, "Juros Compostos")
#end Juros

def DescontoCalculate(this, function, message):
    print("\n * Operação de " + message + " foi selecionada.\n")
    try:
        nominal = floatInput("> Digite o valor do nominal: ");
        taxa = floatInput("> Digite o valor da taxa em %: ");
        periodo = floatInput("> Digite o periodo: ");

        resposta = function(nominal, taxa, periodo);
        print("\nDesconto: %.2f | Valor Final: %.2f" % (resposta, nominal - resposta))

        print("\nDeseja realizar essa operação novamente? (S ou N)")
        
        if(input("\n> ").upper() == "S"):
            clear()
            this(this, function, message)
        #endIf
    except:
        clear()
        print("\nInsira apenas dados numéricos válidos.")
        this(this, function, message)
    #End TryCatch
#end DescontoComercial

def Desconto(operacao, typeOperation):
    if(typeOperation == 3):
        DescontoCalculate(DescontoCalculate, operacao.DescontoSimplesComercial, "Desconto Comercial")
    else:
        DescontoCalculate(DescontoCalculate, operacao.DescontoSimplesRacional, "Desconto Racional")
#end Juros

def main():
    operacao = Operacoes();
    typeOperation = 99;

    while(typeOperation > 0):
        printOptions();
        typeOperation = input("\n > ")
        
        validation, typeOperation = intTryParse(typeOperation);
        if(not validation or typeOperation > 4):
            typeOperation = 99;
            print("\nSelecione uma opção válida.")
            continue;
        #end IF

        clear()

        if(typeOperation == 1 or typeOperation == 2):
            Juros(operacao, typeOperation);
        elif(typeOperation == 3 or typeOperation == 4):
            Desconto(operacao, typeOperation);
        ##End If/Elif
        clear()
    #End While

#end Main()
    

if __name__ == "__main__":
    sys.exit(int(main() or 0))