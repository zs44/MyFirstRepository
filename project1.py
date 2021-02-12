file_name="test.txt"
file=open(file_name,"r")
data=file.read()
words=data.split()

number_of_characters=len(data)


print ('Number of words ::',len (words),number_of_characters)
