import struct

data_in = open("c:/Users/mayn/Desktop/ble_tx125k_6slot.txt") 
binfile = open("BLE_PN9_LR125K_6SLOT","wb+")
for x in data_in: 
        s = struct.pack('B',int(x,16))
        binfile.write(s)
binfile.close()
