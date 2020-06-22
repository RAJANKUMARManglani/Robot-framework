import os
import subprocess
import traceback
import psycopg2
from sshtunnel import SSHTunnelForwarder

subprocess.call('start', shell=True)
print("shell launched")
os.chdir('/Users/rajan.kumar.manglani/Documents/DB')
print("shell launched")
output = subprocess.getoutput('ls')
print(output)
try:

    # with SSHTunnelForwarder(
    #        ('34.195.7.84', 22),
    #       ssh_private_key="/Users/rajan.kumar.manglani/Documents/DB/test.pem",
    #      ssh_username="rajan.k",
    #      remote_bind_address=('fr-test.cdgrcme2rcfh.us-east-1.rds.amazonaws.com', 5432)) as server:
    #  print("server connected")

    # Create an SSH tunnel
    tunnel = SSHTunnelForwarder(
        ('34.195.7.84', 22),
        ssh_private_key="/Users/rajan.kumar.manglani/Documents/DB/test.pem",
        ssh_username="rajan.k",
        remote_bind_address=('fr-test.cdgrcme2rcfh.us-east-1.rds.amazonaws.com', 5432),
        local_bind_address=('localhost', 6543),  # could be any available port
    )
    # Start the tunnel
    tunnel.start()
    db = psycopg2.connect(
        database='farmrise', host=tunnel.local_bind_host, port=tunnel.local_bind_port,
        user='farmersfirstappuser', password='iYCgasd',
        connect_timeout=20
    )
    curs = db.cursor()
    print("database connected")
    curs.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
    print(curs.fetchall())
    postgreSQL_select_Query = "select * from mobile"



    # Stop the tunnel
    tunnel.stop()

except (Exception, psycopg2.Error) as error:
    print(traceback.format_exc())
    print("Connection Failed")
    print("Error while connecting to PostgreSQL", error)
