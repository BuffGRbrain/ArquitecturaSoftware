from addition import Addition
from substract import Substraction
from multiplication import Multiplication
from division import Division
from power import Power
from intDivision import IntDivision

class Calculator:
    def __init__(self,num1,oper,num2):
        self.num1 = num1
        self.oper = oper
        self.num2 = num2
    def get_result(self):
        if self.oper == "+":
            result = Addition(self.num1,self.num2)
            return result.get_result()
        elif self.oper == "-":
            result = Substraction(self.num1,self.num2)
            return result.get_result()
        elif self.oper == "*":
            result = Multiplication(self.num1,self.num2)
            return result.get_result()
        elif self.oper == "/":
            result = Division(self.num1,self.num2)
            return result.get_result()
        elif self.oper == "**":
            result = Power(self.num1,self.num2)
            return result.get_result()
        elif self.oper == "//":
            result = IntDivision(self.num1,self.num2)
            return result.get_result()
        else:
            return "Operacion no valida"