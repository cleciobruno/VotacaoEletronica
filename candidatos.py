import lista
class Sindico:
    def __init__(self, nome, proposta, apartamento, numero_chapa):
        self.nome = nome
        self.proposta = proposta
        self.apartamento = apartamento
        self.numero_chapa = numero_chapa

    def cad_sindico(self, candidato = 'Síndico'):
        lista.df.loc[len(lista.df), ['Candidato','Nome','Proposta', 'Apartamento', 'Número da Chapa']] = candidato ,self.nome, self.proposta, self.apartamento, self.numero_chapa

class Secretario:
    def __init__(self, nome, apartamento, numero_chapa):
        self.nome = nome
        self.apartamento = apartamento
        self.numero_chapa = numero_chapa

    def cad_secretario(self, candidato = 'Secretário'):
        lista.df.loc[len(lista.df), ['Candidato','Nome', 'Apartamento', 'Número da Chapa']] = candidato, self.nome, self.apartamento, self.numero_chapa
