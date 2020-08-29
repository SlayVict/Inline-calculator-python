import re, math

class Calculator():
  # def __init__(self,expressio):
  #   self.expressio = expressio
  
  @staticmethod
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