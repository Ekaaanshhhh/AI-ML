#stores key:value pairs

student = {
    "name":"Ekansh",
    "class":"ece a",
    "cgpa":8.70
}

print(type(student))#type is dict
print(len(student))#len is 3 i.e no of keys

print(student.get("cgpa"))# 8.70 gets the value corresponding to the key
print(student["cgpa"])

#mtable unordered type of data structure


#functions in dictionary
print(student.keys())#returns all the keys

print(student.values())#returns all the values

print(student.items())#gets all the (key,value) pairs

print(student.get("name"))#gets the value to a particular key


student.update({
    "college":"NITP"
})

print(student)