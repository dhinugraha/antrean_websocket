GENERIC WEBSOCKET FOR QUEUE KIOSK DISPLAY

Based on simple-websocket-server

https://pypi.org/project/simple-websocket-server/

- pastikan ada python 2.7 atau 3.x :
python -V

- install module pendukung :
pip install simple-websocket-server --user
pip install configparser --user

- file config.txt
server : blank for all interface
delay : in second, integer
 
[config]
server=localhost
port=8000
delay=5

- chmod (khusus linux) :
chmod +x websocket
chmod +x main.py

- Testing service :
python main-debug.py

- Jalankan service (khusus linux) :
websocket start

- Perintah lain (khusus linux) :
websocket stop
websocket restart

