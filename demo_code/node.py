from socket import *
from threading import *

HOST = "127.0.0.1"  # The server's hostname or IP address on localhost
PORT = 33500  # The port used by the server

#sending to the server node list of EV
def SendToServer(nodeList): 
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(nodeList)
        data = s.recv(1024)

    print(f"Received {data!r}")

#receiving node list of EV and eta of the EV which is communicating with the RSU
def Receiving(sock):
    while True:
        # decode data and use c.py to send it
        data, addr = sock.recvfrom(1024)
        data = data.decode('ascii')
        nodes, eta = data.split('/')
        nodes = nodes.strip()
        nodes = nodes.split(' ')
        print("Travel Route: ", nodes, "\nETA to first node: ", eta)
        print("Start clearing traffic between ", nodes[0], " and ", nodes[1])
        if len(nodes)>2:
            SendToServer(data[1:].encode('ascii'))


my_addr =('10.35.70.4',33501) # Ensure Hostname is correct using hostname -I
#t_ip = '127.0.0.1' 
#target =(t_ip, 65432)
#node_table = {'C':(t_ip, 65432)}


s = socket(AF_INET, SOCK_DGRAM)
s.bind(my_addr)

print("waiting connection")



x = Thread(target=Receiving, args=(s,))
x.start()

#wel="OK!"
#for key in node_table:
    #target = node_table[key]
    #s.sendto(wel.encode('ascii'), target)
