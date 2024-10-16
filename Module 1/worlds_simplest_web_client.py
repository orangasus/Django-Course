import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Talking to localhost:9000
try:
    mysock.connect(('127.0.0.1', 9000))
except Exception as e:
    print(f'Unable to connect to 127.0.0.1:9000\n{e}')
else:
    # Sending GET-request
    cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            print('---> Disconnected')
            break
        print(data.decode(), end='')

    mysock.close()