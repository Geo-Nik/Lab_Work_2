'''
Write the code to perform following task:
    1. Generate sequence 5 integers long from range(0, 100)
    2. Generate random float
    3. Print variables above
    4. Find max element from generated sequence
    5. Make a floor division between max element and generated float
    6. Find factorial of the result above
    7. Shorten the code as much as possible
'''

#Importing the module
import random
import math
#1. Generate sequence 5 integers long from range(0, 100)
rand_int=random.sample(range(100),5)

#2. Generate random float
rand_float=random.random()

#3. Print variables above
print("\n\t3. Print variables above\n")
print("rand_int={},rand_float={}".format(rand_int,rand_float))

# 4. Find max element from generated sequence
max_sequence=max(rand_int)
print("\n\t4. Find max element from generated sequence\n")
print("max(rand_int)=",max_sequence)

#5. Make a floor division between max element and generated float
floore_div=max_sequence//rand_float
print("\n\t5. Make a floor division between max element and generated float\n")
print("max_sequence//rand_float=",floore_div)

#6. Find factorial of the result above
print("\n\t5. 6. Find factorial of the result above\n")
print("factorial(max_sequence//rand_float)=",math.factorial(floore_div))
#7. Shorten the code as much as possible

