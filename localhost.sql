-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 19-Out-2023 às 23:59
-- Versão do servidor: 5.7.11
-- PHP Version: 5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_atividade`
--
CREATE DATABASE IF NOT EXISTS `db_atividade` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `db_atividade`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tb_dados`
--

CREATE TABLE `tb_dados` (
  `id` int(11) NOT NULL,
  `pdata` date DEFAULT NULL,
  `nome_cliente` varchar(250) DEFAULT NULL,
  `origem` varchar(250) DEFAULT NULL,
  `destino` varchar(250) DEFAULT NULL,
  `forma_pagamento` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `tb_dados`
--

INSERT INTO `tb_dados` (`id`, `pdata`, `nome_cliente`, `origem`, `destino`, `forma_pagamento`) VALUES
(1, '2023-10-19', 'jOCA', 'recife', 'joao pesoa', 'Pix'),
(3, '2023-10-19', 'jOCA', 'recife', 'joao pesoa', 'Pix'),
(4, '2000-01-01', '', '', '', 'Pix'),
(5, '2000-01-01', 'Joca', 'Recife', 'Portugal', 'Boleto');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_dados`
--
ALTER TABLE `tb_dados`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_dados`
--
ALTER TABLE `tb_dados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
