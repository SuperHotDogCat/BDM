import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
def gather_data():
    alcohol_data = []
    try:
        while True:
            data = ser.readline().decode("utf-8").strip()
            alcohol_data.append(data)
            print(data)
            time.sleep(1)
            # Arduino A0の値:  A0: 101 みたいな感じで出力されます。
    except KeyboardInterrupt:
        with open("alcohol_data.txt", "w") as f:
            for d in alcohol_data:
                f.write(d)
                f.write("\n")
        ser.close()


if __name__ == "__main__":
    gather_data()