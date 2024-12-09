SELECT c.brandid,
       c.source,
       c.inspireid,
       c.firstname,
       c.lastname
FROM {{cust_profile_plr_bv}} c
INNER JOIN
  (SELECT DISTINCT brand_id,
                   source_system_nm
   FROM {{cip_sources}}
   WHERE active_ind = TRUE
     AND usecase = 'UC2'
     AND source_data_flow = 'udp1' ) conf ON lower(c.brandid) = conf.brand_id
AND lower(c.source) = conf.source_system_nm
LIMIT 50;