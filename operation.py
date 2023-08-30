from abc import ABC, abstractmethod

class Operation:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    @abstractmethod #Así para que los hijos lo redefinan con la operación correspondiente
    def get_result(self):
        pass