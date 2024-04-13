import socket
import picar_4wd as fc
from picar_4wd.adc import ADC

speed = 50
HOST = "192.168.1.79" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    def Keyboard_control(key):
        global speed
        
        if key== b'Forward\r\n':
            fc.forward(speed)
        elif key==b'Left\r\n':
            fc.turn_left(speed)
        elif key==b'Backward\r\n':
            fc.backward(speed)
        elif key==b'Right\r\n':
            fc.turn_right(speed)
        elif key==b'Quit\r\n':
            fc.stop()
        else:
            fc.stop()

    def power_read():
        power_read_pin = ADC('A4')
        power_val = power_read_pin.read()
        power_val = power_val / 4095.0 * 3.3
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
            
            power = int(power_read())
            print(power)
            
            if data != b"":
                print(data)
                Keyboard_control(data)
                client.sendall(data, power) # Echo back to client
                

    except Exception as e: 
        print("Closing socket")
        print(e)
        fc.stop()
        client.close()
        s.close()   
