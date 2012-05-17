<?php
// links.php

require_once("config.php");

function url($view, $object=null){
    $url = CONTROLLER;
    if ($view){
        $url .= "?view=".$view;
        if (in_array($view, array("user", "task", "project"))){
            $url .= "&$view=".$object->id;
        }
    }
    return $url;
}

function link_user($user){
    return ("<a class=\"user\" href=\"".url("user",$user)."\">".$user->username."</a>");
}

function link_task($task){
    return ("<a class=\"task\" href=\"".url("task",$task)."\">".$task->name."</a>");
}

function link_project($project){
    return ("<a class=\"project\" href=\"".url("project",$project)."\">".$project->name."</a>");
}

function link_dashboard(){
    return ("<a class=\"dashboard\" href=\"".url(null)."\">StorkL</a>");
}

?>
