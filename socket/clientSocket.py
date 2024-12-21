import socket

s = socket.socket()

port = 12345

s.connect(('192.168.1.175', port))

file = open('send.mp4', 'rb')
file_chunk = file.read(2048)

while file_chunk:
    s.send(file_chunk)
    file_chunk = file.read(2048)

file.close()
s.close()
