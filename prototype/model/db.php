<?php
// db.php

# connessione al database
$host = "localhost";   
$user = "root";
$pass = "darkaelf";
$dbname = "storkl";

$connection = mysql_connect($host,$user,$pass) or die (mysql_error());
mysql_select_db($dbname,$connection) or die (mysql_error());
mysql_query("SET CHARACTER SET utf8");

function db_get_single_row($table, $id){
    $sql = "select * from $table where id = $id;";
    $result = mysql_query($sql) or die (mysql_error());
    if (mysql_num_rows($result) > 0) {
        return mysql_fetch_assoc($result); 
    }
}

function db_get_single_row_by_string($table, $field, $value){
    $sql = "select * from $table where $field = '$value';";
    $result = mysql_query($sql) or die (mysql_error());
    if (mysql_num_rows($result) > 0) {
        return mysql_fetch_assoc($result); 
    }
}

function db_get_manytomany($table, $id1, $id2){
    $result = mysql_query("select * from $table;");
    $field1 = mysql_field_name($result, 0);
    $field2 = mysql_field_name($result, 1);
    
    if (!is_null($id1) and !is_null($id2)){
        $sql = "select * from $table where $field1 = $id1 and $field2 = $id2;";
    }
    elseif (is_null($id1) and !is_null($id2)){
        $sql = "select * from $table where $field2 = $id2 ;";
    }
    elseif (!is_null($id1) and is_null($id2)){
        $sql = "select * from $table where $field1 = $id1;";    
    }
    else {
        return null;
    }
    $result = mysql_query($sql) or die (mysql_error());
    $resultset = array();
    while ($row = mysql_fetch_assoc($result)){
        $resultset[] = $row;
    }
    return $resultset;
}

function  db_get_many($table, $fk, $id){
    $sql = "select * from $table where $fk = $id;";
    $result = mysql_query($sql) or die (mysql_error());
    $resultset = array();
    while ($row = mysql_fetch_assoc($result)){
        $resultset[] = $row;
    }
    return $resultset;

}

function db_update($table, $id, $updates){
    foreach($updates as $update){
        if ($update["type"] == "string"){
            $sql = "update $table set ".$update["field"]." = '".$update["value"]."' where id = ".$id.";";
        }
        elseif ($update["type"] == "integer"){
            $sql = "update $table set ".$update["field"]." = ".$update["value"]." where id = ".$id.";";
        }
        elseif ($update["type"] == "boolean"){
            $sql = "update $table set ".$update["field"]." = '".($update["value"] ? "true" : "false")."' where id = ".$id.";";
        }
        elseif ($update["type"] == "date"){
            $sql = "update $table set ".$update["field"]." = '".date( 'Y-m-d', $update["value"])."' where id = ".$id.";";
        }
        $result = mysql_query($sql) or die (mysql_error());
    }
}

function db_delete($table, $id){
    $sql = "delete from $table where id = ".$id.";";
    mysql_query($sql) or die (mysql_error());
}

function db_insert($table, $id, $values){
    $field_names = array();
    $field_values = array();
    foreach($values as $value){
        $field_names[] = $value["field"];
        if ($value["type"] == "string"){
            $field_values[] = "'".$value["value"]."'";
        }
        elseif ($value["type"] == "integer"){
            $field_values[] = $value["value"];
        }
        elseif ($value["type"] == "boolean"){
            $field_values[] = $value["value"] ? "true" : "false";
        }
        elseif ($value["type"] == "date"){
            $sql = "update $table set ".$value["field"]." = '".date( 'Y-m-d', $value["value"])."' where id = ".$id.";";
        }
    }
    $sql = "insert into $table (".implode(", ", $field_names).") values (".implode(", ", $field_values).");";
    #echo ($sql);
    $result = mysql_query($sql) or die (mysql_error());
}

function db_delete_manytomany($table, $id1, $id2){
    $result = mysql_query("select * from $table;");
    $field1 = mysql_field_name($result, 0);
    $field2 = mysql_field_name($result, 1);
    if (!is_null($id1) and !is_null($id2)){
        $sql = "delete from $table where $field1 = $id1 and $field2 = $id2;";
    }
    elseif (is_null($id1) and !is_null($id2)){
        $sql = "delete from $table where $field2 = $id2 ;";
    }
    elseif (!is_null($id1) and is_null($id2)){
        $sql = "delete from $table where $field1 = $id1;";    
    }
    else {
        return null;
    }
    
    $result = mysql_query($sql) or die (mysql_error());
}

function db_add_manytomany($table, $id1, $id2){
    $result = mysql_query("select * from $table;");
    $field1 = mysql_field_name($result, 0);
    $field2 = mysql_field_name($result, 1);
    $sql = "insert into $table ($field1, $field2) values ($id1, $id2);";
    $result = mysql_query($sql) or die (mysql_error());
}

function db_next_id($table){
    $sql = "select next from information_schema.tables where table_name = '$table';";
    $result = mysql_query($sql);
    return $result["next"];
}
?>
