
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select timestamp
from ATMOSYNC_DB.PUBLIC.stg_sensor_data
where timestamp is null



  
  
      
    ) dbt_internal_test