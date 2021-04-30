# Tugas3-magang-Ichiro
UDP server-client implementation

# server.py

## Program Flow

1. Mengambil IP addres yang digunakan server dengan memanggil fungsi `socket.gethostname()`
2. Menentukan port yang digunakan server
3. Membuat socket dan memasukkan IP address dan portnya
4. Membaca semua data yang masuk ke dalam socket dan memasukkannya dalam sebuah queue
5. Untuk setiap data yang masuk dilakukan :

- Jika terdapat client baru akan ditambahkan
- Pesan berbentuk byte dibaca dengan memanggil fungsi `bytes.decode()`
- Mencetak pesan di setiap data

6. Mengirim pesan ke semua client yang bukan pengirim
7. Memberi kondisi untuk server berhenti menerima pesan

## Daftar Fungsi
- `RunServer()` untuk menjalankan semua program server, tanpa nilai kembalian
- `RecvData()` untuk menerima data dalam socket, dengan mengembalikan data yang masuk dan alamat IP pengirimnya

# client.py

## Program Flow

1. Memasukkan IP address server yang ingin dimasuki
2. Mengambil IP address yang digunakan client dengan memanggil fungsi `socket.gethostname()`
3. Mengambil port secara random
4. Membuat socket baru dan memasukkan IP address dan port milik client
5. Memasukkan data nama
6. Mengirim data nama ke server
7. Membaca semua pesan yang dikirimkan dengan memanggil fungsi `threading.Thread()`
8. Memasukkan pesan yang ingin dikirimkan
9. Mengirim pesan ke server
10. Membaca dan mencetak pesan dari client lain yang dikirim oleh server
11. Memberikan kondisi untuk selesai, tidak mengirim dan menerima pesan lagi

## Daftar Fungsi
- `RunClient()` untuk menjalankan semua program client, dengan parammeter alamat IP servernya dan tanpa nilai kembalian
- `ReceiveData()` untuk menerima data dalam socket, dengan mengembalikan data yang masuk dan alamat IP pengirimnya


 
