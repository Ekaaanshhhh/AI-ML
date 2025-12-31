marks = [10,20,5,40,-1]
print(len(marks))

#list is mutable i.e particular index pe jaake changes kiye jaa sakte hai
marks[3]=35;
print(marks)
print(type(marks))#type is list
print(marks[0:6])#prints 0-5



#append.  adds a value to the last
#insert(idx,val).    adds a value to a particular index
#sort.     sorts the list ascending order me
#reverse    reverses the list

marks.append(2)
print(marks)


marks.insert(10,-3)#if idx>length-1. acts as append only
print(marks)



marks.sort()#sort function kaam nahi krega agar types alag alag hai list me
print(marks)


marks.reverse()
print(marks)


#loops in lists
for marks in marks:
    print(marks)


