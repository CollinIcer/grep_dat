import matplotlib.pyplot as pl 
import math
adc_in = open("c:/Users/mayn/Desktop/ble_tx.data")
#adc_in = open("c:/Users/mayn/Desktop/2M_2402_PRS9_37b_1f.txt")

sin_lut=[]
x=[]
x_ori=[]
y=[]
y2=[]
y_ori=[]
i=0
j=0
z=0

#while(i<128):
#	x.append(i)
#	y.append(int(math.sin(2*math.pi*i/50)*2**9)) #25M /128
#	i=i+1
	
for lines in adc_in:
	dat = int(lines,16) 
	if(dat>=2**11):
		dat=dat-2**12


	if(i==0):
		j=j+1
		x.append(j)
		y.append(dat) #25M /128
	else:
		y2.append(dat)
	i=~i

	z=z+1
	if(z<(40)*32):
		x_ori.append(z)
		y_ori.append(dat) #25M /128
	

pl.plot(x, y,ls="-")
pl.plot(x, y2,ls="-")
pl.show()

#pl.plot(x_ori, y_ori,ls="-")
#pl.show()