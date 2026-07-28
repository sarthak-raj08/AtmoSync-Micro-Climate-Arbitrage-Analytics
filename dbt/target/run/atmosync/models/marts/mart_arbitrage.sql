
  
    

create or replace transient table ATMOSYNC_DB.PUBLIC.mart_arbitrage
    
    
    
    
    

    as (SELECT

container_id,

shipment_id,

health_score,

spoilage_probability,

CASE

WHEN spoilage_probability >= 80

THEN 'Immediate Reroute'

WHEN spoilage_probability >= 50

THEN 'Monitor'

ELSE 'Normal Delivery'

END AS recommendation

FROM ATMOSYNC_DB.PUBLIC.int_spoilage
    )
;


  