import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(4096)
            if not msg:
                break
            broadcast(msg, client_socket)
        except:
            break

    clients.remove(client_socket)
    client_socket.close()

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                pass

def main():
    host = "127.0.0.1"
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print("🔐 Encrypted Chat Server started...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connected with {addr}")
        clients.append(client_socket)

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    main()
