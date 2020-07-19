file1=open('file1.txt','r')
file2=open('file2.txt','r')

linesIn = file1.readlines()
linesOut = file2.readlines()
file2=open('file2.txt','w')

print(linesOut[2],'\n',linesIn[1])	
linesOut[2]=linesIn[1]

file2.writelines(linesOut)
	
file1.close()
file2.close()
