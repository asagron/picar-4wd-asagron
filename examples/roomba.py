import picar_4wd as fc
import time
import random

speed = 10
angle = 50

def main():
    threshold = 20
    distance = 100
    while True:
        if distance < threshold and distance != -2:
            time.sleep(.2)
            fc.backward(speed*2)
            fc.stop()
            turn = random.randint(-90, 90)
            print("turn: ", str(turn))
            fc.turn_right(30)
            distance = fc.get_distance_at(angle)
            print("distance: ", str(distance))
            check_view()
        else:
            time.sleep(.2)
            distance = fc.get_distance_at(angle)
            print("distance", str(distance))
            fc.forward(speed)
            check_view()

def check_view(fov = 40):
    dist_list = []
    for i in range (angle - fov, angle + fov, 10):
        distance = fc.get_distance_at(i)
        dist_list.append(distance)
    print(dist_list)

            


        # time.sleep(1)
        # scan_list = fc.scan_step(35)
        # if not scan_list:
        #     continue

        # tmp = scan_list[3:7]
        # print(tmp)
        # if tmp != [2,2,2,2]:
        #     angle = random.randint(-30, 30)
        #     fc.stop()
        #     fc.backward(speed/2)
        #     fc.turn_right(angle)
        # else:
        #     fc.forward(speed)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
