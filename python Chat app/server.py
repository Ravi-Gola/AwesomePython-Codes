import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip="127.0.0.1"
port=5555
s.bind((server_ip,port))
s.listen(1)
(connection,address)=s.accept()
print("connected")

while True:
    msg=input("enter your message")
    msg=msg.encode()
    connection.send(msg)
    recv_msg=connection.recv(1024)
    recv_msg=recv_msg.decode()
    print(recv_msg)