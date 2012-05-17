<?php
// widget.php

function widget_message($message){
    $html = "<div class=\"widget\" id=\"message\">";
    $html .= "<span id=\"timestamp\">".$message->timestamp."</span><br/>";
    $html .= "<span id=\"author\">".link_user($message->author)."</span><br/>";
    $html .= "<span id=\"text\">".$message->text."</span>";
    $html .= "</div>";
    return $html;
}

function widget_task($task){
    global $visitor;
    $html = "<span class=\"widget\" id=\"task\">";
    $html .= "<span class=\"".$task->status($visitor)."\">";
    $html .= link_project($task->project)."/";
    $html .= link_task($task);
    $html .= "</span>";
    $html .= "</span>";
    return $html;
}
?>
