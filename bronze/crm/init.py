import sqlite3

def run_sql_cust_info(filename):
    conn = sqlite3.connect("bronze.db")
    cursor = conn.cursor()
    
    with open(filename) as f:
        row = f.readline()
        csv_file = f.readlines()
        csv_file = [tuple(i.replace("\n","").split(",")) for i in csv_file]
    cursor.execute("BEGIN TRANSACTION;")
    cursor.executemany(f"INSERT INTO crm_cust_info VALUES (?,?,?,?,?,?,?)",csv_file)
    conn.commit()
    conn.close()

def run_sql_prd_info(filename):
    conn = sqlite3.connect("bronze.db")
    cursor = conn.cursor()
    
    with open(filename) as f:
        row = f.readline()
        csv_file = f.readlines()
        csv_file = [tuple(i.replace("\n","").split(",")) for i in csv_file]
    cursor.execute("BEGIN TRANSACTION;")
    cursor.executemany(f"INSERT INTO crm_prd_info VALUES (?,?,?,?,?,?,?)",csv_file)
    conn.commit()
    conn.close()

def run_sql_sales_details(filename):
    conn = sqlite3.connect("bronze.db")
    cursor = conn.cursor()
    
    with open(filename) as f:
        row = f.readline()
        csv_file = f.readlines()
        csv_file = [tuple(i.replace("\n","").split(",")) for i in csv_file]
    cursor.execute("BEGIN TRANSACTION;")
    cursor.executemany(f"INSERT INTO crm_sales_details VALUES (?,?,?,?,?,?,?,?,?)",csv_file)
    conn.commit()
    conn.close()
 

run_sql_cust_info("datasets/source_crm/cust_info.csv")
run_sql_prd_info("datasets/source_crm/prd_info.csv")
run_sql_sales_details("datasets/source_crm/sales_details.csv")