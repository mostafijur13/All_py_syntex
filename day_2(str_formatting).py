#(Formating) means replacing placeholders with actual values to build a final string:
age=21
name="omi"

print("%s is %d years old" %(name,age))#To use two or more argument specifiers, use a tuple (parentheses)

#alternative:

print(f"{name} is {age} years old")

#alternative:

format_data="%s is %d years old"
print(format_data %(name,age))# injecting (name,age) values into format_data's placeholders


#(Use of tuple(peranthesis))

data=("omi",21) #works just as list to hold multiple types of data . but unlike list the data inside cant be changed

print("%s is %d years old" %data)

#alternative:

print(f"{data[0]} is {data[1]} years old")


#(Formating of list)

my_list=[1,2,3]

print("My lis is:%s"%my_list)#Any object which is not a string can be formatted using the %s operator.
print(f"My list is:{my_list}")

#(basic argument specifiers):

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase

#(Exercise)
#You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.

data=("John", "Doe", 53.44)
format_string="Hello %s %s. Your current balance is $%s"
print(format_string %data)








