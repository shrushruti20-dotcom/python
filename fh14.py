new_file = open('new_file.txt','x')
new_file.close()
import os
print("Checking if my_file exists or not.... ")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")
my_file = open("my_file.txt","w")
my_file.write("Hi iam shruti")
my_file.close()
os.remove('sample.txt')
os.randir('folder')
#duplicating
utputfile = open('updatesfile.txt','w')
inputfile = open('repeated.txt','r')
lines_seen_so_far = set()
print('eliminating duplicate lines..')
for line in inputfile:
    if line not in lines_seen_so_far:
        outputfile.write(line)
        lines_seen_so_far.add(line)
inputfile.close()
outputfile.close()

