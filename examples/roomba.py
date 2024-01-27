import picar_4wd as fc
import time
import random

speed = 10
angle = 50

def main():
    threshold = 30
    distance = check_view()
    while True:
        if distance < threshold:
            time.sleep(.2)
            fc.backward(speed*2)
            fc.stop()
            turn = random.randint(-90, 90)
            print("turn: ", str(turn))
            fc.turn_right(turn)
            distance = check_view()
            print("distance: ", str(distance))
        else:
            time.sleep(.2)
            distance = check_view()
            print("distance", str(distance))
            fc.forward(speed)

def check_view(fov = 40):
    dist_list = []
    for i in range (angle - fov, angle + fov, 10):
        distance = fc.get_distance_at(i)
        if distance == -2:
            distance = 100
        dist_list.append(distance)
    return (min(dist_list))

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
