CREATE DATABASE  IF NOT EXISTS `namastebd` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `namastebd`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: namastebd
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `reserva`
--

DROP TABLE IF EXISTS `reserva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reserva` (
  `idreserva` int NOT NULL,
  `fk_cliente` int NOT NULL,
  `fecha` date NOT NULL,
  `status_pago` tinyint NOT NULL,
  PRIMARY KEY (`idreserva`),
  KEY `fk_clientet_idx` (`fk_cliente`),
  CONSTRAINT `fk_clientet` FOREIGN KEY (`fk_cliente`) REFERENCES `tcliente` (`idtcliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserva`
--

LOCK TABLES `reserva` WRITE;
/*!40000 ALTER TABLE `reserva` DISABLE KEYS */;
/*!40000 ALTER TABLE `reserva` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tablacl_ter`
--

DROP TABLE IF EXISTS `tablacl_ter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tablacl_ter` (
  `id_tct` int NOT NULL,
  `idfk_cliente` int NOT NULL,
  `idfk_terapeuta` int NOT NULL,
  `idk_servicio` int NOT NULL,
  `total` int NOT NULL,
  PRIMARY KEY (`id_tct`),
  KEY `fkcliente_idx` (`idfk_cliente`),
  KEY `fk_ter_idx` (`idfk_terapeuta`),
  KEY `fk_serv_idx` (`idk_servicio`),
  CONSTRAINT `fk_serv` FOREIGN KEY (`idk_servicio`) REFERENCES `tablaservicios` (`id_servicio`),
  CONSTRAINT `fk_ter` FOREIGN KEY (`idfk_terapeuta`) REFERENCES `tterapeuta` (`idtterapeuta`),
  CONSTRAINT `fkcliente` FOREIGN KEY (`idfk_cliente`) REFERENCES `tcliente` (`idtcliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tablacl_ter`
--

LOCK TABLES `tablacl_ter` WRITE;
/*!40000 ALTER TABLE `tablacl_ter` DISABLE KEYS */;
/*!40000 ALTER TABLE `tablacl_ter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tablaservicios`
--

DROP TABLE IF EXISTS `tablaservicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tablaservicios` (
  `id_servicio` int NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `monto` decimal(10,0) NOT NULL,
  PRIMARY KEY (`id_servicio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tablaservicios`
--

LOCK TABLES `tablaservicios` WRITE;
/*!40000 ALTER TABLE `tablaservicios` DISABLE KEYS */;
/*!40000 ALTER TABLE `tablaservicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcliente`
--

DROP TABLE IF EXISTS `tcliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tcliente` (
  `idtcliente` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `descuento` decimal(10,0) DEFAULT NULL,
  `condicion_salud` varchar(500) NOT NULL,
  PRIMARY KEY (`idtcliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcliente`
--

LOCK TABLES `tcliente` WRITE;
/*!40000 ALTER TABLE `tcliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tterapeuta`
--

DROP TABLE IF EXISTS `tterapeuta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tterapeuta` (
  `idtterapeuta` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `turno` varchar(20) NOT NULL,
  `sueldo` int NOT NULL,
  `especialidad` varchar(45) NOT NULL,
  `cedula` varchar(13) NOT NULL,
  PRIMARY KEY (`idtterapeuta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tterapeuta`
--

LOCK TABLES `tterapeuta` WRITE;
/*!40000 ALTER TABLE `tterapeuta` DISABLE KEYS */;
/*!40000 ALTER TABLE `tterapeuta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'namastebd'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-24 17:51:22
