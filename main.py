import serial
import re
import time

serial_con = '/dev/ttyUSB0' # change this line according to available port

def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a") as file_object:
        # Append text at the end of file
        file_object.write("\n{}".format(text_to_append))

if __name__ == '__main__':
    # SET SERIAL VALUE OF ARDUINO ON RASPI
    ser = serial.Serial(serial_con, 9600, timeout=1)
    ser.flush()

    while True:
        if ser.in_waiting > 0:
            # READLINE FROM ARDUINO
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            append_new_line('jump.txt', line)
            time.sleep(0.01)
