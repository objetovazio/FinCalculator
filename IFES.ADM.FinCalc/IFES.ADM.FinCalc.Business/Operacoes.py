from math import log

class Operacoes(object):
    """description of class"""

    ### INICIO JUROS SIMPLES ###
    def JurosSimplesJuros(self, capital, taxa, periodo):
        taxa = taxa / 100.0
        juros = capital * taxa * periodo
        return juros
    #End JurosSimples

    def JurosSimplesCapital(self, juros, taxa, periodo):
        taxa = taxa / 100.0
        capital = juros / (taxa * periodo)
        return capital
    #end GetCapitalJurosSimples

    def JurosSimplesTaxa(self, juros, capital, periodo):
        resultado = juros / (capital * periodo)
        taxa = resultado * 100.0
        return taxa
    #end GetTaxaJurosSimples

    def JurosSimplesPeriodo(self, juros, capital, taxa):
        taxa = taxa / 100.0
        periodo = juros / (capital * taxa)
        return periodo
    #end GetPeriodoJurosSimples

    ### FIM JUROS SIMPLES ###

    ### INICIO JUROS COMPOSTOS ###
    def JurosCompostosJuros(self, capital, taxa, periodo):
        taxa = taxa / 100.0
        montante = capital * ((1 + taxa) ** periodo)
        juros = montante - capital
        return juros
    #end JurosCompostosJuros

    def JurosCompostosCapital(self, montante, taxa, periodo):
        taxa = taxa / 100.0
        capital = montante / ((1 + taxa) ** periodo)
        return capital
    #end JurosCompostosJuros

    def JurosCompostosTaxa(self, juros, capital, periodo):
        montante = capital + juros
        taxa = ((montante / capital) ** (1 / periodo)) - 1
        return taxa
    #end JurosCompostosJuros

    def JurosCompostosPeriodo(self, juros, capital, taxa):
        taxa = taxa / 100.0
        montante = capital + juros
        periodo = log(montante / capital) / log(1 + taxa)
        return periodo
    #end JurosCompostosJuros

    ### FIM JUROS SIMPLES ###



    def DescontoSimplesRacional(self, nominal, taxa, periodo):
        desconto = (nominal * taxa * periodo) / (100 + (taxa * periodo))
        return desconto
    #End DescontoSimplesRacional

    def DescontoSimplesComercial(self, nominal, taxa, periodo):
        taxa = taxa / 100.0
        desconto = nominal * taxa * periodo
        return desconto;
    #end DescontoSimplesComercial

  

