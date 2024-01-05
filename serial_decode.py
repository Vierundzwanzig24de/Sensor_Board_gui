import sys
import glob
import serial


serial_port_class = serial.Serial()

def listPorts():
    if sys.platform.startswith('win'):
        ports = ["COM%s" % (i+1) for i in range(255)]
    elif sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
        ports = glob.glob("/dev/tty[A-Za-z]*")
    elif sys.platform.startswith("darwin"):
        ports = glob.glob("/dev/tty.'")
    else:
        raise EnvironmentError("Unsopported platform")

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def connectSerial(selected_port):
    global serial_port_class
    serial_port_class = serial.Serial(
            port = selected_port,
            baudrate=115200,
            bytesize=serial.EIGHTBITS,
            timeout = 1
    )
    serial_port_class.isOpen()

def readSerial():
    identifier = serial_port_class.read(1)
    aIn0_value = serial_port_class.read(2).hex()
    aIn0_value = int(aIn0_value,16)
    return aIn0_value

#print(sys.platform)
#print(glob.glob("/dev/tty[A-Za-z]*"))
#port_list = listPorts()
#print(port_list)
#connectSerial(port_list[0])
#for i in range(100):
#    print(readSerial())
