from socket import *


def createServer():
    # Creating the phone
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        # Willing to receive phone calls on port 9000
        serversocket.bind(('localhost', 9000))
        # Asking OC hold off other phone calls
        serversocket.listen(5)
        # Waiting for incoming request
        while True:
            # Ready to pick the phone up, next line runs only after the call is received
            clientsocket, address = serversocket.accept()

            # We are the server -> we listen first
            # Reading data
            rd = clientsocket.recv(5000).decode()
            # Splitting data
            pieces = rd.split("\n")
            # Printing first part of the request
            print(pieces[0])

            # Creating a response
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            # Sending the response
            clientsocket.sendall(data.encode())
            # Closing the connection
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serversocket.close()


print('Access http://localhost:9000')
createServer()
