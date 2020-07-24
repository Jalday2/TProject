import os
import subprocess
import numpy as np
import pandas as pd

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
	inputf=open('./Thalassa/in/input.txt','r')
	linesOutInp = inputf.readlines()
	objectf=open('./Thalassa/in/object.txt','r')
	linesOutObj = objectf.readlines()
	inputf=open('./Thalassa/in/input.txt','w')
	objectf=open('./Thalassa/in/object.txt','w')

	#replaces object lines in thalassa from multiple object file
	for z in range(0,16):
		#print(z)
		#print(linesOutObj[z],linesInObj[z])	
		linesOutObj[z]=linesInObj[z + 16 * x]
		
	#stops replacing input settings if there is only one or 2
	if countInM > x:
		#print(countInM)
		#countInM -= 1
		for z2 in range(0,46):
			#print(z2)
			#print(linesOutInp[z2],linesInInp[z2])	
			linesOutInp[z2]=linesInInp[z2 + 46 * x]
	
	#writes and closes files
	objectf.writelines(linesOutObj)
	inputf.writelines(linesOutInp)
	objectf.close()
	inputf.close()
		
	#this line runs thalassa
	os.system("cd Thalassa\n ./thalassa.x in/input.txt in/object.txt") 

	TextIn = ["./out/orbels.dat", "./out/cart.dat"]
	TextOut = ["./editedOut/orbelsNoC.dat", "./editedOut/cartNoC.dat"]

	#this for loop makes a copy of the ouptut files with no commas then converts those files into numpy arrays and exports them to excel
	for j in range(2):
		
		TempTxtIn=open(TextIn[j],"r+")
		ExchangeC=TempTxtIn.read()
		
		ExchangeC=ExchangeC.replace(',',' ')
		
		TempTxtOut=open(TextOut[j],"w+")
		TempTxtOut.write(ExchangeC)
		
		TempTxtIn.close()
		TempTxtOut.close()

		if (j == 0):
			MJDOrb, SMA, ECC, INC, RAAN, AOP, MA = np.loadtxt(TextOut[j], skiprows = 3, unpack = True)#this is the line that converts the files into numpy arrays
			
			#print("\nMJD\n",MJDOrb,"\nSMA\n",SMA,"\nECC\n",ECC,"\nINC\n",INC,"\nRAAN\n",RAAN,"\nAOP\n",AOP,"\nMA\n",MA,"\nend orbitals")
			
			outLoc = "./out/Orbitals" + str(x+1) + ".xlsx"
			df = pd.DataFrame({"MJD" : MJDOrb, "SMA": SMA, "ECC" : ECC, "INC" : INC,"RAAN" : RAAN, "AOP" : AOP, "MA" : MA})
			df.to_excel(excel_writer = outLoc)

		else:
			MJDCart, X, Y, Z, VX, VY, VZ = np.loadtxt(TextOut[j], skiprows = 3, unpack = True)#this is the line that converts the files into numpy arrays

			#print("\nMJD\n",MJDCart,"\nX\n",X,"\nY\n",Y,"\nZ\n",Z,"\nVX\n",VX,"\nVY\n",VY,"\nVZ\n",VZ)	
			
			outLoc = "./out/Cartesian" + str(x+1) + ".xlsx"
			df = pd.DataFrame({"MJD" : MJDCart, "X": X, "Y" : Y, "Z" : Z,"VX" : VX, "VY" : VY, "VZ" : VZ})
			df.to_excel(excel_writer = outLoc)
	
	#b = input("enter to continue : ") 

ObjectM.close()
InputM.close()
