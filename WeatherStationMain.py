'''
Created on 6 Jun 2018

@author: Nagelfar
'''
import serial
import time

if __name__ == '__main__':

#    oSerial = serial.Serial('COM5',
#                            '9600',
#                            serial.EIGHTBITS,
#                            serial.PARITY_NONE,
#                            serial.STOPBITS_ONE)

    currTime = time.localtime()
    timeStr = str(currTime.tm_year) +\
        "-" + str(currTime.tm_mon) +\
        "-" + str(currTime.tm_mday) +\
        ", " + str(currTime.tm_hour) +\
        ":" + str(currTime.tm_min)

    print timeStr



'''    
    dataStream = oSerial.read(10)   # Read 10 bytes of data once.

    hexData = []

    for ch in dataStream:
        hexData.append(ch.encode('hex'))

    PM25Lb = hexData[2]
    PM25Hb = hexData[3]
    PM10Lb = hexData[4]
    PM10Hb = hexData[5]

    PM25Lb = int(PM25Lb, 16)
    PM25Hb = int(PM25Hb, 16)
    PM10Lb = int(PM10Lb, 16)
    PM10Hb = int(PM10Hb, 16)

    print "PM2.5: %d" % (((PM25Hb * 256) + PM25Lb) / 10)
    print "PM10: %d" % (((PM10Hb * 256) + PM10Lb) / 10)
'''
    #time.sleep(1)
