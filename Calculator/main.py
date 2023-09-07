from calculator import Calculator
num1 = float(input("Ingrese el primer numero: "))
oper = input("Ingrese la operacion: ")
num2 = float(input("Ingrese el segundo numero: "))

calc = Calculator(num1,oper,num2)
print(calc.get_result())