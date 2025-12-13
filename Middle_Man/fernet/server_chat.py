# Source - https://stackoverflow.com/q
# Posted by BlueSun, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-13, License - CC BY-SA 4.0
#https://stackoverflow.com/questions/56844402/cryptography-fernet-invalidtoken-when-sending-encrypted-message-over-network


import socket
from cryptography.fernet import Fernet

HOST = "localhost"
PORT = 4444

KEY = b"GLpnLBTkUsqcwT5TYpMgQT0c-W_Ust13ybM3ZK5whj8="
crypt = Fernet(KEY)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    print(f"Listening on {HOST}:{PORT}")
    conn, addr = s.accept()

    with conn:
        while True:
            data = conn.recv(2048)
            if not data:
                print("Client disconnected")
                break
            try:
                print(f'decrypt data {data}')
                message = crypt.decrypt(data).decode()
                print("Client:", message)
            except Exception as e:
                print(e)
