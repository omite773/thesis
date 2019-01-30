from time import sleep
from smbus2 import SMBusWrapper
import struct
address = 0x08

# Give the I2C device time to settle
sleep(2)
def get_data():
    try:
        with SMBusWrapper(1) as bus:
            return bus.read_i2c_block_data(address, 99, 16)#lagg till 16?
    except:
        print("Error happend :(")
        return -1
        

def get_float(data, index):
    bytes = bytearray(data[4*index:(index+1)*4])
    return struct.unpack('f', bytes)[0]

data = get_data()
if(data != -1):
    temp = round(get_float(data,0),2)
    c = round(get_float(data,1),2)
    helo = round(get_float(data,2),2)
    print(temp)
    print(c)
    print(helo)
    
"""    

try:
    with SMBusWrapper(1) as bus:
        data = bus.read_i2c_block_data(address, 99, 3)
        print(data)
except:
    print(' Oops! Error')

# Decreasing delay may create more transmission errors.
"""
sleep(0.0005)
