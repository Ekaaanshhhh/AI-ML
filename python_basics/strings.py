a='ekansh'
b='ekasnh'
c=a+b#concatenation
print(len(c));


#slicing a string
#taking parts out of a particular string
#is called slicing
str = "ekanshsatsangi"
print(str[2:6]);#prints from index 2 to 5
print(str[3:]);#prints sxtring from 3 to end



# F-STRINGS AND FORMATTING
a = 5
b = 10

#format method
print("The sum  is {}".format(a+b))
print("The sum of {} and {} is {}".format(a,b,a+b))


#index based  formatting

print("The sum of {1} and {2} is {0}".format(a+b,a,b));



#value based formatting

print("The value of a is {a} and b is {b} ".format(a=5,b=10))


#F string

print(f"sum of {a} and {b} is {a+b}")