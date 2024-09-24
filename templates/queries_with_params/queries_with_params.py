query1 = """SELECT c.brandid,
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
LIMIT 50;"""

query2 = """SELECT c.brandid,
       c.source,
       c.inspireid,
       c.firstname,
       c.lastname
FROM cust_profile_plr_bv c
INNER JOIN
  (SELECT DISTINCT brand_id,
                   source_system_nm
   FROM cip_sources
   WHERE active_ind = TRUE
     AND usecase = 'UC2'
     AND source_data_flow = 'udp1' ) conf ON lower(c.brandid) = conf.brand_id
AND lower(c.source) = conf.source_system_nm
LIMIT 50;"""

query3 = """SELECT c.brandid,
       c.source,
       c.inspireid,
       c.firstname,
       c.lastname
FROM {{cust_profile_plr_bv}} c
INNER JOIN
  (SELECT DISTINCT brand_id,
                   source_system_nm
   FROM {{cip_sources
   WHERE active_ind = TRUE
     AND usecase = 'UC2'
     AND source_data_flow = 'udp1' ) conf ON lower(c.brandid) = conf.brand_id
AND lower(c.source) = conf.source_system_nm
LIMIT 50;"""


def replace_params(query: str):
    parts = []
    result = query.split('{{')
    parts.append(result[0])
    for i in range(1, len(result)):
        split = result[i].split('}}')

        if len(split) < 2:
            raise ValueError(f'Invalid SQL query! Table ID parameter {split[0].split()[0]} does not have closing brackets. Please check query syntax.')

        parts.append(get_table(split[0]))
        parts.append(split[1])

    for part in parts:
        print(part)
        print('--------')

def get_table(table_name: str) -> str:
   return 'QA.' + table_name

replace_params(query3)
