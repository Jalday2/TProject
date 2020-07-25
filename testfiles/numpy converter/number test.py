import numpy as np

#vals1, vals2 = np.loadtxt('cart.dat', skiprows = 0, unpack = True)

#print vals1
#print vals2

#f = open('cart.dat', 'r')

#f_numbers = f.readline()


#print(f_numbers)

#

#f.close

tempNum = 0.0
position = 0
sign = 1
power = 1.0



with open('cart.dat', 'r') as f:
	for line in f:
		if not line.startswith("#"):
			x = 0
			position = 0
			power = 0
			sign = 1
			while x < len(line)-1:
				if line[x] is "-" and line[x+2] is ".":
					sign = -1
				elif line[x] is "E":
					power = float(line[x+2]) * 10 + float(line[x+3])
					if line[x+1] is "-":
						power = -power
					x = x + 3
					#print power
					print (tempNum*sign*pow(10,float(power)))
					position = 0
					power = 0
					sign = 1
					tempNum = 0.0
				elif line[x] is ",":
					print(",")
				elif not line[x] is "-" and not line[x] is " " and not line[x] is "." and not line[x] is "+" and not line[x] is ",":					
					tempNum += float(line[x]) * pow(10,-position)
					#print(float(line[x]) * pow(10,-position))
					#print tempNum
					position+=1				
				x+=1

			






