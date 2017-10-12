<?php
$lat = $_GET['lat'] ;
$lng = $_GET['lng'] ;
$command = escapeshellcmd('python roomGetter.py '.$lat.' '.$lng);
$output = shell_exec($command);

echo $output;

?>