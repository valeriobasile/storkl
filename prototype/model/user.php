<?
// user

/* User class models a Storkl user. Users in Storkl are all the same,
 * though they have different roles in different projects
 * such as owner/involved/not involved. User roles are not explicits in the
 * User class; rather, they are inferred from Task and Project objects
 */
class NotFoundException extends Exception {}

class User{
    /* static factory: return null if try to create a User object from a field
     * which is not found in the DB
     */
    public static function load($_id, $_username = null, $_email = null) {
        try {
            return new User($_id, $_username, $_email);
        } catch (NotFoundException $unfe) {
            return null;
        }
    }

    function __construct($_id, $_username = null, $_email = null) {
        if (is_null($_id)){
            if (!is_null($_username)){
                // get user by username
                $this->username = $_username;
                $user_record = db_get_single_row_by_string("user", "username", $this->username);
                $this->id = $user_record['id'];
                $this->email = $user_record['email'];
            }
            elseif (!is_null($_email)){
                // get user by email
                $this->email = $_email;
                $user_record = db_get_single_row_by_string("user", "email", $this->email);
                if ($user_record){
                    $this->id = $user_record['id'];
                    $this->username = $user_record['username'];
                }
                else {
                    throw new NotFoundException();
                }
            }
            else {
                // create new user   
                $this->id = db_next_id("user");
                $this->username = $_username;
                $this->email = $_email;
                $this->create();
            }
        }
        else {
            $this->id = $_id;
            $user_record = db_get_single_row("user", $this->id);
            $this->username = $user_record['username'];
            $this->email = $user_record['email'];
        }
    }

    function create(){
        $updates = array();
        $updates[] = array("field" => "username", "value" => $this->username, "type" => "string");
        $updates[] = array("field" => "email", "value" => $this->email, "type" => "string");
        db_insert("user", $this->id, $updates);
    }

    /* returns an array of Task objects which are the tasks the user is
     * is assigned to, from every project
     */
    function assignment(){
        $assignment = array();
        $assignment_recordset = db_get_manytomany("assignment", $this->id, null);
        foreach ($assignment_recordset as $assignment_record){
            $assignment[] = new Task($assignment_record["task"]);
        }
        return $assignment;
    }

    /* returns an array of Project containing:
     * - projects containing tasks assigned to the user
     * - projects owned by the user
     */
    function involvement(){
        $involvement = array();
        
        // get projects from assigned tasks
        foreach ($this->assignment() as $assigned_task){
            if (!in_array($assigned_task->project, $involvement)){
                    $involvement[] = $assigned_task->project;
            }
        }
        
        // get owned projects
        $projects_recordset = db_get_many("project", "owner", $this->id);
        foreach ($projects_recordset as $owned_project_row){
            $owned_project = new Project($owned_project_row["id"]);
            if (!in_array($owned_project, $involvement)){
                    $involvement[] = $owned_project;
            }
        }
        return $involvement;
    }
    
    function trust_requests_made(){
        $trust_requests = array();
        $trust_requests_recordset = db_get_many("trust_request", "sender", $this->id);
        foreach ($trust_requests_recordset as $trust_requests_record){
            
            $trust_requests[] = new TrustRequest($trust_requests_record["sender"], $trust_requests_record["recipient"]);
        }
        
        return $trust_requests;
    }
    
    function trust_requests_received(){
        $trust_requests = array();
        $trust_requests_recordset = db_get_many("trust_request", $this->id, "recipient");
        foreach ($trust_requests_recordset as $trust_requests_record){
            $trust_requests[] = new TrustRequest($trust_requests_record["sender"], $trust_requests_record["recipient"]);
        }
        return $trust_requests;
    }
    
    
    
    /* returns an array of User objects which are the users in
     * a trusted relation with the current user.
     * Trust is a symmetrical relation
     */
    function trust(){
        $trust = array();
        $trust_recordset = db_get_manytomany("trust", $this->id, null);
        foreach ($trust_recordset as $trusted_user_row){
            $trust[] = new User($trusted_user_row["user2"]);
        }
        $trust_recordset = db_get_manytomany("trust", null, $this->id);
        foreach ($trust_recordset as $trusted_user_row){
            $trust[] = new User($trusted_user_row["user1"]);
        }
        return $trust;
    }

}

?>
