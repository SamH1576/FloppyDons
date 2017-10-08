<?php

$command = escapeshellcmd('python roomGetter.py');
$output = shell_exec($command);
echo $output;

?>