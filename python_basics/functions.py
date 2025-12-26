#blocks of statement performing a specific  task is called a function
#def keyword is used 


def ekansh():
    print("hELLO");


ekansh();#function call


def sum(a,b):
    return a+b


print(sum(3,4))




def average(a,b,c):
    return float((a+b+c)/3);

print(average(1,2,3));


#implement a function that if one parameter is passed it adds 1 to it and returns and if 2 paramteres are passed, it returns thier sum


def sum(a,b=1):
    return a+b

print(sum(5))#b=1 assign hoajaega by default
print(sum(3,4))#b=4 assign hoga



#types of functions are two types, builtin function and user defined functions

#LAMBDA FUNCTIONS ARE RANDOM ANONYMUS FUNCTIONS
#example if i write lambda a,b,c:a+b+c.....it automatically creates a function taking a b and c as input and returning a+b+c as output
#the number of parameters in the labda function can be as many as we want but the expression should only be one
#lambda fucntions are generally used in higher order functions which tkaen and return a function as argument and a return value



addition=lambda a,b,c:a+b+c;

print(addition(1,2,3))



def factorial(n):
    product=1
    for i in range(1,n+1,1):
        product=product*i;
    return product

print(factorial(5))
