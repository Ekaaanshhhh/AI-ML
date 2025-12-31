tup = (1,2,3,4,5,5,6,"abc",102.45)
print(len(tup))

#tuples are immutable i.e we cannot change a particular index value
#tup[3]=45; #this will give error
print(tup)
print(type(tup))#type is tuple



#functions of tuples
#tup.index(val).  returns the first occurence index of val in tuple

print(tup.index(5));#returns 4

#tup.count(val).  returns the total occurences of the val in tuple

print(tup.count(5))#returns 2