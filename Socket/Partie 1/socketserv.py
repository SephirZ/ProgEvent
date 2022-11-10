import socket

host = '127.0.0.1'
port = 6824

def server_program():
    server = socket.socket()
    server.bind((host, port))
    server.listen(5)
    conn, address = server.accept()
    print("Connection depuis : "+str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            server.close()
            print('Utilisateur deconnecté, retour à l\'écoute')
            server_program()
        elif data =="arret":
            break
        print("Reçu d'un utilisateur connecté : "+str(data))
        data = input(' Répondre :  ')
        if data =="arret":
            break
        conn.send(data.encode())
    server.close()

if __name__ == '__main__':
    server_program()