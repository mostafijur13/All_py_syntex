# Number

# 1st way of definig int (# Same goes for float)
a=7
print(a)
# 2nd way of defining int
a=int(7)
print(a)
# 3rd way of defnig int
a=7
print(int(a))

# String

# 1st . ""is good for all the time cause we can use single quotes as well
text="hello world" 
print(text)
# 2nd
text=str("hello world")
print(text)
# 3rd
text="hello world"
print(str(text))
# 4th
name="omi"
sur="rahman"
print(f"{name}{sur}") #the f("{}{}")  creates a new string object that contains the string representation. the {} covert variaables into string.the type doesnt change . it just convert into str to display
print(f"{3+4}")#see the type doesnt change so the operation was done and display the result as a str
print(f"{"3+4"}")#inside the {}its possible to do again return the str value.

# more way to define variable

one=1
two=2
three=one+two

hello="hello"
world="world"
helloworld=hello+" "+world
print(str(helloworld))

# exception(operator cant be use with multiple types of variables)
# Ex: we can print(hello+world) ;if both the variables are the same type . its wrong to use operator with varies type of variables . Alter way is :
name, age ="omi", 21
print(name,age) #the ","works as a seperator of variables


# way to asign value
a, b =3, 4
print(a,b) # can print many types of variables at the same time

#Excercise
myint=30
mystring="muscle memory"
myfloat=50.56

if mystring == "muscle memory":
    print(f"string:{mystring}")
    print("String: %s"%mystring)
if isinstance(myfloat,float)and myfloat==50.56:
    #ininstace varify the type of variable i am saying is true or false .
    print(f"float:{myfloat}")
    print("float:%f"%myfloat)
if isinstance(myint,int)and myint==30:
     #ininstace varify the type of variable i am saying is true or false .
    print(f"integer:{myint}")
    print("integer:%d"%myint)  
    



