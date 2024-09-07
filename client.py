import socket
import threading


SERVER_IP = 'thor.pylex.xyz'
SERVER_PORT = 10244

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            print("Error receiving message.")
            break

def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    
    username = input("Enter your username: ")
    client_socket.send(username.encode('utf-8'))


    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()


    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

if __name__ == "__main__":
    start_client()
