-- ==========================================
-- Container Master
-- ==========================================

CREATE TABLE container_master (

container_id VARCHAR(20) PRIMARY KEY,

container_type VARCHAR(50),

capacity_kg INT,

owner_company VARCHAR(100),

status VARCHAR(30)

);

-- ==========================================
-- Shipment Master
-- ==========================================

CREATE TABLE shipment_master (

shipment_id VARCHAR(20) PRIMARY KEY,

container_id VARCHAR(20),

product VARCHAR(50),

origin_city VARCHAR(50),

destination_city VARCHAR(50),

departure_date DATE,

arrival_date DATE,

FOREIGN KEY(container_id)

REFERENCES container_master(container_id)

);

-- ==========================================
-- Sensor Data
-- ==========================================

CREATE TABLE sensor_data (

sensor_id INT PRIMARY KEY,

shipment_id VARCHAR(20),

container_id VARCHAR(20),

temperature_c FLOAT,

humidity_percent FLOAT,

vibration_level FLOAT,

door_status VARCHAR(20),

battery_percent INT,

gps_latitude DOUBLE,

gps_longitude DOUBLE,

timestamp DATETIME

);

-- ==========================================
-- Commodity Prices
-- ==========================================

CREATE TABLE commodity_prices (

price_id INT AUTO_INCREMENT PRIMARY KEY,

date DATE,

city VARCHAR(50),

product VARCHAR(50),

market_price_per_kg FLOAT,

demand_index INT,

supply_index INT

);