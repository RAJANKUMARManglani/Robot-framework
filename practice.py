import itertools
import os
import subprocess
import time
import traceback

import connection as connection
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sshtunnel import SSHTunnelForwarder

subprocess.call('start', shell=True)
os.chdir('/Users/rajan.kumar.manglani/Documents/DB')
print('Navigated to Directory where ssh keys are present')
output = subprocess.getoutput('ls')
print(output)
try:
    # Create an SSH tunnel
    tunnel = SSHTunnelForwarder(
        ('34.195.7.84', 22),
        ssh_private_key="/Users/rajan.kumar.manglani/Documents/DB/test.pem",
        ssh_username="rajan.k",
        remote_bind_address=('fr-test.cdgrcme2rcfh.us-east-1.rds.amazonaws.com', 5432),
        local_bind_address=('localhost', 6543),  # could be any available port
    )
    print("ssh connection made sucessfully")
    # Start the tunnel
    tunnel.start()


    def show_query(title, qry):
        print('%s' % (title))
        cursor.execute(qry)
        for row1 in cursor.fetchall():
            print(row1)
        print('')


    connection = psycopg2.connect(
        database='farmrise', host=tunnel.local_bind_host, port=tunnel.local_bind_port,
        user='farmersfirstappuser', password='iYCgasd',
        connect_timeout=20
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    print("database connected")
    cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
    print(cursor.fetchall())
    show_query('current database', 'SELECT current_database()')
    show_query('available databases', 'SELECT * FROM pg_database')
    cursor.close()
    print("cursor is closed")
    connection.close()
    print("PostgreSQL connection is closed")
    # stop the tunnel
    tunnel.stop()
    print("tunnel stopped for ssh successfully")

except (Exception, psycopg2.Error) as error:
    print(traceback.format_exc())
    print("Connection Failed")
    print("Error while connecting to PostgreSQL", error)
finally:

    # closing database connection.
    if connection:
        connection.close()
        print("PostgreSQL database connection is closed successfully")
