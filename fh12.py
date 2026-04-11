outputfile = open('updatesfile.txt','w')
inputfile = open('repeated.txt','r')
lines_seen_so_far = set()
print('eliminating duplicate lines..')
for line in inputfile:
    if line not in lines_seen_so_far:
        outputfile.write(line)
        lines_seen_so_far.add(line)
inputfile.close()
outputfile.close()