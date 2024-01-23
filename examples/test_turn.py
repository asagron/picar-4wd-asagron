import picar_4wd as fc
import time

try:
    while True:
        for i in range(-90, 90, 10):
            print(i)
            fc.turn_right(i)
            time.sleep(1)
finally:
    fc.stop()
    time.sleep(0.2)