import picar_4wd as fc
import time
import random

speed = 10

def main():
    while True:
        # time.sleep(1)
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print(tmp)
        if tmp != [2,2,2,2]:
            angle = random.randint(-30, 30)
            fc.stop()
            fc.backward(speed/2)
            fc.turn_right(angle)
        else:
            fc.forward(speed)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
