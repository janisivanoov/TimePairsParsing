# Database verification using forward lookup
import json
from logging import error, exception
import urllib.request
import web3
import mysql.connector
from mysql.connector import errorcode
from web3 import Web3

# Initialise WEB3 ENS
w3 = Web3(HTTPProvider('https://bsc-dataseed1.binance.org/'))
eth_key = 'X9FG4X92X5FVU75UWHT5W7VE6RDRYYNT6R'
contract = '0xa274d4daaff01e3aa710907aabdd57d036c96cec'

maxcount = 100

# Config for database
config = {
    'user': 'db_user_1',
    'password': 'db_user_password',
    'host': 'localhost',
    'database': 'timeparsing',
    'raise_on_warnings': True
}

# initializing MySQL connection #1
try:
  my_cn = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
    quit()
else:
  print ("Connected to the Database #1")

# initializing MySQL connection #2
try:
  my_cn2 = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
    quit()
else:
  print ("Connected to the Database #2")


# initializing MySQL connection #3
try:
  my_cn3 = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
    quit()
else:
  print ("Connected to the Database #3")

# Connecting the cursors
cursor =  my_cn.cursor() 
cursor2 =  my_cn2.cursor()
cursor3 = my_cn3.cursor()

# Making a consolidated array of addresses
# Read contracts into array
c_sql="select address from current"
cursor.execute(c_sql)
for c in cursor:
    cur_name = c[0]


c_sql = "select addr from main where addr > %s order by addr"
cursor.execute(c_sql, [cur_name])
for c in cursor:
    try:
        addr = ns.address(c[1].strip())
        cursor2.execute('update current set addr = %s', [ c[1] ])
        my_cn2.commit()
        if addr != c[0]:
            print(c[0] + '---' + c[1] + '---' + str(addr) + '--- ERROR')
            cursor3.execute('insert into audit (addr_reverse, addr_forward, message) values (%s, %s, %s)', [ c[0], str(addr), c[1], 'ERROR' ])
            my_cn3.commit()
        else:
            print(c[0] + '---' + c[1] + '---' + str(addr) + '--- OK')
    except BaseException as err:
        print(c[0] + '---' + c[1] + '---' + str(addr) + '--- Exception ' + str(err))
        cursor3.execute('insert into audit (addr_reverse, addr_forward, message) values (%s, %s, %s)', [ c[0], str(addr), c[1], 'Exception '+str(err) ])
        my_cn3.commit()
    

# Clean the database
cursor3.execulte('delete from timeparsing.main where addr in (select addr_reverse from audit)')
my_cn3.commit()
cursor3.execute('delete from timeparsing.audit')
my_cn3.commit()
        
# Close the cursor and the connection
cursor.close()
my_cn.close()

cursor2.close()
my_cn2.close()

cursor3.close()
my_cn3.close()
