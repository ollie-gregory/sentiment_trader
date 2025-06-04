CREATE TABLE `FUND` (
  `fund_id` varchar(255) PRIMARY KEY NOT NULL,
  `fund_name` varchar(255) NOT NULL,
  `fund_value` double NOT NULL
);

CREATE TABLE `TRADE` (
  `trade_id` varchar(255) PRIMARY KEY NOT NULL,
  `fund_id` varchar(255) NOT NULL,
  `stock_id` varchar(255) NOT NULL,
  `price` double NOT NULL,
  `quantity` double NOT NULL,
  `type` ENUM ('BUY', 'SELL') NOT NULL,
  `execution_date` timestamp NOT NULL,
  `pnl` double NOT NULL
);

CREATE TABLE `STOCK` (
  `stock_id` varchar(255) PRIMARY KEY NOT NULL,
  `stock_name` varchar(255) NOT NULL,
  `ticker` varchar(255) NOT NULL,
  `exchange` varchar(255),
  `asset_type` varchar(255),
  `ipo_date` timestamp,
  `current_price` double
);

CREATE TABLE `HISTORIC_PRICE` (
  `stock_id` varchar(255) NOT NULL,
  `interval` ENUM ('1m', '5m', '10m', '30m', '1hr', '1d') NOT NULL,
  `close_timestamp` timestamp NOT NULL,
  `open_price` double,
  `high_price` double,
  `low_price` double,
  `close_price` double NOT NULL,
  `volume` double,
  PRIMARY KEY (`stock_id`, `interval`, `close_timestamp`)
);

CREATE TABLE `FUND_HISTORY` (
  `fund_id` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `closing_value` double NOT NULL,
  `change` double NOT NULL,
  PRIMARY KEY (`fund_id`, `date`)
);

CREATE TABLE `DEPOSIT` (
  `deposit_id` varchar(255) NOT NULL,
  `fund_id` varchar(255) NOT NULL,
  `timestamp` timestamp NOT NULL,
  `deposit_amount` double NOT NULL,
  `type` ENUM ('DEPOSIT', 'WITHDRAWAL') NOT NULL
);

CREATE TABLE `SENTIMENT` (
  `sentiment_id` varchar(255) PRIMARY KEY NOT NULL,
  `stock_id` varchar(255),
  `timestamp` timestamp NOT NULL,
  `source` ENUM ('REDDIT', 'TWITTER', 'NEWS') NOT NULL,
  `content` varchar(255) NOT NULL
);

ALTER TABLE `TRADE` ADD FOREIGN KEY (`fund_id`) REFERENCES `FUND` (`fund_id`);

ALTER TABLE `TRADE` ADD FOREIGN KEY (`stock_id`) REFERENCES `STOCK` (`stock_id`);

ALTER TABLE `HISTORIC_PRICE` ADD FOREIGN KEY (`stock_id`) REFERENCES `STOCK` (`stock_id`);

ALTER TABLE `FUND_HISTORY` ADD FOREIGN KEY (`fund_id`) REFERENCES `FUND` (`fund_id`);

ALTER TABLE `DEPOSIT` ADD FOREIGN KEY (`fund_id`) REFERENCES `FUND` (`fund_id`);

ALTER TABLE `SENTIMENT` ADD FOREIGN KEY (`stock_id`) REFERENCES `STOCK` (`stock_id`);
