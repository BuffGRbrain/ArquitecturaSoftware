from addition import Addition
from substract import Substraction
from multiplication import Multiplication
from division import Division
from power import Power
from intDivision import IntDivision

num1 = float(input("Ingrese el primer numero: ")) #I want to change the input type to do
oper = input("Ingrese la operacion: ")
num2 = float(input("Ingrese el segundo numero: "))
#Pendiente mejorar inputs del usuario
if oper == "+":
    result = Addition(num1,num2)
    print(result.get_result())
elif oper == "-":
    result = Substraction(num1,num2)
    print(result.get_result())
elif oper == "*":
    result = Multiplication(num1,num2)
    print(result.get_result())
elif oper == "/":
    result = Division(num1,num2)
    print(result.get_result())
elif oper == "**":
    result = Power(num1,num2)
    print(result.get_result())
elif oper == "//":
    result = IntDivision(num1,num2)
    print(result.get_result())
else:
    print("Operacion no valida")