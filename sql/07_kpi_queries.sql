USE atmosync;

-- Average Temperature

SELECT

AVG(temperature_c) AS avg_temperature

FROM sensor_data;

--------------------------------------------------

-- Highest Commodity Price

SELECT

product,

MAX(market_price_per_kg) AS highest_price

FROM commodity_prices

GROUP BY product;

--------------------------------------------------

-- Shipment Count

SELECT

COUNT(*) AS total_shipments

FROM shipment_master;

--------------------------------------------------

-- Battery Status

SELECT

AVG(battery_percent) AS average_battery

FROM sensor_data;

--------------------------------------------------

-- Containers per Product

SELECT

product,

COUNT(*) AS total

FROM shipment_master

GROUP BY product;