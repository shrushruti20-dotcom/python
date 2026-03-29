file = open("sample.txt","r")
lines = file.readlines()
print("Total lines is",len(lines))
file.close()