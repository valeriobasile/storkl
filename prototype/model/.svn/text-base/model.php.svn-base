<?php
// model.php
require_once("db.php");
require_once("user.php");
require_once("task.php");
require_once("project.php");


/* Message class models a message posted by a user to a task
 */
class Message{
    function __construct($_id, $_task = null, $_author = null, $_text = null) {
        if (is_null($_id)){
            $this->id = db_next_id("message");
            $this->task = new Task($_task);
            $this->author = new User($_author);
            $this->text = $_text;
            $this->create();
        }
        else {
            $this->id = $_id;
            $message_record = db_get_single_row("message", $this->id);
            $this->task = new Task($message_record['task']);
            $this->author = new User($message_record['author']);
            $this->timestamp = $message_record['timestamp'];
            $this->text = $message_record['text'];
        }
    }

    function create(){
        $updates = array();
        $updates[] = array("field" => "task", "value" => $this->task->id, "type" => "integer");
        $updates[] = array("field" => "author", "value" => $this->author->id, "type" => "integer");
        $updates[] = array("field" => "text", "value" => $this->text, "type" => "string");
        db_insert("message", $this->id, $updates);
    }
}

/* TrustRequest class models a request of enter in trust relation from an 
 * user to another
 */
class TrustRequest{
    function __construct($_sender_id, $_recipient_id){
        $this->sender = new User($_sender_id);
        $this->recipient = new User($_recipient_id);
        $trust_request_recordset = db_get_manytomany("trust_request", $_sender_id, $_recipient_id);
        if (count($trust_request_recordset) > 0){
            // return existing relation
            $this->timestamp = $trust_request_recordset[0]["timestamp"];
            $this->pending = $trust_request_recordset[0]["pending"];
        }
        else {
            // create new trust request
            $this->timestamp = null;
            $this->pending = true;
            $this->create();
        }
    }
    
    function create(){
        $updates = array();
        $updates[] = array("field" => "sender", "value" => $this->sender->id, "type" => "integer");
        $updates[] = array("field" => "recipient", "value" => $this->recipient->id, "type" => "integer");
        $updates[] = array("field" => "pending", "value" => $this->pending, "type" => "boolean");
        db_insert("trust_request", null, $updates);
    }    
}

?>

