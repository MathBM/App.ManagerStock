SET GLOBAL host_cache_size=0
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "-03:00";

CREATE DATABASE IF NOT EXISTS `Silver_POS` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `Silver_POS`;

CREATE TABLE `STOCKS` (
  `product_code` int NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `product_weight` float NOT NULL,
  `qty_stock` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `USERS` (
  `id` int NOT NULL,
  `first_names` varchar(100) DEFAULT NULL,
  `last_names` varchar(100) DEFAULT NULL,
  `user_names` varchar(100) DEFAULT NULL,
  `passwords` longtext,
  `Role` enum('Admin','Operator') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE `STOCKS`
  ADD PRIMARY KEY (`product_code`);

ALTER TABLE `USERS`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `STOCKS`
  MODIFY `product_code` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1455446;

ALTER TABLE `USERS`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

  INSERT INTO `USERS` (`id`, `first_names`, `last_names`, `user_names`, `passwords`, `Role`) VALUES
(2, 'Admin', 'admin', 'admin', '9af15b336e6a9619928537df30b2e6a2376569fcf9d7e773eccede65606529a0', 'Admin'),
(4, 'op', 'op', 'op', '9af15b336e6a9619928537df30b2e6a2376569fcf9d7e773eccede65606529a0', 'Operator');