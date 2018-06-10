import sys
import os
from Operacoes import *
from sty import fg, bg, ef, rs

clear = lambda: os.system('cls');

os.system('color F');

def printMessage(message, sucess):
    if(sucess):
        print(fg.green + message + fg.rs)
    else:
        print(fg.red + message + fg.rs)
    #endIf
#end printMessage

def printWarning(message):
    print(fg.yellow + message + fg.rs);
#end printMessage

def printResultJuros(value, capital, taxa, periodo, notMontante = True):
    printMessage("\nCapital: %.2f" % capital, True)
    printMessage("Taxa: %.2f%%" % taxa, True)
    printMessage("Periodo: %.2f" % periodo, True)

    if(notMontante):
        printMessage("Resultado final:\tJuros: %.2f | Montante: %.2f" % (value, (capital + value)), True)
    else:
        printMessage("Resultado final:\tJuros: %.2f | Montante: %.2f" % ((value - capital), value), True)
#end printResultJuros

def printResultDesconto(value, capital, taxa, periodo):
    printMessage("\nNominal: %.2f" % capital, True)
    printMessage("Taxa: %.2f%%" % taxa, True)
    printMessage("Periodo: %.2f" % periodo, True)
    printMessage("Resultado final:\Desconto: %.2f | Valor Líquido: %.2f" % (value, (capital - value)), True)
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

def printJurosSimplesOptions():
    print("\nO que precisa descobrir? ");
    print("  1. Juros");
    print("  2. Capital");
    print("  3. Taxa");
    print("  4. Periodo");
#end printOptions

def printDescontoSimplesOptions():
    print("\nO que precisa descobrir? ");
    print("  1. Desconto");
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
        val = 0;

        isJurosSimples = message == "Juros Simples";

        if(isJurosSimples):
            val = floatInput("> Digite o valor do juros: ");
        else:
            val = floatInput("> Digite o valor do montante: ");
        #endif

        taxa = floatInput("> Digite o valor da taxa em %: ");
        periodo = floatInput("> Digite o periodo: ");

        resposta = function(val, taxa, periodo);
        printResultJuros(val, resposta, taxa, periodo, isJurosSimples);

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
        printJurosSimplesOptions();
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
        printJurosSimplesOptions();
        typeOperationJuros, isValid = operatorValidation();

        if(not isValid):
            printMessage("Operação Inválida!", False)
            return;
        #endIf

        clear()

        if(typeOperationJuros == 1):
            JurosCalculateJuros(JurosCalculateJuros, operacao.JurosCompostosJuros, message);
        elif(typeOperationJuros == 2):
            JurosCalculateCapital(JurosCalculateCapital, operacao.JurosCompostosCapital, message);
        elif(typeOperationJuros == 3):
            JurosCalculateTaxa(JurosCalculateTaxa, operacao.JurosCompostosTaxa, message);
        elif(typeOperationJuros == 4):
            JurosCalculatePeriodo(JurosCalculatePeriodo, operacao.JurosCompostosPeriodo, message);
        #End IF
    #End IF
#end Juros
############## JUROS #######################

############## DESCONTO #######################
def DescontoCalculateDesconto(this, function, message):
    print("\n * Operação de " + message + " foi selecionada.\n");
    printWarning("\t Descobrir Desconto\n");

    try:
        nominal = floatInput("> Digite o valor do nominal: ");
        taxa = floatInput("> Digite o valor da taxa em %: ");
        periodo = floatInput("> Digite o periodo: ");

        resposta = function(nominal, taxa, periodo);
        printResultDesconto(resposta, nominal, taxa, periodo);

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

def DescontoCalculateNominal(this, function, message):
    print("\n * Operação de " + message + " foi selecionada.\n");
    printWarning("\t Descobrir Nominal\n");

    try:
        # desconto, taxa, periodo
        desconto = floatInput("> Digite o valor do desconto: ");
        taxa = floatInput("> Digite o valor da taxa em %: ");
        periodo = floatInput("> Digite o periodo: ");

        resposta = function(desconto, taxa, periodo);
        printResultDesconto(desconto, resposta, taxa, periodo);

        print("\nDeseja realizar essa operação novamente? (S ou N)");
        
        if(input("\n> ").upper() == "S"):
            clear();
            this(this, function, message)
        #endIf
    except Exception as e:
        print(str(e))
        clear();
        printMessage("\nInsira apenas dados numéricos válidos.", False);
        this(this, function, message);
    #End TryCatch
#end DescontoComercial

def DescontoCalculateTaxa(this, function, message):
    print("\n * Operação de " + message + " foi selecionada.\n");
    printWarning("\t Descobrir Taxa\n");

    try:
        # desconto, nominal, periodo
        desconto = floatInput("> Digite o valor do desconto: ");
        nominal = floatInput("> Digite o valor da nominal: ");
        periodo = floatInput("> Digite o periodo: ");

        resposta = function(desconto, nominal, periodo);
        printResultDesconto(desconto, nominal, resposta, periodo);


        print("\nDeseja realizar essa operação novamente? (S ou N)");
        
        if(input("\n> ").upper() == "S"):
            clear();
            this(this, function, message)
        #endIf
    except:
        clear();
        printMessage("\nInsira apenas dados numéricos válidos.", False);
        this(this, function, message);
    #End TryCatch
#end DescontoComercial

def DescontoCalculatePeriodo(this, function, message):
    print("\n * Operação de " + message + " foi selecionada.\n");
    printWarning("\t Descobrir Periodo\n");

    try:
        # desconto, nominal, taxa
        desconto = floatInput("> Digite o valor do desconto: ");
        nominal = floatInput("> Digite o valor da nominal: ");
        taxa = floatInput("> Digite o valor da taxa em %: ");

        resposta = function(desconto, nominal, taxa);
        printResultDesconto(desconto, nominal, taxa, resposta);

        print("\nDeseja realizar essa operação novamente? (S ou N)");
        
        if(input("\n> ").upper() == "S"):
            clear();
            this(this, function, message)
        #endIf
    except Exception as e:
        clear();
        printMessage("\nInsira apenas dados numéricos válidos.", False);
        this(this, function, message);
    #End TryCatch
#end DescontoComercial

def Desconto(operacao, typeOperation):
    if(typeOperation == 3):
        message = "Desconto Simples Comercial";
        clear();
        printDescontoSimplesOptions()
        typeOperationDesconto, isValid = operatorValidation();

        if(not isValid):
            printMessage("Operação Inválida!", False)
            return;
        #endIf

        clear()

        if(typeOperationDesconto == 1):
            DescontoCalculateDesconto(DescontoCalculateDesconto, operacao.DescontoSimplesComercialDesconto, message);
        elif(typeOperationDesconto == 2):
            DescontoCalculateNominal(DescontoCalculateNominal, operacao.DescontoSimplesComercialNominal, message);
        elif(typeOperationDesconto == 3):
            DescontoCalculateTaxa(DescontoCalculateTaxa, operacao.DescontoSimplesComercialTaxa, message);
        elif(typeOperationDesconto == 4):
            DescontoCalculatePeriodo(DescontoCalculatePeriodo, operacao.DescontoSimplesComercialPeriodo, message);

    else:
        message = "Desconto Simples Racional";
        clear();
        printDescontoSimplesOptions()
        typeOperationDesconto, isValid = operatorValidation();

        if(not isValid):
            printMessage("Operação Inválida!", False)
            return;
        #endIf

        clear()

        if(typeOperationDesconto == 1):
            DescontoCalculateDesconto(DescontoCalculateDesconto, operacao.DescontoSimplesRacionalDesconto, message);
        elif(typeOperationDesconto == 2):
            DescontoCalculateNominal(DescontoCalculateNominal, operacao.DescontoSimplesRacionalNominal, message);
        elif(typeOperationDesconto == 3):
            DescontoCalculateTaxa(DescontoCalculateTaxa, operacao.DescontoSimplesComercialPeriodo, message);
        #EndIF
#end Desconto
############## DESCONTO #######################

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