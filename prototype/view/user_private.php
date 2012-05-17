<?php
// user.php

$title = "user: ".$user->username;
require_once("inc/header.php");
require_once("inc/content.php");

echo(content_toolbar($visitor));
echo(content_title("USER", $user));
echo(content_div("USER_INVOLVEMENT", $user));
echo(content_div("USER_ASSIGNMENT", $user));
echo(content_div("USER_TRUST", $user));
echo(content_div("USER_TRUST_REQUESTS_MADE", $user));
echo(content_div("USER_TRUST_REQUESTS_RECEIVED", $user));
echo(content_div("USER_REQUEST_TRUST", $user));

require_once("inc/footer.php");
?>
