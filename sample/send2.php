<?php
  include ("WebsocketClient.php");

  function updatejson($key, $channel, $val){
    $data_antrean = file_get_contents('antrean2.json');
    $obj = json_decode($data_antrean, true);
    $antrian = $val;
    
    $time = rand();

    $message = json_encode(
      array(
        "server"  => "devel", 
        "media"   => "plasma",
        "channel" => $channel, 
        "time"    => $time, 
        "antrian" => $antrian
      )
    );
    $obj[$key] = $antrian;
    $json_object = json_encode($obj);
    file_put_contents('antrean2.json', $json_object);

    return $message;
  }

  $message = updatejson('plasma'.$_GET['id'], 'channel'.$_GET['id'], $_GET['val']);
  
  
  //reset
  if($_GET['id'] == "reset") {
    $data = json_encode(
      array(
        "plasma1" => 0, 
        "plasma2" => 0, 
        "plasma3" => 0
      )
    );

    file_put_contents('antrean2.json', $data);
    $message = json_encode(
      array(
        "server"  => "devel", 
        "reset" => 1
      )
    );
  }

  if($_GET['id'] == "other") {
    $message = json_encode(
      array(
        "server"  => "devel", 
        "other" => "pesan lain",
        "var 2" => "var2",
      )
    );
  }

  $server = 'localhost';
  $group = "/rsai/devel/";
  $client = new WebsocketCient();

  if( $sp = $client->websocket_open($server, 8100, $group, 10, $errstr) ) {
    //echo "Sending message to server: '$message' \n";
    $client->websocket_write($sp, $message);
    echo $message;
    //echo "Server responed with: '" . $client->websocket_read($sp,$errstr) ."'\n";
  } else {
    echo "Failed to connect to server\n";
    echo "Server responed with: $errstr\n";
  }

?>
