# 🔐 Encrypted Chat Application

This project is a secure chat application that I built to understand how real-world messaging systems protect user data using encryption.
Instead of sending normal readable messages over the network, this application **encrypts every message first**, sends it securely, and then decrypts it on the receiver’s side.

In simple words — users chat normally, but behind the scenes everything is protected using cryptography.

---

## 🎯 Why I built this project

During my internship task, I wanted to move beyond basic chat applications and build something that actually focuses on **security**.
So I decided to create a chat system where:

- Messages are never sent as plain text
- Data is protected from network sniffing
- The system follows the idea of **secure communication**

This helped me understand how apps like WhatsApp, Signal, and Telegram work internally.

---

## 🧠 What I actually implemented

Here’s what I worked on step by step:

1. Built a **client-server chat system** using Python sockets
2. Added **AES encryption** so every message is encrypted before sending
3. Used a fresh **IV (Initialization Vector)** for each message to improve security
4. Implemented **decryption on the receiver side** so only the intended user can read the message
5. Converted the terminal-based system into a **GUI desktop application** using Tkinter
6. Added debugging logs to clearly show:
   - encrypted message being sent
   - encrypted message being received
   - decrypted final output

So the user experience is simple, but the backend follows real security practices.

---

## 🔁 How the system works (simple flow)

1. User types a message in the app
2. Message gets encrypted using AES
3. Encrypted data is sent to the server
4. Server forwards it to the other client
5. Receiver decrypts the message
6. User sees the normal readable message

So even if someone intercepts the network traffic, they will only see **encrypted data**, not the real message.

---

## 🚀 Features

- AES encryption & decryption
- Secure client-server communication
- GUI-based desktop chat app
- No plaintext messages over the network
- Multi-client support
- Clean project structure
- Easy to run and test

---

## 🛠️ Tech Stack Used

- Python
- Socket Programming
- AES Encryption (PyCryptodome)
- Tkinter (for GUI)
- Git & GitHub

---

## ▶️ How to run this project

### 1. Install required library
```bash
pip install pycryptodome
2. Start the server
bash
Copy code
python server.py
3. Run the chat app
bash
Copy code
python chat_app.py
Open the app in two terminals or two systems to test secure chatting.

📸 Project Screenshots
Screenshots of the working application, encrypted logs, and chat UI are available in the screenshots folder.

🎓 What I learned from this project
How encryption works in real applications

Importance of protecting data in transit

Basics of cryptography and key handling

Client-server architecture

Writing clean and structured code

Using GitHub for professional project hosting

This project gave me confidence to work on more security-focused applications in the future.

👤 Author
Vinayak Rudrawar
Intern – Cyber Security