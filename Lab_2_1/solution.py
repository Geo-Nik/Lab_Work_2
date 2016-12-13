'''
Write the code to do following:
1. Create any variable with name var1
2. Check type of var1 with type function
3. Check is var1 is True
4. Check is var1 is False
5. Create var2 that equal to (var1 or True)
6. Check is var2 is True
7. Check is var2 is False
8. Check result for var2 and var1
'''
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


