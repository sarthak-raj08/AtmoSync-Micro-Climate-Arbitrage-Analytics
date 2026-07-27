USE atmosync;

-- =====================================
-- Latest Sensor Readings
-- =====================================

CREATE OR REPLACE VIEW latest_sensor_status AS

SELECT

container_id,

AVG(temperature_c) AS avg_temperature,

AVG(humidity_percent) AS avg_humidity,

AVG(vibration_level) AS avg_vibration,

AVG(battery_percent) AS avg_battery

FROM sensor_data

GROUP BY container_id;

-- =====================================
-- Commodity Price Summary
-- =====================================

CREATE OR REPLACE VIEW commodity_summary AS

SELECT

product,

AVG(market_price_per_kg) AS average_price,

MAX(market_price_per_kg) AS highest_price,

MIN(market_price_per_kg) AS lowest_price

FROM commodity_prices

GROUP BY product;