import socket

target_host = "10.254.25.5"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("HELLOWORLD!", (target_host, target_port))

data, addr = client.recvfrom(4096)

print "addr: "+addr+"\r\n"
print data