#bin2dat
import binascii
import struct
in_fp = open("pcm24.pcm","rb")
#in_fp = open("pcm_vad.raw","rb")
out_fp = open("in24.dat","w")
num = 10000
while num>0:
	dat0 = struct.unpack("B",in_fp.read(1))
	dat1 = struct.unpack("B",in_fp.read(1))
	dat2 = struct.unpack("B",in_fp.read(1))
	
	
	dat0_int = int(str(dat0[0]))
	dat1_int = int(str(dat1[0]))
	dat2_int = int(str(dat2[0]))
	dat = dat0_int + (dat1_int<<8) + (dat2_int <<16)
	dat_hex = hex(dat & 0xffffff)
	dat_int = int(dat_hex,16)
	if(dat_int>=0x800000):
		dat_int = dat_int - 0x1000000
	#print(dat_str)
	num = num-1
	
	
	if(len(dat1)>0):
		i = 1
		out_fp.write(str(dat_int))
		#out_fp.write(dat_hex)
		out_fp.write("\n")
	else:
		break
		
out_fp.close
#
import binascii
import struct
in_fp = open("test.wav","rb")
out_fp = open("test.dat","w")

while 1:
	dat = in_fp.read(2)
	if(len(dat)>0):
		out_fp.write(str(binascii.b2a_hex(dat)) + '\n')
	else:
		break
		
out_fp.close

#dat2bin
in_fp = open("eqcoef.dat")
out_fp = open("eq_coeh.dat","w")
while 1:
	dat = in_fp.readline()
	if(len(dat)<=0):
		break
	dat_int = int(dat)
	hex_dat = hex(dat_int & 0xffffffff)
	out_fp.write( hex_dat[2:] + "\n")
  
#
import struct
import binascii
in_fp = open("pcm.dat")
out_fp = open("pcm.raw","wb")
while 1:
	dat = in_fp.readline()
	if(len(dat)<=0):
		break
	dat_int = int(dat,16)
	dat_h = dat_int >> 8
	dat_l = dat_int & 0xff
	out_fp.write(struct.pack('B',dat_l))
	out_fp.write(struct.pack('B',dat_h))











