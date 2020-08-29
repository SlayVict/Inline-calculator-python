import re
import math

# expressio = input("Write math expressio: ")
expressio = 'sqrt(4*sqrt(200+sqrt 3136))'
print(expressio)

def simplify(expressio):
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
  expressio = expressio.replace("multipli", "*")

  expressio = expressio.replace("divide", "/")
  expressio = expressio.replace("divide by", "/")

  expressio = expressio.replace(" ", "")
  return expressio

expressio = simplify(expressio)
print(expressio)

def searchSqrt(expressio):
  while(True):
    isEndFirst = False
    isEndSecond = False

    found=re.search(r'sqrt\(([^\(\)\D]|\.|\+|\*|/|-)*\)', expressio)
    if found:  
      step = found[0][5:-1]
      stepAnswer = str(math.sqrt(eval(step)))
      print(f'sqrt({step}) = {stepAnswer}')
      expressio = expressio.replace(f'sqrt({step})', stepAnswer)
    else:
      isEndFirst = True
      print("No steps for sqrt()")

    found=re.search(r'sqrt\d+.?\d+', expressio)
    if found:  
      step = found[0][4:]
      stepAnswer = str(math.sqrt(eval(step)))
      print(f'sqrt{step} = {stepAnswer}')
      expressio = expressio.replace(f'sqrt{step}', stepAnswer)
    else:
      isEndSecond = True
      print("No steps for sqrt")
    
    if isEndFirst and isEndSecond:
      break
  return expressio

expressio = searchSqrt(expressio)

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