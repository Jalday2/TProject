import numpy as np
import os

TextIn = ["./out/orbels.dat", "./out/cart.dat"]
TextOut = ["./out/orbelsNoC.dat", "./out/cartNoC.dat"]
#for loop takes commas out of file then turns that file into numpy arrays
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
		os.remove("./out/orbelsNoC.dat")
		#print("MJD\n",MJD,"\nSMA\n",SMA,"\nECC\n",ECC,"\nINC\n",INC)
		#print("RAAN\n",RAAN,"\nAOP\n",AOP,"\nMA\n",MA,"\nend orbels")

	else:
		MJD, X, Y, Z, VX, VY, VZ = np.loadtxt(TextOut[j], skiprows = 3, unpack = True)
		os.remove("./out/cartNoC.dat")

		#print("MJD\n",MJD,"\nX\n",X,"\nY\n",Y,"\nZ\n",Z)
		#print("VX\n",VX,"\nVY\n",VY,"\nVZ\n",VZ,"\nend cart")
					



			
