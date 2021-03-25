import cv2 as cv
import pySerial
import radar
import schedule

connected = False
serial = None
radar = radar.Radar()
try:
    serial = pySerial.PySerial()
    connected = True
except:
    print("could not connect serial")


def parse_msg(msg):
    degree = int(msg[0])
    distance = int(msg[1])
    radar.calc_draw_point(degree, distance)


def clean_up_lines():
    radar.clean_up_lines()


def clean_up_dots():
    radar.clean_up_dots()


schedule.every(0.1).seconds.do(clean_up_lines)
schedule.every(1).seconds.do(clean_up_dots)

# for degree in range(0, 360):
#     radar.calc_draw_point(degree, 240)

cv.waitKey(1)

if connected:
    while True:
        schedule.run_pending()
        if serial.ser.inWaiting():
            line = serial.read_line()
            print(line)
            parse_msg(line)
        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break
    serial.close_conn()
