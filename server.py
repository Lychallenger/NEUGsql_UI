import socket
class server:
    HOST = '219.216.65.81'
    PORT = 6280
    BUF_SIZE = 1024
    ADDR = (HOST, PORT)
    client = socket.socket()
    client.connect(ADDR)
    while True:
        data = input(">>> ")
        if not data: break
        client.send(b"end12323\n")
        recv_data = client.recv(BUF_SIZE)
        if not recv_data: break
        print(recv_data.decode())
    client.close()