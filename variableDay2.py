num_char=len("hello")
print(type(num_char))
print("there are "+str(num_char)+" char in Hello")
divisor=int(input())
dividend=int(input())
quotient=round(divisor/dividend)
quotient *=5
print(quotient)
#f string is used to print multiple data types without changing the data type of each variable
score=5
height=1.5
winning=False
print(f"your score is {score}, your height is {height}, your winning value is {winning}")