USE atmosync;

-- =====================================
-- Total Records
-- =====================================

SELECT COUNT(*) AS total_containers
FROM container_master;

SELECT COUNT(*) AS total_shipments
FROM shipment_master;

SELECT COUNT(*) AS total_sensor_records
FROM sensor_data;

SELECT COUNT(*) AS total_market_prices
FROM commodity_prices;

-- =====================================
-- Missing Values
-- =====================================

SELECT *
FROM sensor_data
WHERE temperature_c IS NULL
   OR humidity_percent IS NULL
   OR battery_percent IS NULL;

-- =====================================
-- Duplicate Sensor IDs
-- =====================================

SELECT
sensor_id,
COUNT(*) AS duplicates
FROM sensor_data
GROUP BY sensor_id
HAVING COUNT(*) > 1;

-- =====================================
-- Temperature Validation
-- =====================================

SELECT *
FROM sensor_data
WHERE temperature_c < -20
OR temperature_c > 60;

-- =====================================
-- Battery Validation
-- =====================================

SELECT *
FROM sensor_data
WHERE battery_percent < 0
OR battery_percent > 100;