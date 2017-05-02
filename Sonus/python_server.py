from socket import socket
import json

sock = socket()
sock.connect(('localhost', 5786))


def server():
    track_clients = {}
    while True:
        print "waiting for a connection"
        connection, client_address = sock.accept()
        try:
            print "connection from ", client_address
            data = json.loads(connection.recv(1024))
            track_clients[data['id']] = connection

            if data['id'] == 'API_AI':
                conn = track_clients['SONUS']
                conn.sendall(data)
            connection.sendall(json.dumps(data))
        finally:
            pass

if __name__ == '__main__':
    server()
