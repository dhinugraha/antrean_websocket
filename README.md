# WEBSOCKET SERVER UNTUK KIOSK DISPLAY ANTREAN

Berdasarkan dari simple-websocket-server

https://pypi.org/project/simple-websocket-server/

- **pastikan ada python 3.x :**
```
python -V
```

- **install module pendukung :**
```
pip install simple-websocket-server --user
pip install configparser --user
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
```
- **Jalankan service (khusus linux) :**
```
websocket start 
```
- **Perintah lain (khusus linux) :**
``` 
websocket stop
websocket restart
```

File binary windows dibangun menggunakan pyinstaller :
pyinstaller --onefile --noconsole --hidden-import simple-websocket-server --hidden-import configparser 