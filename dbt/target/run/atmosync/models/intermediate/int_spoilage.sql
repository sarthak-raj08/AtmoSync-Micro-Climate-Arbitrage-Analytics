
  
    

create or replace transient table ATMOSYNC_DB.PUBLIC.int_spoilage
    
    
    
    
    

    as (SELECT

*,

CASE

WHEN temperature_c > 30 THEN 90

WHEN temperature_c > 25 THEN 60

ELSE 10

END AS spoilage_probability,

CASE

WHEN temperature_c > 30 THEN 'High'

WHEN temperature_c > 25 THEN 'Medium'

ELSE 'Low'

END AS spoilage_status

FROM ATMOSYNC_DB.PUBLIC.int_health_score
    )
;


  