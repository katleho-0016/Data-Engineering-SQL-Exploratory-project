import sqlite3

def run_sql(filename):
    conn = sqlite3.connect("DataWareHouse.db")
    cursor = conn.cursor()
    
    with open(filename) as f:
        sql_file = f.read()

    cursor.executescript(sql_file)
    conn.commit()
    conn.close()

## create datawarehouse and tables 
set_up = ["bronze/create_datawarehouse.sql","bronze/crm/crm_cust_info.sql","bronze/crm/crm_prd_info.sql",
          "bronze/crm/crm_sales_details.sql","bronze/erp/erp_cust_info.sql","bronze/erp/erp_prd_info.sql",
          "bronze/erp/erp_sales_details.sql"]
for  i in set_up:
    run_sql(i)