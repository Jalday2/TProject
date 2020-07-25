import numpy as np
import pandas as pd
import xlsxwriter

#tempNum = 0.0
#position = 0
#sign = 1
#power = 1.0

TextIn = ["orbels.dat", "cart.dat"]
TextOut = ["orbelsNoC.dat", "cartNoC.dat"]

print(TextIn[0],TextIn[1],TextOut[0],TextOut[1])

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
		
	ExportExcel = xlsxwriter.Workbook('Export.xlsx')
	ExportSheet = ExportExcel.add_worksheet()
	
	row = 0
	col = 0
	
	print(len(MJD))
	
	for X in range(0,len(MJD)):
		ExportSheet.write(row, col, X)
		#ExportSheet.write(row, col+1, VX)
		
		row+=1
	ExportExcel.close()	
					



			
