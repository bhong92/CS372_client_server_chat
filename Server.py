'''
Run Server.py first to establish server
client will send message first while server receives
to quit type "/q"
'''
import socket
import sys


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 1234        # Port to listen on (non-privileged ports are > 1023)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))

server.listen(100)
conn, addr = server.accept()
print(addr[0] + " connected\nWaiting for message...")
tictactoe = [
    [],
    [],
    []
]


print('    |    |    \n')
print('____|____|____\n')
print('    |    |    \n')
print('____|____|____\n')
print('    |    |    \n')
print('    |    |    \n')
while True:
    data = conn.recv(2048)
    if data:
        data = data.decode('UTF-8')
        data.replace('\n', '')
        if data == '/q\n':
            break
        sys.stdout.write("<Client>: ")
        sys.stdout.write(data)
        sys.stdout.flush()

    message = sys.stdin.readline()
    conn.send(message.encode('UTF-8'))

conn.close()
server.close()

