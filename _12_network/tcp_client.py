import socket, time

"""Sample of TCP client"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('[Client] Try to connect to server.')
s.connect(('localhost', 9999))

welcome_str = s.recv(1024).decode('UTF-8')
print('[Client] Receive welcome info from server: %s.' % welcome_str)

for name in ['Tom', 'Ken', 'Mary']:
    print('[Client] Send request: %s' % name)
    s.send(name.encode('UTF-8'))
    response = s.recv(1024).decode('UTF-8')
    if response:
        print('[Client] Server response: %s' % response)
    time.sleep(1)

print('[Client] Disconnect from server.')
s.send('exit'.encode('UTF-8'))
