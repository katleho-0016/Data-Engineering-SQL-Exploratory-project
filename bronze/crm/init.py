import sqlite3

def run_sql(filename):
    conn = sqlite3.connect("DataWareHouse.db")
    cursor = conn.cursor()
    
    with open(filename) as f:
        row = f.readline()
        csv_file = f.readlines()
        csv_file = [tuple(i.replace("\n","").split(",")) for i in csv_file]
    cursor.execute("BEGIN TRANSACTION;")
    cursor.executemany(f"INSERT INTO bronze.crm_cust_info VALUES (?,?,?,?,?,?,?)")
    conn.commit()
    conn.close()
 

run_sql("datasets/source_crm/cust_info.csv")