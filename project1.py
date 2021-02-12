file_name="test.txt"
file=open(file_name,"r")
data=file.read()
words=data.split()

print ('Number of words ::' len (words))
