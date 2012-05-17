<?php
// task.php

global $config;

/* Task class models the StorkL tasks that make a project. Tasks in StorkL
 * are connected to each other via the non-symmetric relation of Dependency,
 * forming a directed graph
 */
class Task{
    function __construct($_id, $_project = null, $_name = null, $_description = null, $_deadline = null) {
        if (is_null($_id)){
            $this->id = db_next_id("task");
            $this->project = new Project($_project);
            $this->name = $_name;
            $this->description = $_description;
            $this->deadline = $_deadline;
            $this->create();
        }
        else {
            $this->id = $_id;
            $task_record = db_get_single_row("task", $this->id);
            $this->project = new Project($task_record['project']);
            $this->name = $task_record['name'];
            $this->description = $task_record['description'];
            $this->deadline = $task_record['deadline'];
        }
    }

    /* returns an array of User objects containing users assigned to the task
     */
    function assignment(){
        $assignment = array();
        $assignment_recordset = db_get_manytomany("assignment", null, $this->id);
        foreach ($assignment_recordset as $assignment_record){
            $assignment[] = new User($assignment_record["user"]);
        }
        return $assignment;
    }

    function remove_assignment(){
        db_delete_manytomany("assignment", null, $this->id);
    }

    function assign($user){
        $assignment = array();
        db_add_manytomany("assignment", $user->id, $this->id);
    }

    /* returns an array of Task objects that are the tasks on which the current
     * task is depending upon
     */
    function dependencies(){
        $dependecies = array();
        $dependency_recordset = db_get_manytomany("dependency", null, $this->id);
        foreach ($dependency_recordset as $dependecies_record){
            $dependecies[] = new Task($dependecies_record["head"]);
        }
        return $dependecies;
    }

    /* returns an array of Task objects that are dependent on the current task
     */
    function dependents(){
        $dependents = array();
        $dependency_recordset = db_get_manytomany("dependency", $this->id, null);
        foreach ($dependency_recordset as $dependants_record){
            $dependents[] = new Task($dependants_record["dependent"]);
        }
        return $dependents;
    }

    /* returns an array of Message objects that are the messages posted
     * in the task page
     */
    function messages(){
        $messages = array();
        $message_recordset = db_get_many("message", "task", $this->id);
        foreach ($message_recordset as $message_record){
            $messages[] = new Message($message_record["id"]);
        }
        return $messages;
    }
    
    function create(){
        $updates = array();
        $updates[] = array("field" => "project", "value" => $this->project->id, "type" => "integer");
        $updates[] = array("field" => "name", "value" => $this->name, "type" => "string");
        $updates[] = array("field" => "description", "value" => $this->description, "type" => "string");
        $updates[] = array("field" => "date", "value" => $this->date, "type" => "date");
        db_insert("task", $this->id, $updates);
    }

    function delete(){
        db_delete("task", $this->id);
    }

    function save(){
        $updates = array();
        $updates[] = array("field" => "name", "value" => $this->name, "type" => "string");
        $updates[] = array("field" => "description", "value" => $this->description, "type" => "string");
        $updates[] = array("field" => "date", "value" => $this->date, "type" => "date");
        db_update("task", $this->id, $updates);
    }

    function remove_dependencies(){
        db_delete_manytomany("dependency", null, $this->id);
    }
    
    function add_dependency($dependency){
        db_add_manytomany("dependency", $dependency->id, $this->id);
    }
    
    function remove_dependents(){
        db_delete_manytomany("dependency", $this->id, null);    
    }
    
    function add_dependent($dependent){
        db_add_manytomany("dependency", $this->id, $dependent->id);
    }    
    
    /* returns a constant defining the current status of the task
     * concerning its deadline and assignment
     */
    function status($visitor) {
        global $visitor;
        
        $delta = mktime() - strtotime($this->deadline);
        $days = floor($delta / 3600);
        
        if (!in_array($visitor, $this->assignment())){
            return "unassigned";
        }
        elseif ($days > DEADLINE_APPROACHING){
            return "active";
        }
        elseif ($days > DEADLINE_URGENT){
            return "approaching";
        }
        elseif ($days >= 0){
            return "urgent";
        }
        elseif ($days < 0){
            return "overdue";
        }
    }
}

?>
