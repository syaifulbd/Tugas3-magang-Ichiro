import socket
import threading
import queue

def RecvData(sock, recvPackets):
    while True:
        data, addr = sock.recvfrom(1024)
        recvPackets.put((data, addr))

def RunServer():
    # Mengambil IP address dan menentukan port
    host = socket.gethostbyname(socket.gethostname())
    port = 5000
    print('Server hosting on IP-> ' + str(host))

    # Membuat socket baru
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Mengikat address dan port ke socket
    s.bind((host, port))

    # Deklarasi set client
    clients = set()

    # Deklarasi queue data yang dikirim
    recvPackets = queue.Queue()

    print('Server Ready!')

    threading.Thread(target=RecvData, args=(s, recvPackets)).start()

    while True:
        while not recvPackets.empty():
            data, addr = recvPackets.get()

            # Jika ada client baru
            if addr not in clients:
                clients.add(addr)
                continue

            # Membac pesan
            data = data.decode('utf-8')

            # Kondisi untuk menghentikan server
            if data.endswith('close'):
                clients.clear()
                s.close()
                exit(1)

            # Mencetak pesan
            print(str(addr) + data)

            # Mengirim pesan ke semua client yang bukan pengirim
            for c in clients:
                if c != addr:
                    s.sendto(data.encode('utf-8'), c)

RunServer()

