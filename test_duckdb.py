import duckdb 

# with duckdb.connect() as conn: 
#     for i in range(100):
#         sql = f"select 1+{i} id" 
#         df = conn.execute(sql).fetchall()
#         print(df)


with duckdb.connect() as conn:
     sql = 'select * from '


