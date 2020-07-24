#Opens the text files with the multiple object and input settings
ObjectM =open('MultipleObject.txt','r')
linesInObj = ObjectM.readlines()
InputM =open('MultipleInput.txt','r')
linesInInp = InputM.readlines()

#gets the lines in the multiple object and input settings in float and int form
countObjM = int(len(linesInObj)/16)
fcountObjM = len(linesInObj)/16
countInM = int(len(linesInInp)/46)
fcountInM =  len(linesInInp)/46

#next 2 if statements check if the multiple input files have the correct amount of lines
if (fcountObjM - countObjM) > 0:
	print('MultipleObject.txt has invalid amount of lines')
	exit()
	
if (fcountInM - countInM) > 0:
	print('MultipleInput.txt has invalid amount of lines')
	exit()

#for loop that changes the input and object settings in thalassa and runs it
for x in range(0, countObjM):
	#opens and imports lines to python to be read then exported
	inputf=open('input.txt','r')
	linesOutInp = inputf.readlines()
	objectf=open('object.txt','r')
	linesOutObj = objectf.readlines()
	inputf=open('input.txt','w')
	objectf=open('object.txt','w')

	#replaces object lines in thalassa from multiple object file
	for z in range(0,16):
		print(z)
		print(linesOutObj[z],linesInObj[z])	
		linesOutObj[z]=linesInObj[z + 16 * x]
		
	#stops replacing input settings if there is only one or 2
	if countInM > x:
		print(countInM)
		#countInM -= 1
		for z2 in range(0,46):
			print(z2)
			print(linesOutInp[z2],linesInInp[z2])	
			linesOutInp[z2]=linesInInp[z2 + 46 * x]
	
	#writes and closes files
	objectf.writelines(linesOutObj)
	inputf.writelines(linesOutInp)
	objectf.close()
	inputf.close()
	
	b = input("enter to continue : ") 

ObjectM.close()
InputM.close()
