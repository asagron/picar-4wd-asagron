import picar_4wd as fc
import time
import random
import math

angle = 10

def main():
    while(True):
        distance = fc.get_distance_at(angle-60)
        for i in range (-60, 61, 5):
            distance = fc.get_distance_at(angle + i)
            x = distance * math.sin(i)
            y = distance * math.cos(i)
            print("Angle " + str(i) + ": " + str(distance) + "Coord: " + str(x) + "," + str(y))
            time.sleep(1)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()