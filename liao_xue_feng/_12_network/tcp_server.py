import socket, threading, time

"""Sample of TCP server"""


def handler(sock, addr):
    print('[Server %s] accepted new connection.' % threading.current_thread().getName())
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('UTF-8') == 'exit':
            break
        sock.send(('Hello %s' % data.decode('UTF-8')).encode('UTF-8'))
    sock.close()
    print('[Server %s] closed connection.' % threading.current_thread().getName())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9999))
s.listen(10)
print('[Server] began to listen.')

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=handler, args=(sock, addr))
    t.start()
