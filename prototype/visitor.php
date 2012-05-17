<?php
// visitor.php
/*
*/

require_once("model/model.php");

// PHP session is required for login
session_start();

if (isset($_SESSION["visitor"])){
    $visitor_id = $_SESSION["visitor"];
    $visitor = new User($visitor_id);
}
else {
    $visitor = null;
}

/* TEMPORARY */
$visitor_id = 1;
$visitor = new User($visitor_id);
?>
