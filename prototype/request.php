<?php
// request.php
/*
Input handler.
Input is in the form of <key, values> pair passed as GET parameters.
Arguments can be zero or more of these:
- view
- user
- task
- project
*/

require_once("model/model.php");
require_once("config.php");
require_once("visitor.php");
require_once("post.php");

// project
if (isset($_GET['project'])){
    $project_id = $_GET['project'];
    $project = new Project($project_id);
}
else {
    $project = null;
}

// task
if (isset($_GET['task'])){
    $task_id = $_GET['task'];
    $task = new Task($task_id);
}
else {
    $task = null;
}

// user
/* 
   This is the view argument, e.g. to look at a user's page,
   not to be confonded with the logged in user (called visitor).
*/
if (isset($_GET['user'])){
    $user_id = $_GET['user'];
    $user = new User($user_id);
}
else {
    $user = null;
}

// view
if (isset($_GET['view'])){
    $view_id = $_GET['view'];
    if ($view_id == "user") {
        if ($user == $visitor) {
            $view_id = "user_private";
        }
        else {
            $view_id = "user_public";
        }
    }
    elseif ($view_id == "logout"){
        // here be logout
        $view_id = "login";
    }
}
else {
    $view_id = DEFAULT_VIEW;
}

if (file_exists(VIEW_DIR.$view_id.".php")){
    $view_file = VIEW_DIR.$view_id.".php";
}
else {
    $view_file = VIEW_DIR.DEFAULT_VIEW.".php";
}

// call the view object
include($view_file);
?>
