import socket
import picar_4wd as fc

HOST = "192.168.1.143" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

     def Keyboard_control(key):
        while True:
            global power_val
            #key=readkey()
            if key== b"87
                print("forward")
                fc.forward(power_val)
            elif key==b"83":
                print("left")
                fc.turn_left(power_val)
            elif key==b"65":
                print("backward")
                fc.backward(power_val)
            elif key==b"68":
                print("right")
                fc.turn_right(power_val)
            else:
                fc.stop()
            if key==b"q":
                print("quit")  
                break  



    try:
        while 1:
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            if data != b"":
                print(data)
                Keyboard_control(data)
                client.sendall(data) # Echo back to client
    except: 
        print("Closing socket")
        client.close()
        s.close()    

   
