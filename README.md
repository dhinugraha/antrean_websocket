# WEBSOCKET SERVER UNTUK KIOSK DISPLAY ANTREAN

Berdasarkan dari simple-websocket-server

~~https://pypi.org/project/simple-websocket-server/~~
https://github.com/dpallot/simple-websocket-server

Mendukung path atau group, sehingga implementasi bisa terpusat
misal : 
/devel/loket1/
/production/loket1/

Menggunakan database sqlite untuk mendukung proses threading timer (jeda waktu broadcast antar antrean)
antrean.db untuk single path
antrean-multi.db untuk path/group

- **pastikan ada python 2,7 dan 3.x :**
```
python -V
```

- **install module pendukung :**
```
~~pip install simple_websocket_server --user~~
Untuk membuat websocket ini menjadi lebih sederhana, modul pendukung tidak dipakai lagi, langsung dari source code SimpleWebSocketServer

Khusus python 3
pip install configparser
```

- **Edit file config.txt**

server : blank untuk semua interface

delay : dalam detik, integer
``` 
[config]
server=localhost
port=8000
delay=5
```
- **chmod :**
```
chmod +x websocket
chmod +x main.py
```
- **Testing service :**
```
python main.py

Untuk debug :
python main-debug.py

untuk multipath/group
python main-debug-group.py
python main-group.py
```

- **Jalankan service (khusus linux) :**
```
~~websocket start~~
Belum diimplementasikan
```
- **Perintah lain (khusus linux) :**
``` 
~~websocket stop~~
~~websocket restart~~
Belum diimplementasikan
```

File binary windows dibangun menggunakan pyinstaller :
pyinstaller --onefile --noconsole --hidden-import simple-websocket-server --hidden-import configparser main-group.py