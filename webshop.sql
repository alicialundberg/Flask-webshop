-- MySQL dump 10.13  Distrib 5.5.52, for debian-linux-gnu (armv7l)
--
-- Host: localhost    Database: webshop
-- ------------------------------------------------------
-- Server version	5.5.52-0+deb8u1

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
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` char(30) NOT NULL,
  `lastname` varchar(40) NOT NULL,
  `ssn` varchar(15) NOT NULL,
  `adress` varchar(50) NOT NULL,
  `city` char(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `password` varchar(20) NOT NULL,
  `admin` tinyint(1) NOT NULL,
  `cart` text NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (1,'Sven','Andersson','19571017-7425','testbacken 2','testeborg','sven.tester@helloworld.com','070 0001324','kalops',0,'[]'),(2,'Anna','Svensson','19850427-7425','testgatan 7','testköping','annatest@helloworld.com','070 4572157','uggla',1,''),(3,'Kristian','Testström','19120427-7136','testvägen 33','testeå','Krilletest@helloworld.com','070 45743673','honung',0,''),(4,'Elsa','Testsson','19781201-5761','teststigen 5','testholm','testerElsa@helloworld.com','070 6971482','aftonbladet',0,''),(5,'Julia','Cesarsson','19920211-4247','testbacken 8','testeborg','juliatesting@helloworld.com','070 69831486','jordgubbe',0,''),(6,'Nils','Leandersson','19780423-3324','Guttastigen 40','Guttamåla','nils.leandersson@gmail.com','010 1234567','hej',1,'[]'),(7,'Roy','Karlsson','20010323-3323','Nygatan 2','Oslo','bla@bla.no','010 5683747','123',0,''),(8,'Roy','Karlsson','650301-5621','Tokgatan 2','Tokholm','roy@tokholm.se','08 7482943','123',0,'[]'),(9,'Kurt','Olsson','123-56-7890','Ekstigen 4','Hökanäs','kurt@kurt.se','034 567877','kurt',0,''),(10,'Kent','Kentsson','650301-7721','Kentvägen 78','Risanäs','kent@kentnet.se','0457 57364','kent',0,'');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Order`
--

DROP TABLE IF EXISTS `Order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `time` int(11) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Order`
--

LOCK TABLES `Order` WRITE;
/*!40000 ALTER TABLE `Order` DISABLE KEYS */;
INSERT INTO `Order` VALUES (27,6,1487275729),(28,6,1487319687),(30,6,1487675009),(31,6,1487675173),(32,6,1487675369),(33,6,1487675459),(34,6,1487675524),(35,6,1487675865),(36,6,1487680473),(37,6,1487680516),(38,6,1487680701),(39,6,1487683449),(40,6,1487702856),(41,6,1487713655),(42,6,1487802740),(43,6,1487879189),(44,6,1487882347),(45,1,1488138183),(46,6,1488186217),(47,6,1488216106),(48,8,1488237399),(49,8,1488237461),(50,6,1488312217),(51,8,1488362248),(52,8,1488362306),(53,8,1488362346),(54,1,1488452739),(55,6,1488479043);
/*!40000 ALTER TABLE `Order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OrderProduct`
--

DROP TABLE IF EXISTS `OrderProduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OrderProduct` (
  `product_id` int(11) DEFAULT NULL,
  `order_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OrderProduct`
--

LOCK TABLES `OrderProduct` WRITE;
/*!40000 ALTER TABLE `OrderProduct` DISABLE KEYS */;
INSERT INTO `OrderProduct` VALUES (100,27),(45,27),(46,27),(101,27),(105,27),(104,27),(103,27),(102,27),(421,27),(385,27),(353,27),(115,27),(814,27),(902,27),(100,28),(385,28),(46,30),(100,30),(104,31),(101,32),(101,32),(100,33),(353,34),(101,35),(105,36),(104,36),(102,37),(45,37),(46,37),(103,37),(46,38),(103,39),(103,39),(103,39),(103,39),(103,39),(103,39),(353,40),(100,41),(385,42),(100,43),(100,44),(46,45),(105,45),(104,45),(45,46),(101,46),(100,46),(101,47),(100,47),(814,47),(101,48),(101,48),(101,49),(101,49),(101,49),(101,49),(101,49),(101,49),(100,49),(100,49),(100,49),(100,49),(100,49),(100,49),(100,49),(46,49),(46,49),(46,49),(46,49),(46,49),(46,49),(45,49),(45,49),(45,49),(45,49),(45,49),(45,49),(102,49),(102,49),(102,49),(102,49),(102,49),(102,49),(103,49),(103,49),(103,49),(103,49),(103,49),(103,49),(103,49),(104,49),(104,49),(104,49),(105,49),(105,49),(105,49),(105,49),(105,49),(421,49),(421,49),(421,49),(421,49),(421,49),(421,49),(421,49),(385,49),(385,49),(385,49),(385,49),(385,49),(385,49),(353,49),(353,49),(353,49),(353,49),(353,49),(353,49),(115,49),(115,49),(115,49),(115,49),(115,49),(115,49),(115,49),(814,49),(814,49),(814,49),(814,49),(814,49),(814,49),(814,49),(814,49),(902,49),(902,49),(902,49),(902,49),(902,49),(902,49),(902,49),(902,49),(100,50),(45,50),(46,51),(46,51),(46,51),(46,52),(45,52),(102,52),(102,52),(102,52),(102,52),(102,52),(102,52),(102,52),(103,52),(103,52),(103,52),(103,52),(103,52),(103,52),(103,52),(103,52),(103,52),(103,52),(103,52),(103,52),(105,52),(105,52),(105,52),(105,52),(105,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(104,52),(353,52),(353,52),(353,52),(385,52),(385,52),(385,52),(385,52),(385,52),(385,52),(385,52),(385,52),(385,52),(385,52),(385,52),(385,52),(333,52),(333,52),(333,52),(333,52),(333,52),(333,52),(333,52),(333,52),(333,52),(333,52),(333,52),(333,52),(115,52),(115,52),(115,52),(115,52),(115,52),(115,52),(115,52),(115,52),(115,52),(115,52),(115,52),(103,53),(103,53),(103,53),(103,53),(103,53),(421,53),(421,53),(421,53),(421,53),(421,53),(421,53),(421,53),(421,53),(421,53),(333,54),(400,54),(902,54),(46,55),(333,55),(104,55);
/*!40000 ALTER TABLE `OrderProduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Product` (
  `product_id` int(11) NOT NULL,
  `name` varchar(60) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(1000) COLLATE utf8_unicode_ci NOT NULL,
  `imgname` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `manufacturer` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `instock` int(11) NOT NULL,
  `cost` decimal(10,2) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Product`
--

LOCK TABLES `Product` WRITE;
/*!40000 ALTER TABLE `Product` DISABLE KEYS */;
INSERT INTO `Product` VALUES (45,'Toyota','Almost new.','toy.jpg','Toyota',0,5000.00),(46,'Yugo','Slow and defective.','yugo.jpg','Yugo',4,1.00),(100,'Låda','Låda med okänt innehåll. Fantastiskt tillfälle att köpa grisen i säcken!','lada.jpg','Unknown',3,50000.00),(101,'Mård','Nästan tam mård, ej rumsren.','mard.jpg','Svensk',4,500.00),(102,'Ekorre','Fridlyst ekorre.','ekorre.jpg','SydSvensk',-1,1500.00),(103,'Jord','Säckar med jord säljes billigt.','jord.jpg','Landtmanna',-2,100.00),(104,'Skottkärra','Fin gammal skottkärra i topskick!','skott.jpg','Åbykärran',42,1500.00),(105,'Micro','Fabriksny micro!!!','micro.jpg','Elon',-1,999.00),(115,'Paper bag','Needful Things branded Paper bag.','1.png','Paper-R-Us',99973,100.00),(333,'BLT Sandwich','Fresh sandwich','blt.jpg','Subway',31,50.00),(353,'Volvo','A retro Volvo Amazon -69. Still in mint condition!','volvo.jpg','Volvo',6,100000.00),(385,'SAAB','A retro SAAB that needs some tender loving care.','saab.jpg','SAAB',36,100.00),(400,'Laptop Screen','Exellent laptop screen. Only 237,454 hours on it.','screen.jpg','MacBook',554,1500.00),(421,'Winth 435','A used boat in good condition that still floats!','boat.jpg','Winth',4,15000.00),(814,'Book','Needful Things by Stephen King. Brand new!','2.jpg','Stephen King',-2,300.00),(902,'iPhone','A defective iPhone in need of repair.','iphone.jpg','Apple',990,400.00);
/*!40000 ALTER TABLE `Product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-02 19:28:55
