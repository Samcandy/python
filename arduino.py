from time import sleep
import serial
import sys
#from msvcrt import getch
##==============================================================================
ser =serial.Serial("/dev/ttyACM0", 9600, timeout=2) # Establish the connection on a specific port
##==============================================================================
 
##=======getchar========================
def getchar():
    #Returns a single character from standard input
    key = getch()                    ##Get byte         ex: b'a'
    key_num=ord(key)           ##convert byte to integer    97
    key_chr=chr(key_num)    ##convert integer to char       'a'
    return key_num
##====================================
 
##======Write Serial Command to arduino============
def SerialWrite(command):
    ser.write(command)
    rv=ser.readline()
    #print (rv) # Read the newest output from the Arduino
    print ("last time command: "+rv.decode("utf-8")) 
    sleep(1) # Delay for one tenth of a second
    ser.flushInput()
##====================================
while 1:
    var = raw_input("input somthing...")
    if len(var) == 1:
        SerialWrite(chr(ord(var)))
    else:
        print("Please input again!!!")
     
##=======Get  Ready================
#print("Connecting to Arduino.....")
#for i in range (1,10):
#    rv=ser.readline()
#    print("Loading...")
    #print(rv)
    #Debug print (rv) # Read the newest output from the Arduino
