import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

while True:
    s.listen(5)                 # Now wait for client connection.
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    c.send('Thank you for connecting'.encode('UTF-8'))
    while True:
        msg, addr = c.recvfrom(1500)
        print(msg.decode('UTF-8'))

c.close()                # Close the connection
