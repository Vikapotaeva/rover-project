class Calculation:
    num1 = None
    sign = None
    num2 = None
    
    def f(self, num1, sign, num2):
        self.num1 = num1
        self.sign = sign
        self.num2 = num2
    
def counts(num1, sign, num2):
        if sign == '+': return(num1 + num2)
        if sign == '-': return(num1 - num2)
        if sign == '*': return(num1 * num2)
        if sign == '/': return(num1 / num2)
        if sign == '**' or sign == '^':  return(num1 ** num2)
        if sign == 'sqrt': return(num1 ** (1/num2))

Calculator = Calculation()
Calculator.f(int(input('number1: ')), input('sign: '), int(input('number2: ')))

print(counts(Calculator.num1, Calculator.sign, Calculator.num2))










    


