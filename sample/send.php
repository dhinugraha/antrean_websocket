<?php
  include ("WebsocketClient.php");

  function updatejson($key, $channel){
    $data_antrean = file_get_contents('antrean.json');
    $obj = json_decode($data_antrean, true);
    $antrian = $obj[$key] + 1;
    
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
    file_put_contents('antrean.json', $json_object);

    return $message;
  }

  if($_GET['id'] == "1") {
    $message = updatejson('plasma1', 'channel1');
  } else if($_GET['id'] == "2") {
    $message = updatejson('plasma2', 'channel2');
  } else if($_GET['id'] == "3") {
    $message = updatejson('plasma3', 'channel3');
  }
  
  //reset
  if($_GET['id'] == "reset") {
    $data = json_encode(
      array(
        "plasma1" => 0, 
        "plasma2" => 0, 
        "plasma3" => 0
      )
    );

    file_put_contents('antrean.json', $data);
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

  $server = '192.168.1.20';
  $group = "/test/";
  $client = new WebsocketCient();


  if( $sp = $client->websocket_open($server, 8000, $group, 10, $errstr) ) {
    //echo "Sending message to server: '$message' \n";
    $client->websocket_write($sp, $message);
    echo $message;
    //echo "Server responed with: '" . $client->websocket_read($sp,$errstr) ."'\n";
  } else {
    echo "Failed to connect to server\n";
    echo "Server responed with: $errstr\n";
  }

?>