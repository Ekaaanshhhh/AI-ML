#file operations, read close and write
#f = open(path,mode)
# r -> read
# w -> write


f = open("/Users/ekanshsatsangi/Desktop/AI:ML/python-extra/sample.txt","r")#this opens up and returns the file object stored in f
data = f.read()#readline will read the data line by line
print(data)

f.close()#its necessary to close the file once you open it


f = open("/Users/ekanshsatsangi/Desktop/AI:ML/python-extra/sample.txt","w")
#now opens this file in the write mode
f.write("something random")

f.close()



#different modes while opening files



