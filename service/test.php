<?php
# script to test the webservice

session_start();

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

$action = isset($_POST["action"]) ? $_POST["action"] : null;
switch ($action){
    case "registration":
        $url = $BASEURL."register";
        $args = array(
            "username"=>$_POST["username"],
            "password"=>$_POST["password"],
            "email"=>$_POST["email"],
        );
        $response = json_decode(api_call($url, $args));
        break;
    case "activation":
        $url = $BASEURL."activate";
        $args = array(
            "activation"=>$_POST["activation"],
        );
        $response = json_decode(api_call($url, $args));
        break;
    case "authentication":
        $url = $BASEURL."auth";
        $args = array(
            "username"=>$_POST["username"],
            "password"=>$_POST["password"],
        );
        $response = json_decode(api_call($url, $args));
        if ($response->success){
            $_SESSION["session_token"] = $response->response->session;
        }
        break;
    case "new_project":
        $url = $BASEURL."projects/new";
        $args = array(
            "name"=>$_POST["name"],
            "description"=>$_POST["description"],
            "session_token"=>$_SESSION["session_token"],
        );
        $response = json_decode(api_call($url, $args));
        break;
    default:
        $response = null;
        break;        
}
# test template
# $url = $BASEURL."";
# $args = array();
# echo(api_call($url, $args));

?>
<html>
<head>
</head>
<body>

<?
#if (!is_null($response)){
    if ($response->success==1){
        echo("<div style='background-color:#efe;'><pre>");
        print_r($response->response); 
        echo("</pre></div>");
    }
    else {
        echo("<div style='background-color:#fee; whitespace:pre;'><pre>");
        print_r($response->errors); 
        echo("</pre></div>");
    }
#}
?>
<!--registration form -->
<h1>registration</h1>
<form action="test.php" method="post">
<input name="action" type="hidden" value="registration"/>
username<br/>
<input name="username" type="text" /><br/>
password<br/>
<input name="password" type="password" /><br/>
email<br/>
<input name="email" type="text" /><br/>
<input type="submit" />
</form>

<!--activation form -->
<h1>activation</h1>
<form action="test.php" method="post">
<input name="action" type="hidden" value="activation"/>
activation<br/>
<input name="activation" type="activation" /><br/>
<input type="submit" />
</form>

<!--authentication form -->
<h1>authentication</h1>
<form action="test.php" method="post">
<input name="action" type="hidden" value="authentication"/>
username<br/>
<input name="username" type="text" /><br/>
password<br/>
<input name="password" type="password" /><br/>
<input type="submit" />
</form>

<!--new project form -->
<h1>new project</h1>
<form action="test.php" method="post">
<input name="action" type="hidden" value="new_project"/>
name<br/>
<input name="name" type="text" /><br/>
<textarea name="description" />description</textarea><br/>
<input type="submit" />
</form>

</body>
</html>
