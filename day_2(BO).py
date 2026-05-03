#(arithmetic operator)

number=float((9+2*4/4.0)-1.4) #add,sub,multi,devision
print(float(number))

reminder=12%5 #provides reminder of a devision
print(reminder)

square=2.5**5 # to the power of
print(f"{square}")

import math
root=math.sqrt(16) #square root
print(root)

import cmath
neg_root=cmath.sqrt(-1) #complex root
print(neg_root)


#(using operator with string)

a="hello"*10
print(a) #the only arithmetic operator that works between a str and a number.

b="hell"+"hitler" #other arithmetic operator works within the same variable
print(b)

#(using operator with list)

my_list=[1,2,3,4]
your_list=[5,6,7,8]
print(my_list+your_list) #can be joined with additional opperator
our_list=my_list+your_list
print(our_list)

print(my_list*10) # lists with a repeating sequence using the multiplication operator
mul_list=my_list*10
print(mul_list)

world_list=["omi",1]
add_world_list=world_list+["rahman"] #though list can contain varies types of data. 
print(add_world_list)






