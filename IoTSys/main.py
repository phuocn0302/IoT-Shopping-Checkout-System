
import time
from datetime import datetime
import sys
import RPi.GPIO as GPIO
from hx711 import HX711

import cv2 as cv

#================ HX 711 SETUP ===============
GPIO.setwarnings(False)
hx = HX711(5,6)
hx.set_reading_format("MSB", "MSB")

reference_unit = 416
hx.set_reference_unit(reference_unit)

hx.reset()

hx.tare()

#=============================================

def take_picture(name: str):
    cap = cv.VideoCapture(0)
    while(cap.isOpened()):
        ret, frame = cap.read()
        cv.imwrite('image/' + name + '.png', frame)

        cap.release()

def get_weight() -> float:
    return round(hx.get_weight(5), 3)

def in_range(num: float, _from: float, _to: float) -> bool:
    return _from <= num and num <= _to

#================ MAIN FUNCTION ===============


if __name__ == '__main__':
    buffer_weight_value: float = get_weight()
    weight_offset: float = 5;
    print('You can add items now')

    while True:
        try:
            if in_range(get_weight(), buffer_weight_value - weight_offset, buffer_weight_value + weight_offset):
                continue

            print("Taking picture in: ") 
            for i in range(5, 0, -1):
                time.sleep(1)
                print(i)

            weight_value: float = get_weight();
            take_picture(datetime.now().strftime('%H:%M:%S') + '@'  + str(weight_value))
            print('Weight value: ' + str(weight_value))
            buffer_weight_value = weight_value

        except (KeyboardInterrupt, SystemExit):
            print("Exit program")
            sys.exit()

