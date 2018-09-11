#!/usr/bin/python


# Open the license file, read the content into the buffer 
# then close the file descriptor

f = open('conditions.py')
lines10 = f.read(10)
#alllines = f.read()
print (lines10)
f.close()

# Open the license file, read the content as "lines" into the 
# buffer and close it.

f = open('conditions.py')
file_content = f.readlines()
f.close()