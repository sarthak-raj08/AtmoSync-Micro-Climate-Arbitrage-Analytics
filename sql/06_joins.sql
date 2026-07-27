USE atmosync;

SELECT

s.shipment_id,

c.container_type,

s.product,

s.origin_city,

s.destination_city

FROM shipment_master s

JOIN container_master c

ON s.container_id = c.container_id;

----------------------------------------------------

SELECT

sd.container_id,

sd.temperature_c,

sd.humidity_percent,

sm.product,

sm.destination_city

FROM sensor_data sd

JOIN shipment_master sm

ON sd.shipment_id = sm.shipment_id;

----------------------------------------------------

SELECT

sm.product,

cp.city,

cp.market_price_per_kg

FROM shipment_master sm

JOIN commodity_prices cp

ON sm.product = cp.product;