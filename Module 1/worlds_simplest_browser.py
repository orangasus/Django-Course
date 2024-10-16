# kinda like a file you can send data to and receive data from
import socket

# Making the phone
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Dial the phone: domain + port
mysock.connect(('data.pr4e.org', 80))
# Creating the command
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
# Sending the command. We're the browser -> need to talk first
mysock.send(cmd)

# Receiving
while True:
    data = mysock.recv(512)
    # if we get no data -> socket closed
    if len(data) < 1:
        print('--> Connection closed')
        break
    # printing received data
    print(data.decode(), end='')

# Hanging up
mysock.close()
