import sys
from Operacoes import *
import os

clear = lambda: os.system('cls');

os.system('color F');

colorGreen = '\033[92m';
colorRed = '\033[91m';
colorEnd = '\x1b[0m';
WARNING = '\033[93m';

def printMessage(message, sucess):
    if(sucess):
        print(colorGreen + message + colorEnd)
    else:
        print(colorRed + message + colorEnd)
    #endIf
#end printMessage

def printWarning(message):
    print(WARNING + message + colorEnd);
#end printMessage

def printResultJuros(juros, capital, taxa, periodo):
    printMessage("\nCapital: %.2f" % capital, True)
    printMessage("Taxa: %.2f%%" % taxa, True)
    printMessage("Periodo: %.2f" % periodo, True)
    printMessage("Resultado final:\tJuros: %.2f | Montante: %.2f" % (juros, (capital + juros)), True)
#end printResultJuros

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

def printJurosSimplestOptions():
    print("\nO que precisa descobrir? ");
    print("  1. Juros");
    print("  2. Capital");
    print("  3. Taxa");
    print("  4. Periodo");
#end printOptions

def intTryParse(val):
    try:
        return True, int(val);
    except:
        return False, -1;
#end intTryParse

def operatorValidation():
    typeOperation = input("\n > ")
        
    validation, typeOperation = intTryParse(typeOperation);
    if(not validation or typeOperation > 4):
        typeOperation = 99;
        printMessage("\nSelecione uma opção válida.", False);
        return 99, False;
    #end IF

    return typeOperation, True;
#end 

############## JUROS #######################
def JurosCalculateJuros(this, function, message):
    print("\n * Operação de " + message + " foi selecionada.")
    printWarning("\t Descobrir Juros\n");
    try:
        capital = floatInput("> Digite o valor do capital: ");
        taxa = floatInput("> Digite o valor da taxa em %: ");
        periodo = floatInput("> Digite o periodo: ");

        resposta = function(capital, taxa, periodo);
        printResultJuros(resposta, capital, taxa, periodo);

        print("\nDeseja realizar essa operação novamente? (S ou N)")
        
        if(input("\n> ").upper() == "S"):
            clear()
            this(this, function, message)
        #endIf
    except:
        clear()
        printMessage("\nInsira apenas dados numéricos válidos.", False)
        this(this, function, message)
    #End TryCatch
#End JurosCalculate

def JurosCalculateCapital(this, function, message):
    print("\n * Operação de " + message + " foi selecionada.")
    printWarning("\t Descobrir Capital\n")
    try:
        juros = floatInput("> Digite o valor do juros: ");
        taxa = floatInput("> Digite o valor da taxa em %: ");
        periodo = floatInput("> Digite o periodo: ");

        resposta = function(juros, taxa, periodo);
        printResultJuros(juros, resposta, taxa, periodo);

        print("\nDeseja realizar essa operação novamente? (S ou N)")
        
        if(input("\n> ").upper() == "S"):
            clear()
            this(this, function, message)
        #endIf
    except:
        clear()
        printMessage("\nInsira apenas dados numéricos válidos.", False)
        this(this, function, message)
    #End TryCatch
#End JurosCalculate

def JurosCalculateTaxa(this, function, message):
    print("\n * Operação de " + message + " foi selecionada.")
    printWarning("\t Descobrir Taxa\n")
    try:
        juros = floatInput("> Digite o valor do juros: ");
        capital = floatInput("> Digite o valor do capital: ");
        periodo = floatInput("> Digite o periodo: ");

        resposta = function(juros, capital, periodo);
        printResultJuros(juros, capital, resposta, periodo);

        print("\nDeseja realizar essa operação novamente? (S ou N)")
        
        if(input("\n> ").upper() == "S"):
            clear()
            this(this, function, message)
        #endIf
    except:
        clear()
        printMessage("\nInsira apenas dados numéricos válidos.", False)
        this(this, function, message)
    #End TryCatch
#End JurosCalculate

def JurosCalculatePeriodo(this, function, message):
    print("\n * Operação de " + message + " foi selecionada.")
    printWarning("\t Descobrir Periodo\n")

    try:
        juros = floatInput("> Digite o valor do juros: ");
        capital = floatInput("> Digite o valor do capital: ");
        taxa = floatInput("> Digite o valor da taxa em %: ");

        resposta = function(juros, capital, taxa);
        printResultJuros(juros, capital, taxa, resposta);

        print("\nDeseja realizar essa operação novamente? (S ou N)")
        
        if(input("\n> ").upper() == "S"):
            clear()
            this(this, function, message)
        #endIf
    except:
        clear()
        printMessage("\nInsira apenas dados numéricos válidos.", False)
        this(this, function, message)
    #End TryCatch
#End JurosCalculate

def Juros(operacao, typeOperation):
    if(typeOperation == 1):
        message = "Juros Simples";
        clear();
        printJurosSimplestOptions();
        typeOperationJuros, isValid = operatorValidation();

        if(not isValid):
            printMessage("Operação Inválida!", False)
            return;
        #endIf

        clear()

        if(typeOperationJuros == 1):
            JurosCalculateJuros(JurosCalculateJuros, operacao.JurosSimplesJuros, message);
        elif(typeOperationJuros == 2):
            JurosCalculateCapital(JurosCalculateCapital, operacao.JurosSimplesCapital, message);
        elif(typeOperationJuros == 3):
            JurosCalculateTaxa(JurosCalculateTaxa, operacao.JurosSimplesTaxa, message);
        elif(typeOperationJuros == 4):
            JurosCalculatePeriodo(JurosCalculatePeriodo, operacao.JurosSimplesPeriodo, message);
        #End IF
    else:
        message = "Juros Compostos";
        clear();
        printJurosSimplestOptions();
        typeOperationJuros, isValid = operatorValidation();

        if(not isValid):
            printMessage("Operação Inválida!", False)
            return;
        #endIf

        clear()
        #JurosCalculate(JurosCalculate, operacao.JurosCompostosJuros, "Juros Compostos")
    #End IF
#end Juros

############## DESCONTO #######################
def DescontoCalculate(this, function, message):
    print("\n * Operação de " + message + " foi selecionada.\n")
    try:
        nominal = floatInput("> Digite o valor do nominal: ");
        taxa = floatInput("> Digite o valor da taxa em %: ");
        periodo = floatInput("> Digite o periodo: ");

        resposta = function(nominal, taxa, periodo);
        printMessage("\nDesconto: %.2f | Valor Final: %.2f" % (resposta, nominal - resposta), True)

        print("\nDeseja realizar essa operação novamente? (S ou N)")
        
        if(input("\n> ").upper() == "S"):
            clear()
            this(this, function, message)
        #endIf
    except:
        clear()
        printMessage("\nInsira apenas dados numéricos válidos.", False);
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
        typeOperation, isValid = operatorValidation();

        if(not isValid):
            continue;
        #endIf

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