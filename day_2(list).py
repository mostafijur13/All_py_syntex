#(the basic syntex of list)

a=["omi","sara","sakib"]
print(a[0])
print(a[1],a[2])

#(way of creating list)

b=[]
c=[1,2,3]
d=[1,"omi",True,3.14]# a single variable now can contain varity types of variable

#(kinds of dot notation in list variables)

friend=[] #its empty
friend.append("omi")# adds a any types thing to variable
friend.remove("omi")#remove any types of thingfrom the varuable
friend.extend(["omi","sara"])#add multiple types of thing at once
print(friend,len(friend))#len checks how many are in the varrable
friend.reverse()
print(friend)#uno reverse result 
friend.sort()#alpha lsit get priority

#(uses of true and false)

print("omi"in friend)#true
print("john"in friend)#false
print("sara"in friend)#true
print("sara"not in friend)#false

# (alter way to use extend)

my_list = [1, 2]
my_list = my_list + ["three", 4]# its ok cause in list we can combain varias type of variable in one. rather then the use of + operator would be a syntex error. 

#(Negetive indexing)

lol=[1,2,3]
print(lol[-1])#3
print(lol[-2])#2
print(lol[-3])#1    



#(use of loops in list) 

enemy=["sakip","afrin bitch"]
for x in enemy:
    print(f"fuck you {x}")
    #will lern it leter ;cause its not the funtion part

#(slicing)

n=[1,2,3,4,5]
print(n[1:3])# [2,3]
print(n[:2])#[1,2]
print(n[2:])#[3,4,5]




 




