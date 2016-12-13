##Braine academy. Python courle. Laboratory №2
  
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