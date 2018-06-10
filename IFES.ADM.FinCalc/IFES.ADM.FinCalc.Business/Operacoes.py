from math import log

class Operacoes(object):
    """description of class"""

    ### INICIO JUROS SIMPLES #################################                                      <--
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
    ### FIM JUROS SIMPLES ######################################                                    <--

    ### INICIO JUROS COMPOSTOS #################################                                    <--
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
        return taxa * 100;
    #end JurosCompostosJuros

    def JurosCompostosPeriodo(self, juros, capital, taxa):
        taxa = taxa / 100.0
        montante = capital + juros
        periodo = log(montante / capital) / log(1 + taxa)
        return periodo
    #end JurosCompostosJuros

    ### FIM JUROS COMPOSTOS ####################################                                    <--


    ### DESCONTO SIMPLES COMERCIAL #############################                                    <--
    def DescontoSimplesComercialDesconto(self, nominal, taxa, periodo):
        taxa = taxa / 100.0
        desconto = nominal * taxa * periodo
        return desconto;
    #end DescontoSimplesComercialDesconto

    def DescontoSimplesComercialNominal(self, desconto, taxa, periodo):
        taxa = taxa / 100.0;
        nominal = desconto / (taxa * periodo);
        return nominal;
    #End DescontoSimplesComercialNominal

    def DescontoSimplesComercialTaxa(self, desconto, nominal, periodo):
        taxa = desconto / (nominal * periodo);
        taxa = taxa * 100;
        return taxa;
    #End DescontoSimplesComercialTaxa

    def DescontoSimplesComercialPeriodo(self, desconto, nominal, taxa):
        taxa = taxa / 100.0;
        periodo = desconto / (nominal * taxa);
        return periodo;
    #End DescontoSimplesComercialPeriodo
    ### DESCONTO SIMPLES COMERCIAL #############################                                    <--

  
    ### Desconto Simples Racional ##############################                                    <--
    def DescontoSimplesRacionalDesconto(self, nominal, taxa, periodo):
        desconto = (nominal * taxa * periodo) / (100 + (taxa * periodo));
        return desconto;
    #End DescontoSimplesRacionalDesconto

    def DescontoSimplesRacionalNominal(self, desconto, taxa, periodo):
        # Formula : Dr = Vn * i * t / (100 + i * t);
        left = desconto * (100 + (taxa * periodo)); # Dr * (100 + i * t) = (Vn * i * t)
        nominal = left / (taxa * periodo) # (left / i * t) = Vn
        return nominal;
    #End DescontoSimplesRacionalNominal

    def DescontoSimplesRacionalTaxa(self, desconto, nominal, periodo):
        taxa = -((100 * desconto) / ((desconto * periodo) - (nominal * periodo)))
        return taxa;
    #End DescontoSimplesRacionalNominal
    ### Desconto Simples Racional #############################                                     <--

