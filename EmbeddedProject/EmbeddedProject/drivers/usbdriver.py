import serial
import sys


def open_serial_port(port=""):
    print ("Open port %s" % port)

    port = None

    try:
        port = serial.Serial(port, baudrate=9600)

    except serial.SerialException as msg:
        print( "Error opening serial port %s" % msg)

    except:
        exctype, errorMsg = sys.exc_info()[:2]
        print ("%s  %s" % (errorMsg, exctype))

    print("Opened port %s" % port.name)
    return port


def read_serial_data(queue, stopped, serialPort):
    print("start reading data")

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
        else:
            queue.put("NO DATA")

    serialPort.close()
    print("Read_Data finished.")

if __name__ == '__main__':
    open_serial_port("/dev/ttyS1")




