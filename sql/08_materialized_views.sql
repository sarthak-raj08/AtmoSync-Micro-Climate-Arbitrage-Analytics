
USE atmosync;

DROP TABLE IF EXISTS sensor_summary;

CREATE TABLE sensor_summary AS

SELECT

container_id,

AVG(temperature_c) AS avg_temp,

AVG(humidity_percent) AS avg_humidity,

AVG(vibration_level) AS avg_vibration,

AVG(battery_percent) AS avg_battery

FROM sensor_data

GROUP BY container_id;