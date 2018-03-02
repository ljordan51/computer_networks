import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print(s.recv(1024).decode('UTF-8'))

usr = input('Please enter your username: ')

while True:
    msg = input(usr + ': ')
    s.sendto(msg.encode('UTF-8'), (host, port))

s.close()                  # Close the socket when done
