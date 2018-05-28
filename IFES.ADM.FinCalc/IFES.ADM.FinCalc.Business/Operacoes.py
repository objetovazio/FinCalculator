class Operacoes(object):
    """description of class"""

    def JurosSimples(self, capital, taxa, periodo):
        taxa = taxa/100.0;
        resultado = capital * taxa * periodo;
        return resultado;
    #End JurosSimples

    def JurosCompostos(self, capital, taxa, periodo):
        taxa = taxa/100.0;
        montante = capital * ((1 + taxa) ** periodo);
        juros = montante - capital;
        return juros;
    #end JurosCompostos

    def DescontoSimplesRacional(self, nominal, taxa, periodo):
        desconto = (nominal * taxa * periodo) / (100 + (taxa * periodo));
        return desconto;
    #End DescontoSimplesRacional

    def DescontoSimplesComercial(self, nominal, taxa, periodo):
        taxa = taxa/100.0;
        desconto = nominal * taxa * periodo;
        return desconto;
    #end DescontoSimplesComercial

   

