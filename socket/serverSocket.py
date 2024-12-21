import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("Socket creation failed with error: %s" %(err))

port = 12345

s.bind(('172.22.223.119', port))
print ("Socket binded to %s" %(port))

s.listen(5)
print ("Socket is listening")

c,addr = s.accept()
print ("Got connection from ", addr)

file = open('receive.mp4', 'wb')
file_chunk = c.recv(2048)

while file_chunk:
    file.write(file_chunk)
    file_chunk = c.recv(2048)

file.close()
c.close()

