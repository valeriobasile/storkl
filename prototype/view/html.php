<?php
// html.php

function make_content_div_html($title, $content){
    $html = "<div class = \"content\">";
    
    if ($title) {
        $html .= "<h2>$title</h2>";
    }
    $html .= "$content</div>";
    return $html;
}

function make_list($items){
    $html = "<ul>";
    foreach ($items as $item){
        $html .= "<li>$item</li>";
    }
    $html .= "</ul>";
    return $html;    
}

function make_form($inputs, $action){
    $html = "<form method=\"post\" action=\"".$action."\">";
    $html .= "<ul>";
    
    foreach ($inputs as $input){
        $html .= "<li>".$input."</li>";
    }
    $html .= "</ul>";
    $html .= "</form>";
    return $html;    
}

function make_input($type, $name, $value, $label=true){
    $html = "";
    if ($type == "textbox"){
        if ($label){
            $html .= "<label for=\"$name\">$name</label>";
        }
        $html .= "<input type=\"text\" name=\"$name\" id=\"$name\" value=\"$value\" />";
    }
    elseif ($type == "password"){
        if ($label){
            $html .= "<label for=\"$name\">$name</label>";
        }
        $html .= "<input type=\"password\" name=\"$name\" id=\"$name\" value=\"$value\" />";
    }
    elseif ($type == "textarea"){
        if ($label){
            $html .= "<label for=\"$name\">$name</label>";
        }
        $html .= "<textarea name=\"$name\" id=\"$name\">$value</textarea>";
    }
    elseif ($type == "hidden"){
        $html .= "<input type=\"hidden\" name=\"$name\" value=\"$value\" />";
    }
    elseif ($type == "submit"){
        $html .= "<input type=\"submit\" value=\"$value\" />";
    }
    elseif ($type == "checkbox"){
        $html .= "<input name=\"".$name."[]\" id=\"".$name."_".$value["key"]."\" type=\"checkbox\" value=\"".$value["key"]."\"";
        if ($value["selected"] == "selected"){
            $html .= " checked=\"checked\" ";
        }
        $html .= "><label for=\"".$name."_".$value["key"]."\">".$value["value"]."</label></input>";
    }

    return $html;
}

function make_icon($icon, $visitor){
    $html = "";
    if ($icon == "trust") {
        $html .= "<a href=\"".url("user", $visitor)."\"/>";
        $html .= "<img class=\"icon\" id=\"$icon\" src=\"".ICONS_DIR.$icon.".png\"/>";
        $html .= "[".count($visitor->trust_requests_received())."]";
        $html .= "</a>";
    }
    if ($icon == "logout") {
        $html .= "<a href=\"".url("logout")."\"/>";
        $html .= "<img class=\"icon\" id=\"$icon\" src=\"".ICONS_DIR.$icon.".png\"/>";
        $html .= "</a>";
    }
    return $html;    
}

?>
