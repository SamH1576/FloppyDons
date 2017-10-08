<?php

$command = escapeshellcmd('python API_TEST.py');
$output = shell_exec($command);
echo $output;

?>