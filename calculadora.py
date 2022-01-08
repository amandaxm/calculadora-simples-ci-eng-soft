import math
class Calculadora:

  def adicao(self, x, y):
    return(x+y)

  def subtracao(self,x, y):
    return(x-y)
  
  def divisao(self, x, y):
    if y == 0:
      return(0)
    else :
      return(x/y)
  
  def multiplicacao(self, x, y):
     return(x*y)

  def maior(self, x, y):
    if(x==y):
      return("iguais")
    if(x > y):
       return(x)
    else:
       return(y)

  def menor(self, x, y):
    if(x==y):
       return("iguais")
    if(x<y):
      return(x)
    else :
       return(y)      
  
  def raiz_quadrada(self, x):
    return math.pow(x, 1/2)