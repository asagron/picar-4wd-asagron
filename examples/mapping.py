import picar_4wd as fc
import time
import random

def main():
    distance = fc.get_distance_at(50)
    print(distance)
if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()