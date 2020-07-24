import os
import subprocess
import numpy as np

#this line runs thalassa
os.system("cd Thalassa\n ./thalassa.x in/input.txt in/object.txt") 

TextIn = ["./out/orbels.dat", "./out/cart.dat"]
TextOut = ["./editedOut/orbelsNoC.dat", "./editedOut/cartNoC.dat"]

#this for loop makes a copy of the ouptut file with no commas then converts that file into numpy arrays
for j in range(2):
	
	TempTxtIn=open(TextIn[j],"r+")
	ExchangeC=TempTxtIn.read()
	
	ExchangeC=ExchangeC.replace(',',' ')
	
	TempTxtOut=open(TextOut[j],"w+")
	TempTxtOut.write(ExchangeC)
	
	TempTxtIn.close()
	TempTxtOut.close()

	if (j == 0):
		MJD, SMA, ECC, INC, RAAN, AOP, MA = np.loadtxt(TextOut[j], skiprows = 3, unpack = True)
		
		print("MJD\n",MJD)
		print("SMA\n",SMA)
		print("ECC\n",ECC)
		print("INC\n",INC)
		print("RAAN\n",RAAN)
		print("AOP\n",AOP)
		print("MA\n",MA)
		print("end orbitals")

	else:
		MJD, X, Y, Z, VX, VY, VZ = np.loadtxt(TextOut[j], skiprows = 3, unpack = True)

		print("MJD\n",MJD)
		print("X\n",X)
		print("Y\n",Y)
		print("Z\n",Z)
		print("VX\n",VX)
		print("VY\n",VY)
		print("VZ\n",VZ)
