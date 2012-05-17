<?php
// dashboard.php

require_once("inc/header.php");
require_once("inc/content.php");

echo(content_toolbar($visitor));
echo(content_title("DASHBOARD", $visitor));
echo(content_div("USER_INVOLVEMENT", $visitor));
echo(content_div("NEW_PROJECT", $visitor));

?>
