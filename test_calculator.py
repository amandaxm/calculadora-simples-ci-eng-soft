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
    def teste_divisao(self):
    calculadora= Calculadora()
    self.assertEqual(5,calculadora.divisao(15,3))
  
  def teste_divisao_zero(self):
    calculadora= Calculadora()
    self.assertEqual(0,calculadora.divisao(5,0))
  
  def teste_multiplicacao(self):
    calculadora= Calculadora()
    self.assertEqual(45,calculadora.multiplicacao(15,3))
  
  def teste_multiplicacao_zero(self):
    calculadora= Calculadora()
    self.assertEqual(0,calculadora.multiplicacao(0,10))