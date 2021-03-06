import cv2 as cv
import pySerial
import radar
import schedule

max_sensor_distance_cm = 60
connected = False
serial = None
radar = radar.Radar(max_sensor_distance_cm)
try:
    serial = pySerial.PySerial()
    connected = True
except:
    print("could not connect serial")


def parse_msg(msg):
    if len(msg) == 0:
        return
    degree = int(msg[0])
    distance = int(msg[1])
    radar.calc_draw_point(degree, distance)


schedule.every(0.01).seconds.do(radar.clean_up_lines)
schedule.every(1).seconds.do(radar.clean_up_dots)

while connected:
    schedule.run_pending()
    if serial.ser.inWaiting():
        line = serial.read_line()
        print(line)
        parse_msg(line)
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        serial.close_conn()
        break
