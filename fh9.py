file = open("sp.txt","r")
content = file.read()
print(content)
file.close()

file  = open("Sp.txt","r")
content = file.read(10)
print(content)
file.close()

file = open("sp.txt","r")
print(file.readline())
print(file.readline())
file.close()

file = open("sp.txt","r")
for line in file:
    print(line)
    file.close()

file = open("sp.txt","r")
count = 0
for line in file:
    count += 1
print("Total lines:",count)
file.close()