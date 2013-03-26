import serial
import re
import sys

SENDSMS = True
def sendSMS(number, message):
  global SENDSMS
  if(re.match('^\+373[0-9]{8}$', number) and SENDSMS):
    modem = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
    data = ''
    modem.write("AT+CMGF=1\r")
    modem.write('AT+CMGS="' + number + '"\r')
    modem.write(message.replace('\r\n', '').replace('  ', ' '))
    modem.write(chr(26))

    for i in range(0, 20):  # only 20 tries
      data = modem.readline()
      if data[:5] == "+CMGS":
        break

    print data
    modem.close()


if __name__ == '__main__':
  number = sys.argv[1]
  message = sys.argv[2]
  sendSMS(number, message)

