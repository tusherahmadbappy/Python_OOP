import math 
class Calculator:
  
    def user_input(self):
        self.num1 = int(input("Enter the first number: "))
        self.num2 = int(input("Enter the second number: "))

    def add(self):
        return self.num1+self.num2
    def sub(self):
        return  math.fabs(self.num1-self.num2)
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2
    def mod(self):
        return self.num1%self.num2

ob1 = Calculator()
ob1.user_input()
print(ob1.add())
print(ob1.sub())
print(ob1.mul())
print(ob1.div())
print(ob1.mod())
