from unittest import main, TestCase
import os
import candidatos
import lista
import votos

# limpa o terminal
os.system("cls")

# classe Testes
class Testes(TestCase):

    # teste do cadastro
    def test_cadastro(self):

        candidatos.Sindico.cad_sindico(candidatos.Sindico(
            'Rômulo', 'Minimizar despesas', '37', '99'))
        result = 'Rômulo' in lista.df['Nome'].to_list()
        self.assertTrue(result)
    
    # teste de atualizar
    def test_atualizar(self):
        candidatos.Sindico.cad_sindico(candidatos.Sindico(
            'Carlos', 'Minimizar despesas', '37', '99'))
        lista.df['Proposta'].loc[lista.df['Nome'] ==
                                 'Carlos'] = 'Minimizar gastos desnecessários'
        result = lista.df['Proposta'].loc[lista.df['Nome'] == 'Carlos'].iloc[0]
        expected = 'Minimizar gastos desnecessários'
        self.assertEqual(result, expected)

    # teste da votação
    def test_votos(self):
        for i in range(5):
            votos.votar1('Marcos')

        result = votos.df1.loc[votos.df1['Candidato'] == 'Marcos']['Votos'][0]
        expected = 5
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
