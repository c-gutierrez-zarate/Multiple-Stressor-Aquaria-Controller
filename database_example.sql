-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 07-06-2024 a las 16:57:52
-- Versión del servidor: 10.3.34-MariaDB-0+deb10u1
-- Versión de PHP: 7.3.27-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `database_sample`
--

--
-- Table structure of `cal_od`
--

CREATE TABLE `cal_od` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `cal_od_T1` float NOT NULL,
  `cal_od_T2` float NOT NULL,
  `cal_od_T3` float NOT NULL,
  `cal_od_T4` float NOT NULL,
  `cal_od_T5` float NOT NULL,
  `cal_od_T6` float NOT NULL,
  `cal_od_T7` float NOT NULL,
  `cal_od_T8` float NOT NULL,
  `cal_od_C1` float NOT NULL,
  `cal_od_C2` float NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cal_od`
--

INSERT INTO `cal_od` (`id`, `date`, `cal_od_T1`, `cal_od_T2`, `cal_od_T3`, `cal_od_T4`, `cal_od_T5`, `cal_od_T6`, `cal_od_T7`, `cal_od_T8`, `cal_od_C1`, `cal_od_C2`) VALUES 
(1,'2023-02-24 16:59:32',12,12,11,15,0,8,5,5,0,0);

-- --------------------------------------------------------
--
-- Table structure of `cal_od_mgl`
--

CREATE TABLE `cal_od_mgl` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `cal_od_T1mg` float NOT NULL,
  `cal_od_T2mg` float NOT NULL,
  `cal_od_T3mg` float NOT NULL,
  `cal_od_T4mg` float NOT NULL,
  `cal_od_T5mg` float NOT NULL,
  `cal_od_T6mg` float NOT NULL,
  `cal_od_T7mg` float NOT NULL,
  `cal_od_T8mg` float NOT NULL,
  `cal_od_C1mg` float NOT NULL,
  `cal_od_C2mg` float NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cal_od_mgl`
--

INSERT INTO `cal_od_mgl` (`id`, `date`, `cal_od_T1mg`, `cal_od_T2mg`, `cal_od_T3mg`, `cal_od_T4mg`, `cal_od_T5mg`, `cal_od_T6mg`, `cal_od_T7mg`, `cal_od_T8mg`, `cal_od_C1mg`, `cal_od_C2mg`) VALUES 
(1,'2023-02-02 12:27:01',0.4,0.3,1.2,0.5,0.41,1.1,0.8,-0.9,0,0);

-- --------------------------------------------------------
--
-- Table structure of `cal_ph`
--

CREATE TABLE `cal_ph` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `cal_ph_T1` float NOT NULL,
  `cal_ph_T2` float NOT NULL,
  `cal_ph_T3` float NOT NULL,
  `cal_ph_T4` float NOT NULL,
  `cal_ph_T5` float NOT NULL,
  `cal_ph_T6` float NOT NULL,
  `cal_ph_T7` float NOT NULL,
  `cal_ph_T8` float NOT NULL,
  `cal_ph_C1` float NOT NULL,
  `cal_ph_C2` float NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cal_ph`
--

INSERT INTO `cal_ph` (`id`, `date`, `cal_ph_T1`, `cal_ph_T2`, `cal_ph_T3`, `cal_ph_T4`, `cal_ph_T5`, `cal_ph_T6`, `cal_ph_T7`, `cal_ph_T8`, `cal_ph_C1`, `cal_ph_C2`) VALUES
(1,'2023-02-23 16:35:39',0.018,0,0.021,0,0.015,0,0.008,0,0,0);

-- --------------------------------------------------------
--
-- Table structure of `cal_temp`
--

CREATE TABLE `cal_temp` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `cal_temp_T1` float NOT NULL,
  `cal_temp_T2` float NOT NULL,
  `cal_temp_T3` float NOT NULL,
  `cal_temp_T4` float NOT NULL,
  `cal_temp_T5` float NOT NULL,
  `cal_temp_T6` float NOT NULL,
  `cal_temp_T7` float NOT NULL,
  `cal_temp_T8` float NOT NULL,
  `cal_temp_BM1` float NOT NULL,
  `cal_temp_BM1_negro` float NOT NULL,
  `cal_temp_BM1_blanco` float NOT NULL,
  `cal_temp_BM2` float NOT NULL,
  `cal_temp_BM2_rojo` float NOT NULL,
  `cal_temp_BM2_azul` float NOT NULL,
  `cal_temp_BM3` float NOT NULL,
  `cal_temp_BM3_negro` float NOT NULL,
  `cal_temp_BM3_blanco` float NOT NULL,
  `cal_temp_BM4` float NOT NULL,
  `cal_temp_BM4_rojo` float NOT NULL,
  `cal_temp_BM4_azul` float NOT NULL,
  `cal_temp_Agua` float NOT NULL,
  `cal_temp_Room` float NOT NULL,
  `cal_temp_BM5` float NOT NULL,
  `cal_temp_Cap` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `cal_temp`
--

INSERT INTO `cal_temp` (`id`, `date`, `cal_temp_T1`, `cal_temp_T2`, `cal_temp_T3`, `cal_temp_T4`, `cal_temp_T5`, `cal_temp_T6`, `cal_temp_T7`, `cal_temp_T8`, `cal_temp_BM1`, `cal_temp_BM1_negro`, `cal_temp_BM1_blanco`, `cal_temp_BM2`, `cal_temp_BM2_rojo`, `cal_temp_BM2_azul`, `cal_temp_BM3`, `cal_temp_BM3_negro`, `cal_temp_BM3_blanco`, `cal_temp_BM4`, `cal_temp_BM4_rojo`, `cal_temp_BM4_azul`, `cal_temp_Agua`, `cal_temp_Room`, `cal_temp_BM5`, `cal_temp_Cap`) VALUES
(1, '2022-12-29 13:05:40', 0.25, 0.2, 0.05, 0.3, 0, 0.05, 1.7, 0.2, 0.2, 0.2, 0.3, -0.1, 0.2, 0.2, 0.4, 0.15, 0.1, 0.3, 0.3, 0.9, 0, -1, 1.7, 0.45);

-- --------------------------------------------------------
--
-- Table structure of `cal_temp_ph_od`
--

CREATE TABLE `cal_temp_ph_od` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `cal_temp_T1` float NOT NULL,
  `cal_temp_T2` float NOT NULL,
  `cal_temp_T3` float NOT NULL,
  `cal_temp_T4` float NOT NULL,
  `cal_temp_T5` float NOT NULL,
  `cal_temp_T6` float NOT NULL,
  `cal_temp_T7` float NOT NULL,
  `cal_temp_T8` float NOT NULL,
  `cal_temp_C1` float NOT NULL,
  `cal_temp_C2` float NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cal_temp_ph_od`
--

INSERT INTO `cal_temp_ph_od` (`id`, `date`, `cal_temp_T1`, `cal_temp_T2`, `cal_temp_T3`, `cal_temp_T4`, `cal_temp_T5`, `cal_temp_T6`, `cal_temp_T7`, `cal_temp_T8`, `cal_temp_C1`, `cal_temp_C2`) VALUES 
(1,'2022-11-08 09:29:39',0.2,0.16,0.23,0.05,0.2,0.3,0.3,0.2,-1.7,-0.7);

-- --------------------------------------------------------
--
-- Table structure of `data_od`
--

CREATE TABLE `data_od` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `date` datetime NOT NULL,
  `od_T1` float NOT NULL,
  `od_T2` float NOT NULL,
  `od_T3` float NOT NULL,
  `od_T4` float NOT NULL,
  `od_T5` float NOT NULL,
  `od_T6` float NOT NULL,
  `od_T7` float NOT NULL,
  `od_T8` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `data_od`
--

INSERT INTO `data_od` (`id`, `name`, `date`, `od_T1`, `od_T2`, `od_T3`, `od_T4`, `od_T5`, `od_T6`, `od_T7`, `od_T8`) VALUES
(1, 'Proyecto_corales', '2022-06-07 17:29:13', 102.5,109,79.1,79.8,82.4,82,68.4,83.7,101,105);

-- --------------------------------------------------------
--
-- Table structure of `data_od_mgl`
--

CREATE TABLE `data_od_mgl` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `date` datetime NOT NULL,
  `od_T1mg` float NOT NULL,
  `od_T2mg` float NOT NULL,
  `od_T3mg` float NOT NULL,
  `od_T4mg` float NOT NULL,
  `od_T5mg` float NOT NULL,
  `od_T6mg` float NOT NULL,
  `od_T7mg` float NOT NULL,
  `od_T8mg` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `data_od_mgl`
--

INSERT INTO `data_od_mgl` (`id`, `name`, `date`, `od_T1mg`, `od_T2mg`, `od_T3mg`, `od_T4mg`, `od_T5mg`, `od_T6mg`, `od_T7mg`, `od_T8mg`) VALUES

-- --------------------------------------------------------

--
-- Table structure of `data_ph`
--

CREATE TABLE `data_ph` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `date` datetime NOT NULL,
  `ph_T1` float NOT NULL,
  `ph_T2` float NOT NULL,
  `ph_T3` float NOT NULL,
  `ph_T4` float NOT NULL,
  `ph_T5` float NOT NULL,
  `ph_T6` float NOT NULL,
  `ph_T7` float NOT NULL,
  `ph_T8` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `data_ph`
--

INSERT INTO `data_ph` (`id`, `name`, `date`, `ph_T1`, `ph_T2`, `ph_T3`, `ph_T4`, `ph_T5`, `ph_T6`, `ph_T7`, `ph_T8`) VALUES
(1,'Proyecto_Corales','2022-06-07 17:29:13',7.803,8.263,7.816,8.238,7.818,8.267,7.822,8.238,7.82,7.983);

-- --------------------------------------------------------

--
-- Table structure of `data_temp`
--

CREATE TABLE `data_temp` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `date` datetime NOT NULL,
  `temp_T1` float NOT NULL,
  `temp_T2` float NOT NULL,
  `temp_T3` float NOT NULL,
  `temp_T4` float NOT NULL,
  `temp_T5` float NOT NULL,
  `temp_T6` float NOT NULL,
  `temp_T7` float NOT NULL,
  `temp_T8` float NOT NULL,
  `temp_BM1` float NOT NULL,
  `temp_BM1_negro` float NOT NULL,
  `temp_BM1_blanco` float NOT NULL,
  `temp_BM2` float NOT NULL,
  `temp_BM2_rojo` float NOT NULL,
  `temp_BM2_azul` float NOT NULL,
  `temp_BM3` float NOT NULL,
  `temp_BM3_negro` float NOT NULL,
  `temp_BM3_blanco` float NOT NULL,
  `temp_BM4` float NOT NULL,
  `temp_BM4_rojo` float NOT NULL,
  `temp_BM4_azul` float NOT NULL,
  `temp_Agua` float NOT NULL,
  `temp_Room` float NOT NULL,
  `temp_Cap` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `data_temp`
--

INSERT INTO `data_temp` (`id`, `name`, `date`, `temp_T1`, `temp_T2`, `temp_T3`, `temp_T4`, `temp_T5`, `temp_T6`, `temp_T7`, `temp_T8`, `temp_BM1`, `temp_BM1_negro`, `temp_BM1_blanco`, `temp_BM2`, `temp_BM2_rojo`, `temp_BM2_azul`, `temp_BM3`, `temp_BM3_negro`, `temp_BM3_blanco`, `temp_BM4`, `temp_BM4_rojo`, `temp_BM4_azul`, `temp_Agua`, `temp_Room`, `temp_Cap`) VALUES
(1, 'Proyecto_Corales', '2023-01-26 18:30:22', 11.62, 11.64, 11.74, 11.49, 14.62, 14.68, 14.76, 14.64, 11.82, 12.01, 12.05, 12.15, 11.95, 12.01, 15.03, 14.9, 14.97, 15.05, 14.93, 15.03, 9.81, 13.19, 11.32),

-- --------------------------------------------------------
--
-- Table structure for table `data_temp_ph_od`
--

CREATE TABLE `data_temp_ph_od` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `date` datetime NOT NULL,
  `temp_T1` float NOT NULL,
  `temp_T2` float NOT NULL,
  `temp_T3` float NOT NULL,
  `temp_T4` float NOT NULL,
  `temp_T5` float NOT NULL,
  `temp_T6` float NOT NULL,
  `temp_T7` float NOT NULL,
  `temp_T8` float NOT NULL,
  `temp_C1` float NOT NULL,
  `temp_C2` float NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `data_temp_ph_od`
--

INSERT INTO `data_temp_ph_od` (`id`, `name`, `date`, `temp_T1`, `temp_T2`, `temp_T3`, `temp_T4`, `temp_T5`, `temp_T6`, `temp_T7`, `temp_T8`, `temp_C1`, `temp_C2`) VALUES
(1,'Proyecto_Corales','2022-06-07 17:29:13',13.14,12.91,12.54,12.65,14.82,15.24,14.55,14.45,11.44,10.81);

-- --------------------------------------------------------
--
-- Table structure of `estado_boton`
--

CREATE TABLE `estado_boton` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `name` varchar(50) NOT NULL,
  `estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `estado_boton`
--

INSERT INTO `estado_boton` (`id`, `date`, `name`, `estado`) VALUES
(1, '2022-06-16 12:25:22', 'botonT8temp', 1);

-- --------------------------------------------------------
--
-- Table structure of `hist_od`
--

CREATE TABLE `hist_od` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `hist_od_T1` float NOT NULL,
  `hist_od_T2` float NOT NULL,
  `hist_od_T3` float NOT NULL,
  `hist_od_T4` float NOT NULL,
  `hist_od_T5` float NOT NULL,
  `hist_od_T6` float NOT NULL,
  `hist_od_T7` float NOT NULL,
  `hist_od_T8` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `hist_od`
--

INSERT INTO `hist_od` (`id`, `date`, `hist_od_T1`, `hist_od_T2`, `hist_od_T3`, `hist_od_T4`, `hist_od_T5`, `hist_od_T6`, `hist_od_T7`, `hist_od_T8`) VALUES
(1, '2022-06-07 17:45:35', 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5);

-- --------------------------------------------------------

--
-- Table structure of `hist_ph`
--

CREATE TABLE `hist_ph` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `hist_ph_T1` float NOT NULL,
  `hist_ph_T2` float NOT NULL,
  `hist_ph_T3` float NOT NULL,
  `hist_ph_T4` float NOT NULL,
  `hist_ph_T5` float NOT NULL,
  `hist_ph_T6` float NOT NULL,
  `hist_ph_T7` float NOT NULL,
  `hist_ph_T8` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `hist_ph`
--

INSERT INTO `hist_ph` (`id`, `date`, `hist_ph_T1`, `hist_ph_T2`, `hist_ph_T3`, `hist_ph_T4`, `hist_ph_T5`, `hist_ph_T6`, `hist_ph_T7`, `hist_ph_T8`) VALUES
(1, '2021-09-20 12:00:00', 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005);

-- --------------------------------------------------------

--
-- Table structure of `hist_temp`
--

CREATE TABLE `hist_temp` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `hist_temp_T1` float NOT NULL,
  `hist_temp_T2` float NOT NULL,
  `hist_temp_T3` float NOT NULL,
  `hist_temp_T4` float NOT NULL,
  `hist_temp_T5` float NOT NULL,
  `hist_temp_T6` float NOT NULL,
  `hist_temp_T7` float NOT NULL,
  `hist_temp_T8` float NOT NULL,
  `hist_temp_BM1` float NOT NULL,
  `hist_temp_BM2` float NOT NULL,
  `hist_temp_BM3` float NOT NULL,
  `hist_temp_BM4` float NOT NULL,
  `hist_temp_BM5` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `hist_temp`
--

INSERT INTO `hist_temp` (`id`, `date`, `hist_temp_T1`, `hist_temp_T2`, `hist_temp_T3`, `hist_temp_T4`, `hist_temp_T5`, `hist_temp_T6`, `hist_temp_T7`, `hist_temp_T8`, `hist_temp_BM1`, `hist_temp_BM2`, `hist_temp_BM3`, `hist_temp_BM4`, `hist_temp_BM5`) VALUES
(1, '2022-04-07 13:34:53', 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1);

-- --------------------------------------------------------

--
-- Table structure of `set_od`
--

CREATE TABLE `set_od` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `set_od_T1` float NOT NULL,
  `set_od_T2` float NOT NULL,
  `set_od_T3` float NOT NULL,
  `set_od_T4` float NOT NULL,
  `set_od_T5` float NOT NULL,
  `set_od_T6` float NOT NULL,
  `set_od_T7` float NOT NULL,
  `set_od_T8` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `set_od`
--

INSERT INTO `set_od` (`id`, `date`, `set_od_T1`, `set_od_T2`, `set_od_T3`, `set_od_T4`, `set_od_T5`, `set_od_T6`, `set_od_T7`, `set_od_T8`) VALUES
(1, '2021-10-02 12:23:24', 91.2, 92, 93, 94, 95, 96, 97, 98);

-- --------------------------------------------------------

--
-- Table structure of `set_ph`
--

CREATE TABLE `set_ph` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `set_ph_T1` float NOT NULL,
  `set_ph_T2` float NOT NULL,
  `set_ph_T3` float NOT NULL,
  `set_ph_T4` float NOT NULL,
  `set_ph_T5` float NOT NULL,
  `set_ph_T6` float NOT NULL,
  `set_ph_T7` float NOT NULL,
  `set_ph_T8` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `set_ph`
--

INSERT INTO `set_ph` (`id`, `date`, `set_ph_T1`, `set_ph_T2`, `set_ph_T3`, `set_ph_T4`, `set_ph_T5`, `set_ph_T6`, `set_ph_T7`, `set_ph_T8`) VALUES
(1, '2021-10-15 14:48:00', 7.8, 8.2, 7.8, 8.2, 7.81, 8.2, 7.81, 8.2);

-- --------------------------------------------------------

--
-- Table structure of `set_temp`
--

CREATE TABLE `set_temp` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `set_temp_T1` float NOT NULL,
  `set_temp_T2` float NOT NULL,
  `set_temp_T3` float NOT NULL,
  `set_temp_T4` float NOT NULL,
  `set_temp_T5` float NOT NULL,
  `set_temp_T6` float NOT NULL,
  `set_temp_T7` float NOT NULL,
  `set_temp_T8` float NOT NULL,
  `set_temp_BM1` float NOT NULL,
  `set_temp_BM2` float NOT NULL,
  `set_temp_BM3` float NOT NULL,
  `set_temp_BM4` float NOT NULL,
  `set_temp_BM5` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `set_temp`
--

INSERT INTO `set_temp` (`id`, `date`, `set_temp_T1`, `set_temp_T2`, `set_temp_T3`, `set_temp_T4`, `set_temp_T5`, `set_temp_T6`, `set_temp_T7`, `set_temp_T8`, `set_temp_BM1`, `set_temp_BM2`, `set_temp_BM3`, `set_temp_BM4`, `set_temp_BM5`) VALUES
(1, '2023-02-28 13:29:45', 11.5, 11.5, 11.5, 11.5, 14.5, 14.5, 14.5, 14.5, 12, 12, 15, 15, 25);

-- --------------------------------------------------------

--
-- Table structure of `sondas_od`
--

CREATE TABLE `sondas_od` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `tank` varchar(11) NOT NULL,
  `num_sonda` int(11) NOT NULL,
  `num_serie` varchar(50) NOT NULL,
  `i2c` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `sondas_od`
--

INSERT INTO `sondas_od` (`id`, `date`, `tank`, `num_sonda`, `num_serie`, `i2c`) VALUES
(1, '2021-09-20 12:00:00', 'T1', 1, '00-0000000000001', '71'),
(2, '2021-10-04 21:30:32', 'T2', 2, '00-000000000002', '72'),
(3, '2021-09-20 12:00:00', 'T3', 3, '00-0000000000003', '73'),
(4, '2021-10-04 21:32:19', 'T4', 4, '00-000000000004', '74'),
(5, '2021-09-20 12:00:00', 'T5', 5, '00-0000000000005', '75'),
(6, '2021-10-04 21:32:19', 'T6', 6, '00-000000000006', '76'),
(7, '2021-09-20 12:00:00', 'T7', 7, '00-0000000000007', '77'),
(8, '2021-10-04 21:28:51', 'T8', 8, '00-000000000008', '78'),
(9, '2021-09-20 12:00:00', 'T9', 9, '00-0000000000009', '79'),
(10, '2021-10-04 21:31:30', 'T10', 10, '00-000000000010', '80');

-- --------------------------------------------------------

--
-- Table structure of `sondas_ph`
--

CREATE TABLE `sondas_ph` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `tank` varchar(11) NOT NULL,
  `num_sonda` int(11) NOT NULL,
  `num_serie` varchar(50) NOT NULL,
  `i2c` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `sondas_ph`
--

INSERT INTO `sondas_ph` (`id`, `date`, `tank`, `num_sonda`, `num_serie`, `i2c`) VALUES
(1, '2021-09-20 12:00:00', 'T1', 1, '00-0000000000001', '61'),
(2, '2021-10-04 21:30:32', 'T2', 2, '00-000000000002', '62'),
(4, '2021-09-20 12:00:00', 'T3', 3, '00-0000000000003', '63'),
(5, '2021-10-04 21:24:44', 'T4', 4, '00-000000000004', '64'),
(6, '2021-09-20 12:00:00', 'T5', 5, '00-0000000000005', '65'),
(7, '2021-10-04 21:28:51', 'T6', 6, '00-000000000006', '66'),
(8, '2021-09-20 12:00:00', 'T7', 7, '00-0000000000007', '67'),
(9, '2021-10-04 21:30:32', 'T8', 8, '00-000000000008', '68'),
(10, '2021-09-20 12:00:00', 'T9', 9, '00-0000000000009', '69'),
(11, '2021-10-04 21:31:30', 'T10', 10, '00-000000000010', '70');

-- --------------------------------------------------------

--
-- Table structure of `sondas_temp`
--

CREATE TABLE `sondas_temp` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `tank` varchar(11) NOT NULL,
  `num_sonda` int(11) NOT NULL,
  `num_serie` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Data dump for the table `sondas_temp`
--

INSERT INTO `sondas_temp` (`id`, `date`, `tank`, `num_sonda`, `num_serie`) VALUES
(1, '2022-05-18 18:12:44', 'T1', 1, '28-0121121160c7'),
(2, '2022-05-18 18:13:08', 'T2', 2, '28-012112541d09'),
(4, '2022-05-18 18:14:12', 'T3', 3, '28-0121114dc680'),
(5, '2022-05-18 18:14:31', 'T4', 4, '28-012112d0446c'),
(6, '2022-05-18 18:19:57', 'T5', 5, '28-0121127c24d7'),
(7, '2022-05-18 18:14:55', 'T6', 6, '28-0121114d5325'),
(8, '2021-10-05 19:05:44', 'T7', 7, '28-03089779d143'),
(9, '2022-05-11 20:23:59', 'T8', 8, '28-3c01d075376c'),
(10, '2022-05-18 18:15:24', 'BM1', 9, '28-01211256a2f9'),
(11, '2022-05-18 18:15:42', 'BM2', 10, '28-0121128391bc'),
(13, '2022-05-18 18:15:58', 'BM3', 11, '28-012112c21e40'),
(14, '2022-03-24 19:57:55', 'BM4', 12, '28-0621b2160ae8'),
(16, '2022-05-18 18:16:15', 'BM1_blanco', 13, '28-0121124a6f9f'),
(17, '2022-05-18 18:16:38', 'BM1_negro', 14, '28-012112b47cd1'),
(18, '2022-05-25 10:01:57', 'BM2_rojo', 15, '28-0121128ae371'),
(19, '2022-05-18 18:17:10', 'BM2_azul', 16, '28-0121125549eb'),
(20, '2022-05-18 18:18:47', 'BM3_blanco', 17, '28-0121116383ee'),
(21, '2022-05-18 18:19:03', 'BM3_negro', 18, '28-0121130927c8'),
(22, '2022-05-25 10:02:14', 'BM4_rojo', 19, '28-0121127c24d7'),
(23, '2022-10-24 08:59:44', 'BM4_azul', 20, '28-3c01d0755cd9'),
(24, '2022-05-18 18:22:51', 'Agua', 21, '28-0121122c2b6a'),
(25, '2022-05-18 18:46:12', 'Room', 22, '28-0417b1c26dff'),
(26, '2022-04-04 19:00:00', 'BM5', 23, '28-3c01d0751a22'),
(27, '2022-06-11 19:11:32', 'Cap', 24, '28-03089779b1a2');

-- --------------------------------------------------------

--
-- Table structure for table `sondas_temp_ph_od`
--

CREATE TABLE `sondas_temp_ph_od` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `tank` varchar(11) NOT NULL,
  `num_sonda` int(11) NOT NULL,
  `num_serie` varchar(50) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sondas_temp`
--

INSERT INTO `sondas_temp_ph_od`(`id`, `date`, `tank`, `num_sonda`, `num_serie`) VALUES 
(1,'2021-10-05 19:04:03','T1',1,'28-3c01d075154e'),
(2,'2021-10-05 19:04:24','T2',2,'28-3c01d6072792'),
(4,'2021-10-05 19:04:40','T3',3,'28-3c01d607c1f7'),
(5,'2021-10-05 19:04:57','T4',4,'28-3c01d6076ba8'),
(6,'2021-10-05 19:05:13','T5',5,'28-3c01d6074a2c'),
(7,'2021-10-05 19:05:28','T6',6,'28-3c01d607377b'),
(8,'2021-10-05 19:05:44','T7',7,'28-03089779d143'),
(9,'2021-10-05 19:06:04','T8',8,'28-3c01d6072bbc'),
(10,'2021-10-05 19:06:22','C1',9,'28-3c01d607ee62'),
(11,'2021-10-05 19:08:45','C2',10,'28-3c01d6074bb8');

-- --------------------------------------------------------

-- TABLE INDEXES


--
-- Indexes of `cal_od`
--
ALTER TABLE `cal_od`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `cal_od_mgl`
--
ALTER TABLE `cal_od_mgl`
  ADD PRIMARY KEY (`id`);
  
--
-- Indexes of `cal_ph`
--
ALTER TABLE `cal_ph`
  ADD PRIMARY KEY (`id`);
  
--
-- Indexes of `cal_temp`
--
ALTER TABLE `cal_temp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `cal_temp_ph_od`
--
ALTER TABLE `cal_temp_ph_od`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `data_od`
--
ALTER TABLE `data_od`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `data_od_mgl`
--
ALTER TABLE `data_od_mgl`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `data_ph`
--
ALTER TABLE `data_ph`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `data_temp`
--
ALTER TABLE `data_temp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `data_temp_ph_od`
--
ALTER TABLE `data_temp_ph_od`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `estado_boton`
--
ALTER TABLE `estado_boton`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `hist_od`
--
ALTER TABLE `hist_od`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `hist_ph`
--
ALTER TABLE `hist_ph`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `hist_temp`
--
ALTER TABLE `hist_temp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `set_od`
--
ALTER TABLE `set_od`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `set_ph`
--
ALTER TABLE `set_ph`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `set_temp`
--
ALTER TABLE `set_temp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `sondas_od`
--
ALTER TABLE `sondas_od`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `sondas_ph`
--
ALTER TABLE `sondas_ph`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `sondas_temp`
--
ALTER TABLE `sondas_temp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes of `sondas_temp_ph_od`
--
ALTER TABLE `sondas_temp_ph_od`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT
--

--
-- AUTO_INCREMENT of `cal_od`
--
ALTER TABLE `cal_od`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `cal_od_mgl`
--
ALTER TABLE `cal_od_mgl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `cal_ph`
--
ALTER TABLE `cal_ph`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `cal_temp`
--
ALTER TABLE `cal_temp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `cal_temp_ph_od`
--
ALTER TABLE `cal_temp_ph_od`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `data_od`
--
ALTER TABLE `data_od`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `data_od_mgl`
--
ALTER TABLE `data_od_mgl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `data_ph`
--
ALTER TABLE `data_ph`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `data_temp`
--
ALTER TABLE `data_temp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17414;
  --
-- AUTO_INCREMENT of `data_temp_ph_od`
--
ALTER TABLE `data_temp_ph_od`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17414;
--
-- AUTO_INCREMENT of `estado_boton`
--
ALTER TABLE `estado_boton`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=392;
--
-- AUTO_INCREMENT of `hist_od`
--
ALTER TABLE `hist_od`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `hist_ph`
--
ALTER TABLE `hist_ph`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `hist_temp`
--
ALTER TABLE `hist_temp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `set_od`
--
ALTER TABLE `set_od`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `set_ph`
--
ALTER TABLE `set_ph`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `set_temp`
--
ALTER TABLE `set_temp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT of `sondas_od`
--
ALTER TABLE `sondas_od`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT of `sondas_ph`
--
ALTER TABLE `sondas_ph`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT of `sondas_temp`
--
ALTER TABLE `sondas_temp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
--
-- AUTO_INCREMENT of `sondas_temp_ph_od`
--
ALTER TABLE `sondas_temp_ph_od`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
