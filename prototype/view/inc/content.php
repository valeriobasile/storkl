<?php
// content.php

/* in this module are defined functions to produce HTML content
 */
require_once("link.php");
require_once("widget.php");
require_once("html.php");

function content_title($view, $object){
    $content = "<div class=\"title\">";
    if ($view == "DASHBOARD"){
        $content .= ("<h1>".link_dashboard()."/".link_user($object)."'s dashboard</h1>");
    }
    if ($view == "USER"){
        $content .= ("<h1>".link_dashboard()."/".link_user($object)."</h1>");
    }
    if ($view == "TASK"){
        $content .= ("<h1>".link_dashboard()."/".link_project($object->project)."/".link_task($object)."</h1>");
    }
    if ($view == "PROJECT"){
        $content .= ("<h1>".link_dashboard()."/".link_project($object)."</h1>");
    }
    $content .= "</div>";
    return $content;
}



function content_div($content, $object){
    global $visitor;
    
    /* USER contents */
    if ($content == "USER_INVOLVEMENT"){
        $div_title = "Projects in which ".link_user($object)." is involved";
        $list_items = array();
        foreach ($object->involvement() as $involved_project){
            if ($involved_project->owner == $object) {
                $list_items[] = link_project($involved_project)." (owner)";
            }
            else {
                $list_items[] = link_project($involved_project);
            }
        }

        return make_content_div_html($div_title, make_list($list_items));
    }
    elseif ($content == "USER_ASSIGNMENT"){
        $div_title = "Tasks to which ".link_user($object)." is assigned";
        $list_items = array();
        foreach ($object->assignment() as $assigned_task){
            $list_items[] = widget_task($assigned_task);
        }
        return make_content_div_html($div_title, make_list($list_items));
        
    }
    elseif ($content == "USER_TRUST"){
        $div_title = "Users trusted by ".link_user($object);
        $list_items = array();
        foreach ($object->trust() as $trusted_user){
            $list_items[] = link_user($trusted_user);
        }
        return make_content_div_html($div_title, make_list($list_items));
        
    }
    elseif ($content == "USER_TRUST_REQUESTS_MADE"){
        $div_title = "Trust requests sent by ".link_user($object);
        $list_items = array();
        foreach ($object->trust_requests_made() as $trust_request){
            $list_item = link_user($trust_request->recipient);
            $list_item .= " - ".$trust_request->timestamp;  
            $list_items[] = $list_item;
        }
        return make_content_div_html($div_title, make_list($list_items));   
    }
    
    elseif ($content == "USER_TRUST_REQUESTS_RECEIVED"){
        $div_title = "Trust requests received by ".link_user($object);
        $list_items = array();
        foreach ($object->trust_requests_received() as $trust_request){
            $list_item = link_user($trust_request->sender);
            $list_item .= " - ".$trust_request->timestamp;  
            $list_items[] = $list_item;
        }
        return make_content_div_html($div_title, make_list($list_items));   
    }
    
    elseif ($content == "USER_TRUST_REQUESTS_RECEIVED"){
        $div_title = "Trust requests received by ".link_user($object);

        $list_items = array();
        foreach ($object->trust_requests_received() as $trust_request){
            $list_items[] = link_user($trust_request->sender);
        }
        return make_content_div_html($div_title, make_list($list_items));   
    }
    
    elseif ($content == "USER_REQUEST_TRUST"){
        $div_title = "Send a trust request";

        $inputs = array();
        $inputs[] = make_input("hidden", "form", "trust_request");
        $inputs[] = make_input("textarea", "emails", null, $label=false);
        $inputs[] = make_input("submit", null, "send");
        
        $action = url("user", $object);
        $form = make_form($inputs, $action);
        
        $content = "input the email addresses, one per line";
        $content .= "<br/>";
        $content .= $form;
        return make_content_div_html($div_title, $content);
    }
    
    
    /* TASK contents */
    elseif ($content == "TASK_DESCRIPTION"){
        $div_title = "Description";
        $html = "<p>".$object->description."</p>";
        return make_content_div_html(null, $html);   
    }
    elseif ($content == "TASK_ASSIGNMENT"){
        $div_title = "Users assigned";
        $list_items = array();
        foreach ($object->assignment() as $assigned_user){
            $list_items[] = link_user($assigned_user);
        }
        return make_content_div_html(null, make_list($list_items));
        
    }
    
    elseif ($content == "TASK_DEPENDENCIES"){
        $div_title = "Dependecies";
        $list_items = array();
        foreach ($object->dependencies() as $dependecy){
            $list_items[] = link_task($dependecy);
        }
        return make_content_div_html($div_title, make_list($list_items));
    }
    
    elseif ($content == "TASK_DEPENDENTS"){
        $div_title = "Tasks that depends on this";
        $list_items = array();
        foreach ($object->dependents() as $dependent){
            $list_items[] = link_task($dependent);
        }
        return make_content_div_html($div_title, make_list($list_items));
        
    }
    elseif ($content == "TASK_MESSAGES"){
        $div_title = "Messages";
        $list_items = array();
        foreach ($object->messages() as $message){
            $list_items[] = widget_message($message);
        }
        return make_content_div_html($div_title, make_list($list_items));
    }
    elseif ($content == "TASK_EDIT"){
        $div_title = "Edit task";

        $inputs = array();
        $inputs[] = make_input("hidden", "form", "task");
        $inputs[] = make_input("hidden", "id", $object->id);
        $inputs[] = make_input("textbox", "name", $object->name, $label=false);
        $inputs[] = make_input("textarea", "description", $object->description, $label=false);
        $inputs[] = make_input("submit", null, "update");
        
        $action = url("task", $object);
        $form = make_form($inputs, $action);
        return make_content_div_html($div_title, $form);
    }
    elseif ($content == "TASK_ASSIGNMENT_EDIT"){
        $div_title = "Users assigned (edit)";
        $inputs = array();
        foreach ($visitor->trust() as $trusted_user){
            $list_item = array(
                "key" => $trusted_user->id,
                "value" => $trusted_user->username,
                "selected" => in_array($trusted_user, $object->assignment()) ? "selected" : ""
            );
            $inputs[] = make_input("checkbox", "assignment", $list_item);            
        }

        # add visitor to list
        $visitor_item = array(
            "key" => $visitor->id,
            "value" => $visitor->username,
            "selected" => in_array($visitor, $object->assignment()) ? "selected" : ""
        );
        $inputs[] = make_input("checkbox", "assignment", $visitor_item);           
        $inputs[] = make_input("hidden", "form", "assignment");
        $inputs[] = make_input("hidden", "id", $object->id);
        $inputs[] = make_input("submit", null, "update");
        $action = url("task", $object);
        $form = make_form($inputs, $action);
        return make_content_div_html($div_title, $form);
    }
    
    elseif ($content == "TASK_DEPENDENCIES_EDIT"){
        $div_title = "Dependecies (edit)";
        $inputs = array();
        foreach ($object->project->tasks() as $task){
            $list_item = array(
                "key" => $task->id,
                "value" => $task->name,
                "selected" => in_array($task, $object->dependencies()) ? "selected" : ""
            );
            $inputs[] = make_input("checkbox", "dependencies", $list_item);            
        }

        $inputs[] = make_input("hidden", "form", "dependencies");
        $inputs[] = make_input("hidden", "id", $object->id);
        $inputs[] = make_input("submit", null, "update");
        $action = url("task", $object);
        $form = make_form($inputs, $action);
        return make_content_div_html($div_title, $form);
    }
    
    elseif ($content == "TASK_DEPENDENTS_EDIT"){
        $div_title = "Tasks that depends on this (edit)";
        $inputs = array();
        foreach ($object->project->tasks() as $task){
            $list_item = array(
                "key" => $task->id,
                "value" => $task->name,
                "selected" => in_array($task, $object->dependents()) ? "selected" : ""
            );
            $inputs[] = make_input("checkbox", "dependents", $list_item);            
        }

        $inputs[] = make_input("hidden", "form", "dependents");
        $inputs[] = make_input("hidden", "id", $object->id);
        $inputs[] = make_input("submit", null, "update");
        $action = url("task", $object);
        $form = make_form($inputs, $action);
        return make_content_div_html($div_title, $form);
    }
    
    elseif ($content == "NEW_MESSAGE"){
        $div_title = "New message";

        $inputs = array();
        $inputs[] = make_input("hidden", "form", "new_message");
        $inputs[] = make_input("hidden", "task", $object->id);
        $inputs[] = make_input("hidden", "author", $visitor->id);
        $inputs[] = make_input("textarea", "text", "", $label=false);
        $inputs[] = make_input("submit", null, "send");
        
        return make_content_div_html($div_title, make_form($inputs, "index.php?view=task&task=".$object->id)); // CHANGE to something more elegant
    }
    
   
    /* PROJECT contents */
    elseif ($content == "PROJECT_DESCRIPTION"){
        $div_title = "Description";   
        $html = "<p>".$object->description."<br/>";
        $html .= "owner:".link_user($object->owner)."</p>";
        return make_content_div_html(null, $html);   
    }
    elseif ($content == "PROJECT_TASKS"){
        $div_title = "Tasks";
        $list_items = array();
        foreach ($object->tasks() as $task){
            $list_item = "";
            $list_item .= link_task($task);
            $list_item .= " (";
            $list_item .= implode(" ", array_map(@link_user, $task->assignment()));
            $list_item .= ")";
            $list_items[] = $list_item;
        }
        return make_content_div_html($div_title, make_list($list_items));
    }
    elseif ($content == "PROJECT_INVOLVEMENT"){
        #$div_title = "Users involved";

        $list_items = array();
        foreach ($object->involvement() as $involved_user){
            $list_items[] = link_user($involved_user);
        }
        return make_content_div_html(null, make_list($list_items));
    }
    elseif ($content == "EDIT_PROJECT"){
        $div_title = "Edit project";

        $inputs = array();
        $inputs[] = make_input("hidden", "form", "project");
        $inputs[] = make_input("hidden", "id", $object->id);
        $inputs[] = make_input("textbox", "name", $object->name, $label=false);
        $inputs[] = make_input("textarea", "description", $object->description, $label=false);
        $inputs[] = make_input("textbox", "start", $object->start);
        $inputs[] = make_input("submit", null, "update");

        $action = url("project", $object);
        $form = make_form($inputs, $action);
        return make_content_div_html($div_title, $form);
    }
    
    elseif ($content == "NEW_PROJECT"){
        $div_title = "New project";

        $inputs = array();
        $inputs[] = make_input("hidden", "form", "new_project");
        $inputs[] = make_input("hidden", "id", $visitor->id);
        $inputs[] = make_input("textbox", "name", "New project", $label=false);
        $inputs[] = make_input("textarea", "description", "Project description", $label=false);
        $inputs[] = make_input("submit", null, "create");
        
        $action = url(null);
        $form = make_form($inputs, $action);
        return make_content_div_html($div_title, $form);
    }

    elseif ($content == "DELETE_PROJECT"){
        $div_title = "Delete project";

        $inputs = array();
        $inputs[] = make_input("hidden", "form", "delete_project");
        $inputs[] = make_input("hidden", "id", $object->id);
        $inputs[] = make_input("submit", null, "delete this project");
        
        $action = url(null);
        $form = make_form($inputs, $action);
        return make_content_div_html($div_title, $form); // CHANGE to something more elegant
    }
    
    elseif ($content == "NEW_TASK"){
        $div_title = "New task";

        $inputs = array();
        $inputs[] = make_input("hidden", "form", "new_task");
        $inputs[] = make_input("hidden", "id", $object->id);
        $inputs[] = make_input("textbox", "name", "New task", $label=false);
        $inputs[] = make_input("textarea", "description", "Task description", $label=false);
        $inputs[] = make_input("submit", null, "create");
        
        $action = url("project", $object);
        $form = make_form($inputs, $action);        
        return make_content_div_html($div_title, $form);
    }
    
    elseif ($content == "DELETE_TASK"){
        $div_title = "Delete task";

        $inputs = array();
        $inputs[] = make_input("hidden", "form", "delete_task");
        $inputs[] = make_input("hidden", "id", $object->id);
        $inputs[] = make_input("submit", null, "delete this task");
        
        $action = url("project", $object);
        $form = make_form($inputs, $action);        
        return make_content_div_html($div_title, $form);
    }
    
    echo ($html);
}

function content_toolbar($visitor){
    $content = "<div class=\"toolbar\">";
    $content .= make_icon("trust", $visitor);
    $content .= make_icon("logout", $visitor);
    $content .= "</div>";
    return $content;
}


function content_login(){
        $div_title = "Login";

        $inputs = array();
        $inputs[] = make_input("hidden", "form", "login");
        $inputs[] = make_input("textbox", "username", null);
        $inputs[] = make_input("password", "password", null);
        $inputs[] = make_input("submit", null, "login");
        
        $action = url("dashboard");
        $form = make_form($inputs, $action);        
        return make_content_div_html($div_title, $form);
}

?>

