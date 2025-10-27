/*Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
  Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
  Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string*/

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'subtract':
            return self.a - self.b
        elif operation == 'multiply':
            return self.a * self.b
        elif operation == 'divide':
            return self.a / self.b
        else:
            return "Invalid operation"
          
calc = Calculator(10, 2)
print(calc.calculate('add'))
