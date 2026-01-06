import socket
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

KEY = b"thisisasecretkey"  # 16 bytes key

def pad(msg):
    return msg + b" " * (16 - len(msg) % 16)

def encrypt_message(message):
    iv = get_random_bytes(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(message.encode()))
    return base64.b64encode(iv + encrypted)

def decrypt_message(enc_msg):
    data = base64.b64decode(enc_msg)
    iv = data[:16]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(data[16:])
    return decrypted.strip().decode()

def main():
    host = "127.0.0.1"
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print("Connected to secure chat server 🔐")

    while True:
        msg = input("You: ")
        enc = encrypt_message(msg)
        client.send(enc)

        data = client.recv(4096)
        dec = decrypt_message(data)
        print("Friend:", dec)
        print("Encrypted:", enc)


if __name__ == "__main__":
    main()
