-- MySQL dump 10.13  Distrib 5.1.49, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: storkl
-- ------------------------------------------------------
-- Server version	5.1.49-1ubuntu8.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_message`
--

DROP TABLE IF EXISTS `auth_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_403f60f` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_message`
--

LOCK TABLES `auth_message` WRITE;
/*!40000 ALTER TABLE `auth_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add message',4,'add_message'),(11,'Can change message',4,'change_message'),(12,'Can delete message',4,'delete_message'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add log entry',8,'add_logentry'),(23,'Can change log entry',8,'change_logentry'),(24,'Can delete log entry',8,'delete_logentry'),(28,'Can add project',10,'add_project'),(29,'Can change project',10,'change_project'),(30,'Can delete project',10,'delete_project'),(31,'Can add task',11,'add_task'),(32,'Can change task',11,'change_task'),(33,'Can delete task',11,'delete_task'),(34,'Can add message',12,'add_message'),(35,'Can change message',12,'change_message'),(36,'Can delete message',12,'delete_message');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'basic','','','valeriobasile@gmail.com','sha1$7f32a$5b3e13a36d9dec68ba64dcda2c366206677b157c',1,1,1,'2011-08-25 14:16:27','2011-08-10 08:58:35'),(2,'sara','','','','sha1$349a7$f379298ae971496cb0533150fba69750a04b9bc8',0,1,0,'2011-08-25 12:45:49','2011-08-10 09:44:55');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2011-08-10 09:32:24',1,10,'1','hyperlamp',1,''),(2,'2011-08-10 09:42:08',1,11,'1','%s/%s',1,''),(3,'2011-08-10 09:43:49',1,11,'1','%s/%s',1,''),(4,'2011-08-10 09:44:55',1,3,'2','sara',1,''),(5,'2011-08-10 09:46:58',1,11,'2','hyperlamp/buy paint',1,''),(6,'2011-08-10 09:47:36',1,11,'3','hyperlamp/actually build lamp',1,''),(7,'2011-08-22 10:08:36',1,10,'2','storkl',1,''),(8,'2011-08-22 10:08:59',1,10,'3','MSSL',1,''),(9,'2011-08-23 03:52:48',1,11,'4','MSSL/making',1,''),(10,'2011-08-23 03:53:01',1,11,'5','MSSL/sweet',1,''),(11,'2011-08-23 03:53:16',1,11,'6','MSSL/love',1,''),(12,'2011-08-23 09:28:48',1,11,'1','buy wood',1,''),(13,'2011-08-23 09:29:12',1,11,'2','buy lightbulb',1,''),(14,'2011-08-23 09:29:27',1,11,'3','build lamp',1,''),(15,'2011-08-23 09:29:40',1,11,'4','enjoy',1,''),(16,'2011-08-23 10:06:23',1,11,'1','dfgdfgdf',2,'Changed users.'),(17,'2011-08-23 10:06:46',1,11,'1','buy wood',2,'Changed name, users and dependency.'),(18,'2011-08-23 10:06:54',1,11,'1','buy wood',2,'No fields changed.'),(19,'2011-08-23 10:07:10',1,11,'2','buy lightbulb',1,''),(20,'2011-08-23 10:14:15',1,10,'1','hyperlamp',1,''),(21,'2011-08-23 10:14:31',1,10,'2','MSSL',1,''),(22,'2011-08-23 10:14:54',1,11,'1','buy wood',1,''),(23,'2011-08-23 10:15:07',1,11,'2','buy lightbulb',1,''),(24,'2011-08-23 10:15:24',1,11,'3','build lamp',1,''),(25,'2011-08-23 10:15:39',1,11,'4','making',1,''),(26,'2011-08-23 10:15:50',1,11,'5','sweet',1,''),(27,'2011-08-23 10:16:05',1,11,'6','love',1,''),(28,'2011-08-23 10:16:15',1,11,'6','love',2,'Changed dependency.'),(29,'2011-08-23 10:16:27',1,11,'5','sweet',2,'Changed dependency.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'message','auth','message'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'site','sites','site'),(8,'log entry','admin','logentry'),(10,'project','storklapp','project'),(11,'task','storklapp','task'),(12,'message','storklapp','message');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('28e2fd3c47995562b6cc5df87f0d5421','ODg0Mjg0ZGY4NGM1NmNlZDdjMjM5MzM2YTIyNGU1NzRiNjRlZmM5NTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2011-08-24 09:26:04'),('827f52e19a9fa400f5598e8f02aae331','ODg0Mjg0ZGY4NGM1NmNlZDdjMjM5MzM2YTIyNGU1NzRiNjRlZmM5NTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2011-09-06 06:12:47'),('d31c7a9265a7bd43275dc0c70eea36aa','ODg0Mjg0ZGY4NGM1NmNlZDdjMjM5MzM2YTIyNGU1NzRiNjRlZmM5NTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2011-09-06 04:03:43'),('f6b5c9f746a3b3bfd60da3d9bf296af7','ODg0Mjg0ZGY4NGM1NmNlZDdjMjM5MzM2YTIyNGU1NzRiNjRlZmM5NTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2011-09-08 14:16:27'),('9b2103c3351bf21cc214d141d221af88','ODg0Mjg0ZGY4NGM1NmNlZDdjMjM5MzM2YTIyNGU1NzRiNjRlZmM5NTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2011-09-06 09:01:55'),('75b2392e7f779bb0cfafb54050b91b39','ODg0Mjg0ZGY4NGM1NmNlZDdjMjM5MzM2YTIyNGU1NzRiNjRlZmM5NTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2011-09-07 08:22:13');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storklapp_message`
--

DROP TABLE IF EXISTS `storklapp_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storklapp_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `timestamp` datetime NOT NULL,
  `author_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `storklapp_message_337b96ff` (`author_id`),
  KEY `storklapp_message_499df97c` (`project_id`),
  KEY `storklapp_message_3ff01bab` (`task_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storklapp_message`
--

LOCK TABLES `storklapp_message` WRITE;
/*!40000 ALTER TABLE `storklapp_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `storklapp_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storklapp_project`
--

DROP TABLE IF EXISTS `storklapp_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storklapp_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `storklapp_project_5d52dd10` (`owner_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storklapp_project`
--

LOCK TABLES `storklapp_project` WRITE;
/*!40000 ALTER TABLE `storklapp_project` DISABLE KEYS */;
INSERT INTO `storklapp_project` VALUES (1,'hyperlamp','Una lampada a forma di ipercubo.',1),(2,'MSSL','... ;-)',2),(3,'paella','serata paella con gli amici.',1);
/*!40000 ALTER TABLE `storklapp_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storklapp_task`
--

DROP TABLE IF EXISTS `storklapp_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storklapp_task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `project_id` int(11) NOT NULL,
  `deadline` datetime DEFAULT NULL,
  `completed` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `storklapp_task_b6620684` (`project_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storklapp_task`
--

LOCK TABLES `storklapp_task` WRITE;
/*!40000 ALTER TABLE `storklapp_task` DISABLE KEYS */;
INSERT INTO `storklapp_task` VALUES (1,'buy wood','',1,NULL,0),(2,'buy lightbulb','bl',1,NULL,0),(3,'build lamp','BL',1,'2011-08-27 00:00:00',1),(4,'making','m',2,NULL,0),(5,'sweet','S',2,NULL,0),(6,'love','<3',2,NULL,0),(7,'enjoy','',1,NULL,0),(8,'???','',1,NULL,0),(9,'profit','',1,NULL,0),(10,'fare la spesa','andare da AH e Jumbo e Vismarkt e comprare gli ingredienti',3,'2011-09-02 00:00:00',0),(11,'comprare il pesce','comprare il pesce in Vismarkt',3,'2011-08-30 00:00:00',0),(12,'pulire casa','',3,NULL,0),(13,'cucinare','cucinare la paella',3,'2011-09-02 00:00:00',0),(14,'cena','',3,NULL,0);
/*!40000 ALTER TABLE `storklapp_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storklapp_task_dependencies`
--

DROP TABLE IF EXISTS `storklapp_task_dependencies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storklapp_task_dependencies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_task_id` int(11) NOT NULL,
  `to_task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `from_task_id` (`from_task_id`,`to_task_id`),
  KEY `storklapp_task_dependency_b423b2f3` (`from_task_id`),
  KEY `storklapp_task_dependency_bf911e82` (`to_task_id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storklapp_task_dependencies`
--

LOCK TABLES `storklapp_task_dependencies` WRITE;
/*!40000 ALTER TABLE `storklapp_task_dependencies` DISABLE KEYS */;
INSERT INTO `storklapp_task_dependencies` VALUES (8,3,1),(9,3,2),(7,7,3),(10,5,4),(11,6,5),(12,9,8),(30,13,12),(19,14,12),(20,14,13),(29,13,11),(28,13,10);
/*!40000 ALTER TABLE `storklapp_task_dependencies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storklapp_task_users`
--

DROP TABLE IF EXISTS `storklapp_task_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storklapp_task_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`,`user_id`),
  KEY `storklapp_task_users_c00fe455` (`task_id`),
  KEY `storklapp_task_users_fbfc09f1` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storklapp_task_users`
--

LOCK TABLES `storklapp_task_users` WRITE;
/*!40000 ALTER TABLE `storklapp_task_users` DISABLE KEYS */;
INSERT INTO `storklapp_task_users` VALUES (18,1,1),(2,2,2),(3,3,1),(4,3,2),(5,4,1),(6,4,2),(14,5,2),(13,5,1),(12,6,2),(11,6,1),(15,7,2),(16,7,1),(20,10,1),(21,11,2),(22,12,1),(23,12,2),(24,14,1),(25,14,2);
/*!40000 ALTER TABLE `storklapp_task_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-08-26 10:08:06
