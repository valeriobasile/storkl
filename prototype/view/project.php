<?php
// project.php

$title = "project: ".$project->name;
require_once("inc/header.php");
require_once("inc/content.php");

echo(content_toolbar($visitor));
echo(content_title("PROJECT", $project));
echo(content_div("PROJECT_DESCRIPTION", $project));
echo(content_div("PROJECT_INVOLVEMENT", $project));
echo(content_div("PROJECT_TASKS", $project));
echo(content_div("EDIT_PROJECT", $project));
echo(content_div("NEW_TASK", $project));
echo(content_div("DELETE_PROJECT", $project));

require_once("inc/footer.php");
?>

