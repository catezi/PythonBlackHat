import socket

target_host = "0.0.0.0"
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("I am from TCPClient!")

response = client.recv(4096)

print response