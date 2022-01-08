import unittest
from calculator import Calculadora

class Testes(unittest.TestCase):

  def teste(self):
    calculadora= Calculadora()
    self.assertEqual(10,calculator.adicao(5,5))