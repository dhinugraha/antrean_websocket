# WEBSOCKET SERVER UNTUK KIOSK DISPLAY ANTREAN

Berdasarkan dari simple-websocket-server

https://pypi.org/project/simple-websocket-server/

### Sample client
- **Support custom path subscriber :**
```
ws://<ip_server:port>/plasma-lantai-1/
ws://<ip_server:port>/plasma-lantai-2/
```
- **Persistent reconnect jika koneksi putus**
```
socket.onclose = function(event) {    
  $("#status").html("Socket is closed. Reconnect will be attempted in 2 seconds.");
  setTimeout(function() {
      $("#status").html("try connecting...");
      connect();
  }, 2000);
};
```
- **Parsing json untuk tiap box**
```
if(msg.channel == "channel1") {
  poli = 1;
  $("#poli1").html(msg.antrian);
  $("#raw1").text(event.data);
}
```
