# Source - https://stackoverflow.com/q
# Posted by BlueSun, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-13, License - CC BY-SA 4.0
import socket
from cryptography.fernet import Fernet

HOST = "127.0.0.1"
PORT = 4444

KEY = b"GLpnLBTkUsqcwT5TYpMgQT0c-W_Ust13ybM3ZK5whj8="
crypt = Fernet(KEY)

message = "hello secure world"
encrypted = crypt.encrypt(message.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(encrypted)

print("[+] Message sent")
