SELECT

*,

CASE

WHEN temperature_c BETWEEN 15 AND 25
AND humidity_percent BETWEEN 60 AND 80
THEN 100

WHEN temperature_c BETWEEN 10 AND 30
THEN 80

ELSE 50

END AS health_score,

CASE

WHEN temperature_c > 30
OR humidity_percent > 85

THEN 'High'

WHEN temperature_c > 25

THEN 'Medium'

ELSE 'Low'

END AS risk_level

FROM {{ ref('stg_sensor_data') }}