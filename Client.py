'''
Run Server.py first to establish server
client will send message first while server receives
to quit type "/q"
'''
import socket  # for socket
import sys

#establish socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#same ip addressa and port as server
host = '127.0.0.1'
port = 1234

#connect to server
server.connect((host, port))
print("enter message to send...\n")

while True:
    #read in message to send
    message = sys.stdin.readline()
    #check for quit
    if message == '/q\n':
        #tell server to quit
        server.send(message.encode('UTF-8'))
        break
    server.send(message.encode('UTF-8'))

    data = server.recv(2048)
    if data:
        data = data.decode('UTF-8')
        data.replace('\n', '')
        sys.stdout.write("<Server>: ")
        sys.stdout.write(data)
        sys.stdout.flush()

#close socket
server.close()


