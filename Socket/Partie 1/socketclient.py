import socket
host = '127.0.0.1'
port = 6824
def clientchat():
    client= socket.socket()
    client.connect((host, port))
    message = input(" Entrez un message :  ")
    while message.lower().strip() != 'bye':
        client.send(message.encode())
        if message=="arret":
            break
        data = client.recv(1024).decode()
        if data == "bye" or not data:
            break
        print('Reçu du serveur : ' + data)
        message = input(" Répondre :  ")
    client.close()


if __name__ == '__main__':
    clientchat()