import socket
import base64
import threading
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import tkinter as tk
from tkinter import scrolledtext

KEY = b"thisisasecretkey"  # 16 bytes

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

class ChatApp:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("127.0.0.1", 5555))

        self.window = tk.Tk()
        self.window.title("🔐 Encrypted Chat App")

        self.chat_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD)
        self.chat_area.pack(padx=10, pady=10)
        self.chat_area.config(state="disabled")

        self.msg_entry = tk.Entry(self.window, width=40)
        self.msg_entry.pack(side=tk.LEFT, padx=10, pady=10)

        self.send_btn = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_btn.pack(side=tk.RIGHT, padx=10)

        threading.Thread(target=self.receive_messages, daemon=True).start()

        self.window.mainloop()

    def send_message(self):
        msg = self.msg_entry.get()
        if msg:
            enc = encrypt_message(msg)
            self.client.send(enc)
            self.display_message("You: " + msg)
            self.msg_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                data = self.client.recv(4096)
                if data:
                    dec = decrypt_message(data)
                    self.display_message("Friend: " + dec)
            except:
                break

    def display_message(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state="disabled")

if __name__ == "__main__":
    ChatApp()
