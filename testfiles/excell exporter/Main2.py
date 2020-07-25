import numpy as np
import pandas as pd

TextIn = ["orbels.dat", "cart.dat"]
TextOut = ["orbelsNoC.dat", "cartNoC.dat"]

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

		for o in range(2):
			outLoc = "./out/Orbitals" + str(o) + ".xlsx"

			df = pd.DataFrame({"MJD" : MJD, "SMA": SMA, "ECC" : ECC, "INC" : INC,"RAAN" : RAAN, "AOP" : AOP, "MA" : MA})
			df.to_excel(excel_writer = outLoc)
				
		print("end orbitals")

	else:
		MJD, X, Y, Z, VX, VY, VZ = np.loadtxt(TextOut[j], skiprows = 3, unpack = True)
		
		df = pd.DataFrame({"MJD" : MJD, "X": X, "Y" : Y, "Z" : Z,"VX" : VX, "VY" : VY, "VZ" : VZ})
		df.to_excel(excel_writer = "Cartesian.xlsx")
