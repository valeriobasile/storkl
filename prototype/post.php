<?php
// post.php
/* process POST parameters, if any
 */

if (count($_POST)>0){
    $form = $_POST["form"];
    if ($form == "project"){
        $id = $_POST["id"];
        $project = new Project($id);
        $project->name = $_POST["name"];
        $project->description = $_POST["description"];
        $project->save();
    }
    elseif ($form == "task"){
        $id = $_POST["id"];
        $task = new Task($id);
        $task->name = $_POST["name"];
        $task->description = $_POST["description"];
        $task->save();
    }
    elseif ($form == "assignment"){
        $id = $_POST["id"];
        $task = new Task($id);
        $task->remove_assignment();
        
        if (isset($_POST["assignment"])){
            foreach($_POST["assignment"] as $assignment){
                $user = new User($assignment);
                $task->assign($user);
            }
        }
    }
    elseif ($form == "dependencies"){
        $id = $_POST["id"];
        $task = new Task($id);
        $task->remove_dependencies();
        
        if (isset($_POST["dependencies"])){
            foreach($_POST["dependencies"] as $dependency_id){
                $dependency = new Task($dependency_id);
                $task->add_dependency($dependency);
            }
        }
    }
    elseif ($form == "dependents"){
        $id = $_POST["id"];
        $task = new Task($id);
        $task->remove_dependents();
        
        if (isset($_POST["dependents"])){
            foreach($_POST["dependents"] as $dependent_id){
                $dependent = new Task($dependent_id);
                $task->add_dependent($dependent);
            }
        }
    }
    elseif ($form == "new_task"){
        $id = $_POST["id"];
        $task = new Task(null, $id, $_POST["name"], $_POST["description"]);
    }
    
    elseif ($form == "new_project"){
        $id = $_POST["id"];
        $project = new Project(null, $visitor->id, $_POST["name"], $_POST["description"]);
    }
    
    elseif ($form == "delete_task"){
        $id = $_POST["id"];
        $task = new Task($id);
        $task->delete();
    }
    
    elseif ($form == "delete_project"){
        $id = $_POST["id"];
        $project = new Project($id);
        $project->delete();
    }
    
    elseif ($form == "new_message"){
        $id = $_POST["id"];
        $message = new Message(null, $_POST["task"], $visitor->id, $_POST["text"]);
    }

    elseif ($form == "trust_request"){
        $emails = $_POST["emails"];
        $emails_array = explode("\n", $emails);
        foreach ($emails_array as $_email) {
            $recipient = User::load($id = null, $username = null, $email = $_email);
            if ($recipient) {
                // found a user already in the system with the same email
                $trust_request = new TrustRequest($visitor->id, $recipient->id);            
            }
            else {
                // send an invite email
                // TODO
                echo ("send an email to $_email");
                ;
            }
        }
    }
    elseif ($form == "login"){
        // here be login
        ;
    }
    

}
?>
