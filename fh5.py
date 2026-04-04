file = open("sample.txt","r")
print(file.read())
file.close()

file = open("sample.txt","r")
print("\n Hey \n")
print(file.read(8))
file.close()

file = open("sample.txt","a")
file.write("This is shruti and iam 14 year old")
file.close()