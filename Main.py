import re
import math
from Calculation import Calculator

# expressio = input("Write math expressio: ")
expressio = 'sqrt(4*sqrt(200+sqrt 3136))'
print(expressio)

def simplify(expressio):
  expressio = expressio.replace("Pi","3.14159265359")
  expressio = expressio.replace("pi","3.14159265359")

  expressio = expressio.replace("E","2.7182818285")
  
  expressio = expressio.replace(",", ".")
  
  expressio = expressio.replace("plus", "+")
  expressio = expressio.replace("and", "+")
  expressio = expressio.replace("with", "+")

  expressio = expressio.replace("minus", "-")
  expressio = expressio.replace("subtract", "-")
  expressio = expressio.replace("without", "-")

  expressio = expressio.replace("times", "*")
  expressio = expressio.replace("multiplied by", "*")
  expressio = expressio.replace("mul", "*")
  expressio = expressio.replace("multiply", "*")

  expressio = expressio.replace("divide", "/")
  expressio = expressio.replace("divide by", "/")

  expressio = expressio.replace(" ", "")
  return expressio

expressio = simplify(expressio)
print(expressio)



expressio = Calculator.searchSqrt(expressio)

while(True):
  found=re.search(r'\([^\(\)]*\)', expressio)
  if found:
    step = found[0][1:-1] 
    stepAnswer = str(eval(step))
    print(f'({step}) = {stepAnswer}')
    expressio = expressio.replace(f'({step})', stepAnswer)
  else:
    print("No steps for ()")
    break

print(expressio)
expressio = str(eval(expressio))
print(expressio)

