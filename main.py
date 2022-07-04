import serial
import re
import time

serial_con = '/dev/ttyUSB0' # change this line according to available port

def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)

if __name__ == '__main__':
    # SET SERIAL VALUE OF ARDUINO ON RASPI
    ser = serial.Serial(serial_con, 9600, timeout=1)
    ser.flush()

    name_txt = 'dataset.txt'

    while True:
        if ser.in_waiting > 0:
            # READLINE FROM ARDUINO
            try:
                line = ser.readline().decode('utf-8').rstrip()
                append_new_line(name_txt, line)
            except:
                print('problem with serial readline')
        print('error or stop occured')
        break