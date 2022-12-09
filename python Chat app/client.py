import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip="127.0.0.1"
port=5555
s.connect((server_ip,port))
print("connected")
while True:
    recv_msg=s.recv(1024)
    recv_msg=recv_msg.decode()
    print(recv_msg)
    msg=input("enter your message")
    msg=msg.encode()
    s.send(msg)