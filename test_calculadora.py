# importando o pacote dos testes unitarios

import unittest

# Importando a classe 'Calculadora' pelo arquivo 'calculadora.py'
from calculadora import Calculadora

# Criando a classe de teste unitarios chamada 'Testcalculadora'
class TestCalculadora (unittest.TestCase):
    #criando o metodo de definição do objeto que herdara a classe "Calculadora"

    def setUp(self):
        self.calc = Calculadora()

    # Criando o teste do metodo 'soma' da classe 'calculadora'

    def test_soma(self):
        self.assertEqual(self.calc.soma(10, 20), 30)

    # Criando o teste do metodo 'subtração' da classe 'calculadora'

    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(10, 20), -10)

    # Criando o teste do metodo 'Multiplicação' da classe 'calculadora'

    def test_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(10, 20), 200)

    # Criando o teste do metodo 'divisão' da classe 'calculadora'

    def test_divisao(self):
        self.assertEqual(self.calc.divisao(100, 20), 5)

    # Criando o teste do metodo 'resto' da classe 'calculadora'

    def test_resto(self):
        self.assertEqual(self.calc.resto(10, 20), 10)

    #Chamando a classe de Testes unitarios

if __name__ == '__main__':
        unittest.main()