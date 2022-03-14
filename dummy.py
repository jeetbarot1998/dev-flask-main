# # import os
# # import psycopg2
# # import datetime
# #
# # connection = psycopg2.connect('postgres://ucmdkokipuljyi:3911ddbd4da67f64a3cf80355b0bf7a1cb2221337a43e32c83851f49eeffcfba@ec2-3-226-211-228.compute-1.amazonaws.com:5432/ddvlni5bs2bil6')
# # cursor = connection.cursor()
# # # insert_query = """ INSERT INTO movie_entries(movie_1, movie_2, inserted_on) VALUES(%s, %s, %s) """
# # # item_purchase_time = datetime.datetime.now()
# # # print('here1 time=============',item_purchase_time)
# # # item_tuple = ('test_2', 'test_2', item_purchase_time)
# # # cursor.execute(insert_query, item_tuple)
# # # print('Inserted')
# # cursor.execute("SELECT *FROM movie_entries")
# # purchase_datetime = cursor.fetchall()
# # print('here select====================',purchase_datetime)
# # #
# # # DATABASE_URL = 'postgres://ucmdkokipuljyi:3911ddbd4da67f64a3cf80355b0bf7a1cb2221337a43e32c83851f49eeffcfba@ec2-3-226-211-228.compute-1.amazonaws.com:5432/ddvlni5bs2bil6'
# # #
# # # conn = psycopg2.connect( dbname='ddvlni5bs2bil6 host=ec2-3-226-211-228.compute-1.amazonaws.com', port=5432, user='ucmdkokipuljyi' ,password='3911ddbd4da67f64a3cf80355b0bf7a1cb2221337a43e32c83851f49eeffcfba', sslmode='require')
# # #
# # # cursor = conn.cursor()
# # # # Executing a SQL query to insert data into  table
# # # insert_query = """ INSERT INTO MOVIE_ENTRIES (MOVIE_1, MOVIE_2, INSERTED_ON) VALUES ('Test_movie_1', 'Test_movie_2', 'Todays Date')"""
# # #
# # # cursor.execute(insert_query)
# # # conn.commit()
# # # print("1 Record inserted successfully")
# # # cursor.execute("SELECT * from MOVIE_ENTRIES")
# # # record = cursor.fetchall()
# # # print("Result ", record)
# # #
# # #
import time
start_time = time.time()
print(start_time)
di = [{'ID':90,'D':'S'},{'ID':90,'D':'B'},{'ID':90,'D':'C'}]
# m=[]
# c=dict()
# for b in di:
#     [m.append((k,v)) for k,v in b.items() if (k,v) not in m]
# for a in m:
#     c[a[1]] = a[0]
# print(c)
a={}
for i in di:
    for k,v in i.items():
        a.setdefault(v,set()).add(k)
print(a)

print(time.time())
print("--- %s seconds ---" % (time.time() - start_time))
