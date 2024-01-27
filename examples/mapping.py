import picar_4wd as fc
import time
import random

angle = 10

def main():
    while(True):
        for i in range (-60, 61, 60):
            time.sleep(1)
            distance = fc.get_distance_at(angle + i)
            print(str(i), str(distance))
if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()