with open('codingual.txt') as fp:
    data1 = fp.read()
with open('sample_doc.txt') as fp:
    data2 = fp.read()
data1+= "\n"
data += data2
print("Merging two files...")
with open('Mergedfiltxt','w') as fp:
    fp.write(data1)