#(Boolean logic evaluate condition)

a=3

print(a==3)#TRUE
print(a!=5)#TRUE
print(a>3)#FALSE
print(a<5)#TRUE
print(a>=5)#FASLE
print(a<=7)#TRUE

#(Boolean Operators:AND||OR)

fir_variable="omi"
sec_variable=22

if fir_variable =="omi" and  sec_variable==22:# AND: Checks left → if False, STOPS (no need to check right). Both must True.
    print("yes")
 
if fir_variable =="omi" or sec_variable==22:# OR: Checks left → if True, STOPS (no need to check right). Only one must be True.
    print("yes")

#(IN)

#list

first_list=["omi"]
sec_list=["omi","sara"]

print(first_list in sec_list)#false ;

#string

sec_variable="omi"
thir_variable="omi12345"

print(sec_variable in thir_variable)#true ;

