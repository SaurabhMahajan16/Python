from art import calculator

print(calculator)

def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2

addition="+"
subtraction="-"
multiplication="*"
division="/"
calculator={

    addition:add,
    subtraction:subtract,
    multiplication:multiply,
    division:divide
    

}

def calculation(n1, n2):

    for key in calculator:
        print(key, end=' \t')

    operationCalculator=input("\n pick an operation: ")
    operation=''

    operation=calculator[operationCalculator]
    #print(calculator[key])
    answer=operation(n1, n2)
    print(f"{n1} {operationCalculator} {n2} = {operation(n1, n2)}")
    morecalcualtion=input("do you want to do more calculation yes or no: ")
    print(morecalcualtion)
    if morecalcualtion.lower()== "yes":
            num3=float(input("what is the new number: "))
            calculation(operation(n1,n2), num3)
    else:
         exit


num1=float(input("enter first number: "))
num2=float(input("enter second number: "))
calculation(num1, num2)   


 
        
        
        


