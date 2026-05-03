#(Len)
string='hello world'#single quote

print(len(string))#counts the number total of char

first_list=["omi","sara","sakib"]
print(len(first_list))# total item in list

#(.Index Finds the position number(Index NO)):

#for list

sec_list=["omi","sara","sakib","omi"]

print(sec_list.index("omi")) #only the first index number
print(sec_list.index("sara"))

#Raging

print(sec_list.index("omi",1))#search from index 1 onward

#for string

name = "omi"
print(name.index("m"))   # Output: 1
print(name.index("o"))   # Output: 0

#(Count):

thir_variable="omiomi"
print(thir_variable.count("o"))#counts the no of total specific letter

thir_list=["omi","sara","sakib","omi"]
print(thir_list.count("omi"))#count the number of idem in list


#(String slicing)

forth_variable="hello,bitch"

# POSITIVE → can reach last char by using one-past-the-end (index 11, doesnt exist, no problem)

print(forth_variable[0:11])   # ✅ full string
print(forth_variable[0:])     #Alternative way
print(forth_variable[:11])    #Alternative way

# NEGATIVE → -1 IS the last char, so stop-before rule kills it, no workaround exists

print(forth_variable[-11:-1]) # ❌ misses last char, always
print(forth_variable[-11:])   # ✅ only fix — leave end blank, means "go till finish"

#Skiping

fifth_variable="Noth ing"

print(fifth_variable[0:8:2]) # step 2, range is 8 → step smaller than range, works fine
# Output: Ntig

print(fifth_variable[0:5:9])
# start at 0 (N), jump 9 → lands at index 9, already past stop (5) → immediately stops
# step (9) is bigger than the range (0 to 5), so only grabs the very first character
# Output: N
# RULE: if step > range, you only ever get the first character then jump past the stop line.

#(Reversed)

sixth_variable="esrever"
rev_variable=sixth_variable[::-1]
print(rev_variable)
print(sixth_variable[::-1])

#(UPPER||LOWER)
#It changes case(transform). string transformation method.

first_input=input()

print(first_input.upper())
print(first_input.lower())

#check with loop

if first_input.upper()==first_input:#it check the varriable is .upper or .lower .
    print("UPPERCASE")
else:
    print("lowercase")   

#alter

if first_input==first_input.upper():#it does the same 
    print("UPPERCASE")
else:
    print("lowercase")

#(Isupper||Islower)
#A Boolean string method used for validation.

if first_input.isupper():#.isupper itself gives a boolen output thats why no need to check it.
    print("UPPERCASE")
else:
    print("lowercase")
    
#alter

if first_input.islower():
    print("lowercase")
else:
    print("UPPERCASE")    

#(Startwith||endswith)
#They check if a string begins or ends with a specific substring.string manipulation, input validation, and filtering data.RESULT:TRUE/FALSE

print(first_input.startswith("o"))  #checks o is here or not 
print(first_input.endswith("i"))


sec_input=input()

if sec_input.startswith("o"):
    print("yes")
else:
    print("no")

if sec_input.endswith("i"):
    print("yes")
else:
    print("no")

#alter. string.startswith(prefix, start, end)

txt = "Hello, welcome to my world."
print(txt.startswith("wel", 7, 20))  #it check through the given index only

#alter

txt = "Hello, welcome to my world."
print(txt.endswith("wel", 7, 20))

#(.split()is a methode )
#syntex: string.split(separator, maxsplit)

seventh_varibale="hello bitch"
print(seventh_varibale.split())#default is it split every phrase in a list way

eight_variable = "apple,banana,cherry"
print(eight_variable.split(",")) # Coustom seperator work like a common char that split.

ninth_variable= "one:two:three:four"
print(ninth_variable.split(":", 2)) # the number says how many first phrase will be seperated . rest of them will remain the same 







   