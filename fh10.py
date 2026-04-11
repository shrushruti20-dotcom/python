with open('sample.txt','w') as file:
    file.write("Hi iam shruti")
file.close()
with open('sample.txt','r') as file:
    data = file.readline()
    print("Words in the file are....")
    for line in data:
        word = line.split()
        print(word)
file.close()