import picar_4wd as fc
import time
import random
import math
import numpy as np
# from scipy.ndimage import maximum_filter

angle = 10
grid_size = 300

def main():
    # map = np.zeros((grid_size, grid_size))
    # for i in range (-60, 0, 5):
    #     x = int(grid_size//2 + round(random.randint(-5, 5)))
    #     y = int(round(random.randint(0,10)))
    #     print("Angle " + str(i) + ": " + " Coord: " + str((x,y)))

    #     map[y-1, x-1] = 1
    # print(map)

    # buffer_size = 1
    # map_buffer = maximum_filter(map, size=2*buffer_size+1, mode='constant', cval=0)
    # print(map_buffer)
    map = np.zeros((grid_size, grid_size))
    while(True):
        distance = fc.get_distance_at(angle-60)
        for i in range (-60, 61, 5):
            distance = fc.get_distance_at(angle + i)
            if distance == -2:
                distance = 150
            x = int(grid_size//2 + round(distance * math.sin(math.radians(i))))
            y = int(round(distance * math.cos(math.radians(i))))
            coord = (x,y)
            print("Angle " + str(i) + ": " + str(distance) + " Coord: " + str(coord))
            map[y-1, x-1] = 1
            time.sleep(1)
        print(map)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()