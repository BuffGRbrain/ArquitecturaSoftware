from operation import Operation

class Addition(Operation):
    def __init__(self,num1,num2):
        super().__init__(num1,num2) #Hereda de la clase padre

    def get_result(self):
        return self.num1 + self.num2