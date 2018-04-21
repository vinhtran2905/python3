fw = open('sample.txt','w')

fw.write('writing some stuff in my text file\n')
fw.write('new line is coming')

#free memory
fw.close()


fr = open('sample.txt','r')
line = fr.read()
print(line)

fr.close()