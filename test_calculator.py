import unittest
from calculadora import Calculadora

class Testes(unittest.TestCase):

  def teste_adicao(self):
    calculadora= Calculadora()
    self.assertEqual(10,calculadora.adicao(5,5))
  
  def teste_subtracao(self):
    calculadora= Calculadora()
    self.assertEqual(2,calculadora.subtracao(5,3))
  
  def teste_subtracao_negativo(self):
    calculadora= Calculadora()
    self.assertEqual(-2,calculadora.subtracao(3,5))