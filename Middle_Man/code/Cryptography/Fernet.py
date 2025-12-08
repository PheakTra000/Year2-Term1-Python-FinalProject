from cryptography.fernet import Fernet


# function to generate the key

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # getting the key
    return open("secret.key", "rb").read()

def encrypting_file(filename):
    # load up the function that returns the key
    key = load_key()
    # create a fernet object
    fernet = Fernet(key)
    with open("secret.txt", 'rb') as file:
        # read the data from the file, now all those data are stored inside that variable
        plaintxt = file.read()
    
    encrypting_data = fernet.encrypt(plaintxt)
    with open("secret.txt", 'wb') as file:
        file.write(encrypting_data)
        
def decrypting_file(filename):

    key = load_key()

    fernet = Fernet(key)
    with open("secret.txt", 'rb') as file:
        
        encrypted_data = file.read()
        decrypting_data = fernet.decrypt(encrypted_data)

    with open("secret.txt", 'wb') as file:
        file.write(decrypting_data)

decrypting_file("secret.txt")
