<?php
# script to test the webservice

# config
$BASEURL = "http://127.0.0.1:8080/";
header('Content-Type', 'application/json');

function api_call($url, $args){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_VERBOSE, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);     
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST,1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $args);
    $result = curl_exec($ch);
    return $result;
}

# test template
$url = $BASEURL."";
$args = array();
echo(api_call($url, $args));
?>
