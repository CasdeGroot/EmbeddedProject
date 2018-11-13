import threading, multiprocessing
import time
import serial
import sys


def open_serial_port(port=""):
    print ("Open port %s" % port)

    port = None

    try:
        port = serial.Serial(port,
                    baudrate=2400,
                    bytesize=serial.EIGHTBITS,
                    parity =serial.PARITY_ODD)

    except serial.SerialException as msg:
        print( "Error opening serial port %s" % msg)

    except:
        exctype, errorMsg = sys.exc_info()[:2]
        print ("%s  %s" % (errorMsg, exctype))

    return port


def read_serial_data(queue, stopped, serialPort):
    print("start reading data");

    while not stopped.is_set():
        data = ''

        try:
            data = serialPort.readline()

        except:
            exctype, errorMsg = sys.exc_info()[:2]
            print("Error reading port - %s" % errorMsg)
            stopped.set()
            break

        if len(data) > 0:
            queue.put(data)
        else
            queue.put("NO DATA")

    serialPort.close()
    print("Read_Data finished.")



