<?php
// project.php

/* Project class models StorkL projects as collections of tasks dependent
 * on each other 
 */
class Project{
    function __construct($_id, $_owner = null, $_name = null, $_description = null) {
        if (is_null($_id)){
            $this->id = db_next_id("project");
            $this->owner = new User($_owner);
            $this->name = $_name;
            $this->description = $_description;
            $this->create();
        }
        else {
            $this->id = $_id;
            $project_record = db_get_single_row("project", $this->id);
            $this->name = $project_record['name'];
            $this->description = $project_record['description'];
            $this->start = $project_record['start'];
            $this->owner = new User($project_record['owner']);
        }
   }
   
   /* returns an array of Task objects which are part of the project 
    */
   function tasks(){
        $tasks = array();
        $tasks_recordset = db_get_many("task", "project", $this->id);
        foreach($tasks_recordset as $task_row){
            $tasks[] = new Task($task_row["id"]);
        }
        return $tasks;
   }
   
    /* return an array of User objects made of:
     * - users that are assigned to a task of the projects
     * - the project owner
     * duplicates are removed
     */
    function involvement(){
        $involvement = array();

        // get users from tasks which are part of the project
        $tasks = array();
        $tasks_recordset = db_get_many("task", "project", $this->id);
        foreach ($tasks_recordset as $task_record){
            $task = new Task($task_record["id"]);
            foreach($task->assignment() as $assigned_user){
                if (!in_array($assigned_user, $involvement)){
                    $involvement[] = $assigned_user;
                }
            }
        }
        
        // get owner user
        if (!in_array($this->owner, $involvement)){
            $involvement[] = $this->owner;
        }
        
        return $involvement;
    }

    function create(){
        $updates = array();
        $updates[] = array("field" => "owner", "value" => $this->owner->id, "type" => "integer");
        $updates[] = array("field" => "name", "value" => $this->name, "type" => "string");
        $updates[] = array("field" => "description", "value" => $this->description, "type" => "string");
        db_insert("project", $this->id, $updates);
    }
    
    function delete(){
        db_delete("project", $this->id);
    }
    
    function save(){
        $updates = array();
        $updates[] = array("field" => "name", "value" => $this->name);
        $updates[] = array("field" => "description", "value" => $this->description);
        db_update("project", $this->id, $updates);
    }
}

?>
