import random

#random.seed(1)
#if we use random.seed once 

state=random.getstate()
#in order to use set state we have to use this what this does it saves the randomly generated in memory

print('Generating a random sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))
#random.seed(4)
state2=random.getstate()
#in order to use set state we have to use this what this does it saves the randomly generated in memory

print('Generating a random sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))

random.setstate(state)
# this fetches the saved state of previouly generated where in this case was state
print('Generating the same identical sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))

random_int=random.randint(1,500)
print(f"\n random int is {random_int}")

random_float=random.random()*5# this gives floating value and doesnt need any range 
print(f"\n random float is {random_float}")