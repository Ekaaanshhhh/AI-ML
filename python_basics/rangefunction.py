# prints number within a range

#range(start stop step)

#if start and step is not mentioned then start is considered 0 and step as 1 and it runs upto step-1

for i in range(5):
    print(i);#0,1,2,3,4..start =0  and step = 1


for i in range(1,6):
    print(i);#prints 1,2,3,4,5. since start=1 and end =5 and step=1 automatically considered

for i in range(1,10,3):
    print(i);#prints 1,4,7
