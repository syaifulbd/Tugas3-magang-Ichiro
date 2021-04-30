import socket
import threading
import random

def ReceiveData(sock):
    while True:
            data, addr = sock.recvfrom(1024)
            print(data.decode('utf-8'))

def RunClient(serverIP):
    # Mendeklarasikan IP address server
    server = (str(serverIP), 5000)

    # Mengambil IP addres dan mengambil port
    host = socket.gethostbyname(socket.gethostname())
    port = random.randint(6000, 10000)
    print('Client IP->' + str(host) + ' Port->' + str(port))

    # Membuat socket baru
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Mengikat IP address dan port ke socket
    s.bind((host, port))

    # Memasukkan nama user
    name = input('Write your name: ')

    # Kondisi jika user tidak memasukkan nama
    if name == '':
        name = 'Guest'+str(random.randint(1000, 9999))
        print('Your name is:' + name)

    # Mengirim nama user ke server
    s.sendto(name.encode('utf-8'), server)

    threading.Thread(target=ReceiveData, args=(s,)).start()

    flag = 0
    while True:
        #Memasukkan pesan yang ingin dikirim
        message = input()

        # Kondisi jika ingin menyudahi
        if message == 'quit':
            flag=1
            break

        # kondisi jika tidak menulis pesan
        elif message == '':
            continue

        # Mengirim nama dan pesan
        message = '[' + name + ']' + '->' + message
        s.sendto(message.encode('utf-8'), server)

    if flag!=1:
        # Membaca pesan dari orang lain yang dikirim server
        while True:
            data, addr = s.recvfrom(1024)
            print(data.decode('utf-8'))
    
    s.close()
    exit(1)

ip = input ("Write server's IP address: ")
RunClient(ip)