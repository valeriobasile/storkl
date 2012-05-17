<?php
// for debug purpose
require_once("model/db.php");

mysql_query("truncate table trust_request;") or die (mysql_error());
mysql_query("truncate table trust;") or die (mysql_error());
mysql_query("truncate table message;") or die (mysql_error());
mysql_query("truncate table assignment;") or die (mysql_error());
mysql_query("truncate table dependency;") or die (mysql_error());
mysql_query("truncate table task;") or die (mysql_error());
mysql_query("truncate table project;") or die (mysql_error());
mysql_query("truncate table user;") or die (mysql_error());

mysql_query("insert into user(id, username, email) values (1, 'valerio', 'valeriobasile@gmail.com');") or die (mysql_error());
mysql_query("insert into user(id, username, email) values (2, 'sara', 'sarabarcena@gmail.com');") or die (mysql_error());
mysql_query("insert into user(id, username, email) values (3, 'biascica', 'ao_totti@roma.it');") or die (mysql_error());

mysql_query("insert into project(id, owner, name, description) values (1, 1, 'hyperlamp', 'Building a tessaract-shaped living room lamp.');") or die (mysql_error());
mysql_query("insert into project(id, owner, name, description) values (2, 2, 'styling StorkL', 'write a super awesome badass CSS for this awesome project');") or die (mysql_error());

mysql_query("insert into task(id, project, name, description, deadline) values (1, 1, 'buy materials', 'go to Gamma and buy stuff', null);") or die (mysql_error());
mysql_query("insert into task(id, project, name, description, deadline) values (2, 1, 'assemble', 'put the pieces together', '".date('Y-m-d', 1336852962)."');") or die (mysql_error());
mysql_query("insert into task(id, project, name, description, deadline) values (3, 1, 'buy paint', 'go to Gamma and buy a crapload of paint', '".date('Y-m-d', 1337144962)."');") or die (mysql_error());
mysql_query("insert into task(id, project, name, description, deadline) values (4, 1, 'paint the lamp', 'put some color on that thing', '".date( 'Y-m-d', 1337345162)."');") or die (mysql_error());
mysql_query("insert into task(id, project, name, description, deadline) values (5, 1, 'hang the lamp', 'find a spot on the ceiling and drill a hole', '".date( 'Y-m-d', 1337853962)."');") or die (mysql_error());
mysql_query("insert into task(id, project, name, description, deadline) values (6, 2, 'produce static files', 'extract some relevant HTML static pages from the generated php, possibly with anice identation', '".date('Y-m-d', mktime())."');") or die (mysql_error());
mysql_query("insert into task(id, project, name, description, deadline) values (7, 2, 'write CSS', 'fiddle with the W3C standards untils something nice comes out', '".date( 'Y-m-d', 1336843962)."');") or die (mysql_error());

mysql_query("insert into dependency(head, dependent) values (1,2);") or die (mysql_error());
mysql_query("insert into dependency(head, dependent) values (3,4);") or die (mysql_error());
mysql_query("insert into dependency(head, dependent) values (2,5);") or die (mysql_error());
mysql_query("insert into dependency(head, dependent) values (4,5);") or die (mysql_error());
mysql_query("insert into dependency(head, dependent) values (6,7);") or die (mysql_error());

mysql_query("insert into assignment(user, task) values (1,1);") or die (mysql_error());
mysql_query("insert into assignment(user, task) values (1,2);") or die (mysql_error());
mysql_query("insert into assignment(user, task) values (2,2);") or die (mysql_error());
mysql_query("insert into assignment(user, task) values (1,3);") or die (mysql_error());
mysql_query("insert into assignment(user, task) values (1,4);") or die (mysql_error());
mysql_query("insert into assignment(user, task) values (1,5);") or die (mysql_error());
mysql_query("insert into assignment(user, task) values (2,5);") or die (mysql_error());
mysql_query("insert into assignment(user, task) values (1,6);") or die (mysql_error());
mysql_query("insert into assignment(user, task) values (2,7);") or die (mysql_error());

mysql_query("insert into message(task, author, text) values (1,1, '@sara are you going to Gamma?');") or die (mysql_error());
mysql_query("insert into message(task, author, text) values (1,2, '@valerio yes, wanna come with me?');") or die (mysql_error());
mysql_query("insert into message(task, author, text) values (2,1, 'I don\'t know what I\'m doing');") or die (mysql_error());
mysql_query("insert into message(task, author, text) values (4,2, 'I\'m going to paint it black');") or die (mysql_error());
mysql_query("insert into message(task, author, text) values (4,1, 'Oh yeah baby');") or die (mysql_error());

mysql_query("insert into trust(user1, user2) values (1,2);") or die (mysql_error());
mysql_query("insert into trust(user1, user2) values (1,3);") or die (mysql_error());

mysql_query("insert into trust_request(sender, recipient, pending) values (3,2,1);") or die (mysql_error());

header("location: index.php");
?>
