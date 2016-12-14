##Braine academy. Python course. Laboratory №2
  
<b> Laboratory Work #2.1.</b>
<div>
<i>Write the code to do following:</i>
    <ol>
        <li>Create any variable with name var1</li>
        <li>Check type of var1 with type function</li>
        <li>Check is var1 is True</li>
        <li>Check is var1 is False</li>
        <li>Create var2 that equal to (var1 or True)</li>
        <li>Check is var2 is True</li>
        <li>Check is var2 is False</li>
        <li>Check result for var2 and var1</li>
     </ol>
</div>
<h6> Here is its solution code:</h6>

```Python
# 1. Create any variable with name var1
var1=15
#2. Check type of var1 with type function
print(("type(var1)="),type(var1))
#3. Check is var1 is True
print("true_var1",bool(var1))
#4. Check is var1 is False
print("false_var1", not bool(var1))
# 5. Create var2 that equal to (var1 or True)
var2=16
#6. Check is var2 is True
print("true_var2",bool(var2))
#7. Check is var2 is False
print("false_var2", not bool(var2))
#8. Check result for var2 and var1
print("var1=",var1,", var2=",var2)
```

<b> Laboratory Work #2.2.</b>
<div>
<i>Write the code to do following:</i>
    <ol>
        <li>Generate sequence 5 integers long from range(0, 100)</li>
        <li>Generate random float</li>
        <li>Print variables above</li>
        <li>Find max element from generated sequence</li>
        <li>Make a floor division between max element and generated float</li>
        <li>Find factorial of the result above</li>
        <li>Shorten the code as much as possible</li>
     </ol>
</div>
<h6> Here is its solution code:</h6>

```Python
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
#7. Shorten the code as much as possible
```