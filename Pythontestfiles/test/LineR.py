cont = int(input("how many inputs? : "))

for x in range(0, cont):
	file1=open('file1.txt','r')
	file2=open('file2.txt','r')
	
	linesIn = file1.readlines()
	linesOut = file2.readlines()
	file2=open('file2.txt','w')

	for z in range(0,16):
		print(linesOut[2],linesIn[1])	
		linesOut[z]=linesIn[z]

	file2.writelines(linesOut)
	
	file1.close()
	file2.close()
	
	b = input("enter to continue : ")
