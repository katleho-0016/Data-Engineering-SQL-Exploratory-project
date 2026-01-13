import sqlite3
from time import sleep
def run_sql(filename):
    conn = sqlite3.connect("bronze.db")
    cursor = conn.cursor()
    
    with open(filename) as f:
        sql_file = f.read()

    cursor.executescript(sql_file)
    conn.commit()
    conn.close()

## create datawarehouse and tables 

set_up = ["bronze/crm/crm_cust_info.sql","bronze/crm/crm_prd_info.sql",
          "bronze/crm/crm_sales_details.sql","bronze/erp/erp_cust_az12.sql","bronze/erp/erp_loc_a101.sql",
          "bronze/erp/erp_pc_cat_g1v2.sql"]
for  i in set_up:
    run_sql(i)
    sleep(1)