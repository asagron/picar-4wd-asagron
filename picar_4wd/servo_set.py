import picar_4wd as fc
import time
from .servo import Servo

try:
    while True:
        for i in range(-90, 90, 10):
            print(i)
            fc.servo.set_angle(i)
            time.sleep(1)
finally:
    fc.stop()
    time.sleep(0.2)