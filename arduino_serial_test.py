import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
def serial_test():
    try:
        while True:
            data = ser.readline().decode("utf-8").strip()
            print("Arduino A0の値: ", data)
            time.sleep(1)
            # Arduino A0の値:  A0: 101 みたいな感じで出力されます。
    except KeyboardInterrupt:
        ser.close()


if __name__ == "__main__":
    serial_test()