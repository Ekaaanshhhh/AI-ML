#immutable data types ka collection
#connection of unique elements

marks = {1,2,3,3,3,3,3,3,5,5,5,6}

print(marks) # only 1,2,3,5,6
print(type(marks))#class set
#set is also unordered, koi element aage aur peeche bhi store ho sakta hai
#set.add() is used to add a value to a a set

marks.add(10)
print(marks)

#empty curly braces never create an empty set they always create an empty dictionary
#to create empty set
empty_set= set();
print(empty_set)


marks.add(3)
marks.remove(5)
#marks.clear()#clears the entire set
#marks.pop()    #removes and returns an arbitrary element from the set
#set1.union(set2)`  #returns a set which is the union of set1 and set2
#set1.intersection(set2)  #returns a set which is the intersection of set1
