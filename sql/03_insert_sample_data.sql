USE atmosync;

LOAD DATA LOCAL INFILE 'data/raw/container_master.csv'
INTO TABLE container_master
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'data/raw/shipment_master.csv'
INTO TABLE shipment_master
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'data/raw/container_sensor_data.csv'
INTO TABLE sensor_data
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'data/raw/commodity_prices.csv'
INTO TABLE commodity_prices
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;