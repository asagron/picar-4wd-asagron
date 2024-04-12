import socket
import picar_4wd as fc
from picar_4wd.adc import ADC

power_val = 50

HOST = "192.168.1.143" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    def Keyboard_control(key):
        global power_val
        #key=readkey()
        print(key)
        if key== b'87\r\n':
            direction = "forward"
            fc.forward(power_val)
        elif key==b'83\r\n':
            direction = "left"
            fc.turn_left(power_val)
        elif key==b'65\r\n':
            direction = "backward"
            fc.backward(power_val)
        elif key==b'68\r\n':
            direction = "right"
            fc.turn_right(power_val)
        else:
            fc.stop()
            direction = "N/A"
        if key==b'q\r\n':
            direction = "N/A"
        return direction

    def power_read():
        power_read_pin = ADC('A4')
        power_val = power_read_pin.read()
        power_val = power_val / 4095.0 * 3.3
        # print(power_val)
        power_val = power_val * 3
        power_val = round(power_val, 2)
        return power_val

    def cpu_temperature():          # cpu_temperature
        raw_cpu_temperature = subprocess.getoutput("cat /sys/class/thermal/thermal_zone0/temp")
        cpu_temperature = round(float(raw_cpu_temperature)/1000,2)               # convert unit
        #cpu_temperature = 'Cpu temperature : ' + str(cpu_temperature)
        return cpu_temperature


    try:
        while 1:
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            if data != b"":
                print(data)
                direction = Keyboard_control(data)
                print(direction)
                power = power_read()
                print(power)
                #temp = cpu_temperature()
                #print(temp)
                client.sendall(data) # Echo back to client
    except: 
        print("Closing socket")
        client.close()
        s.close()   

