#  to be used with mySOL test database

import mysql.connector
from mysql.connector import errorcode
import sys

conn_str = {
    'user': 'Python',
    'password': 'password',
    'host': '192.168.1.195',
    'database': 'dougtest',
    'raise_on_warnings': True
    }

# add_emp = ('''INSERT INTO customers
#            (lname, fname, dob)
#            values ('Suida', 'Wayne', '1934-03-03')''')

add_emp2 = (
    '''
    INSERT INTO customers (lname, fname, dob)
    VALUES ('Suida', 'Wayne', '1943-03-02')
    '''
    )

# del_emp = ('''DELETE FROM customers
#            WHERE fname = 'Wayne' ''')

q_emp = '''SELECT * FROM customers'''

try:
    # cnx = mysql.connector.connect(user='Python', password='Ferret11', host='192.168.1.195', database='dougtest')
    cnx = mysql.connector.connect(**conn_str)
    cursor = cnx.cursor()
    cursor.execute(add_emp2)  # write new record to database
    # cursor.execute(del_emp)  # delete test rows form database
    cursor.execute(q_emp)  # pull current records from database
    rows = cursor.fetchall()  # rows is a list of tuples
    cnx.commit()
    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
        sys.exit()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
        sys.exit()
    elif err.errno == 2003:
        print(f"No server at {conn_str['host']} listening on port 3306.")
        sys.exit()
    else:
        print('There was an error:')
        print(err)
        print(err.errno)
        sys.exit()
else:
    cnx.close()

for item in rows:
    print(item)

