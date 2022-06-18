import mysql.connector
from mysql.connector import errorcode

# Config for database
config = {
    'user': 'db_user_1',
    'password': 'db_user_password',
    'host': 'localhost',
    'database': 'timeparsing',
    'raise_on_warnings': True
}

# initializing MySQL connection (cursor 1)
try:
  my_cn1 = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
    quit()
else:
  print ("Connected to the Database")

# initializing MySQL connection (cursor 2)
try:
  my_cn2 = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
    quit()
else:
  print ("Connected to the Database")

c_sql = "select amount0Out from main order by block"
cursor1.execute(c_sql, [main])
for c in cursor1:
         c_sql = "select amount0In from main order by block"
         cursor1.execute(c_sql, [main])
         for b in cursor1:
             cursor1.execute('insert into amountdb (amount0) value (%s)', [ b[0] - c[0])
             my_cn1.commit()

c_sql = "select amount1Out from main order by block"
cursor2.execute(c_sql, [main])
for y in cursor2:
         c_sql = "select amount1In from main order by block"
         cursor2.execute(c_sql, [main])
         for t in cursor2:
             cursor2.execute('insert into amountdb (amount1) value (%s)', [ t[0] - y[0])
             my_cn2.commit()

# Close the cursor and the connection
cursor.close()
my_cn.close()

cursor2.close()
my_cn2.close()