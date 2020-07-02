import itertools
import os
import subprocess
import sys
import time
import traceback

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sshtunnel import SSHTunnelForwarder


def connect_to_qa_db():
    subprocess.call('start', shell=True)
    print("shell launched")
    os.chdir('/Users/rajan.kumar.manglani/Documents/DB')
    print("shell launched")
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


def connect_to_stage_db():
    subprocess.call('start', shell=True)
    print("shell launched")
    os.chdir('/Users/rajan.kumar.manglani/Documents/DB')
    print("shell launched")
    output = subprocess.getoutput('ls')
    print(output)
    try:
        # Create an SSH tunnel
        tunnel = SSHTunnelForwarder(
            ('18.204.109.115', 22),
            ssh_private_key="/Users/rajan.kumar.manglani/Documents/DB/stage.pem",
            ssh_username="rajan.k",
            remote_bind_address=('fr-stage.cdgrcme2rcfh.us-east-1.rds.amazonaws.com', 5432),
            local_bind_address=('localhost', 6543),  # could be any available port
        )
        print("ssh connection made sucessfully")
        # Start the tunnel
        tunnel.start()

        def show_query(title, qry):
            print('%s' % title)
            cursor.execute(qry)
            for row1 in cursor.fetchall():
                print(row1)
            print('')

        connection = psycopg2.connect(
            database='farmrise', host=tunnel.local_bind_host, port=tunnel.local_bind_port,
            user='farmersfirstappuser', password='iYFGbg9dnasa',
            connect_timeout=20
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        print("database connected")
        cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        print(cursor.fetchall())
        show_query('current database', 'SELECT current_database()')
        show_query('available databases', 'SELECT * FROM pg_database')
        print("connecting to %s ...farmrise_users ")
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


def retrieve_all_column_values_database_qa(dbname, postgreSQL_select_Query):
    subprocess.call('start', shell=True)
    print("shell launched")
    os.chdir('/Users/rajan.kumar.manglani/Documents/DB')
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
        print("ssh tunnel is started successfully")

        connection = psycopg2.connect(
            database=dbname, host=tunnel.local_bind_host, port=tunnel.local_bind_port,
            user='farmersfirstappuser', password='iYCgasd',
            connect_timeout=20
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        print("database is connected sucessfully")
        # postgreSQL_select_Query = "select * from farmrise.blf_users where phone_number='9035344027';"
        print("Print each row and it's columns values")
        cursor.execute(postgreSQL_select_Query)
        feedback_records = cursor.fetchall()
        # Total records found in table
        print("Total rows are:  ", len(feedback_records))
        print(feedback_records)
        # Length of rows-
        print("No of  in rows displayed in table", len(feedback_records))
        cursor.execute(postgreSQL_select_Query)
        for i in range(len(feedback_records)):
            feedback_records[i] = cursor.fetchone()
            print("Printing rows of List in separate new line", feedback_records[i])

        # converting into List
        rows = list(feedback_records)
        print(rows)
        # Fetching the column names
        col_names = [cn[0] for cn in cursor.description]
        print(
            f'{col_names[0]} {col_names[1]} {col_names[2]} {col_names[3]} {col_names[4]} {col_names[5]} {col_names[6]} {col_names[7]}')
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


def retrieve_all_column_values_database_staging(dbname, postgreSQL_select_Query):
    subprocess.call('start', shell=True)
    print("shell launched")
    os.chdir('/Users/rajan.kumar.manglani/Documents/DB')
    output = subprocess.getoutput('ls')
    print(output)
    try:
        # Create an SSH tunnel
        tunnel = SSHTunnelForwarder(
            ('18.204.109.115', 22),
            ssh_private_key="/Users/rajan.kumar.manglani/Documents/DB/stage.pem",
            ssh_username="rajan.k",
            remote_bind_address=('fr-stage.cdgrcme2rcfh.us-east-1.rds.amazonaws.com', 5432),
            local_bind_address=('localhost', 6543),  # could be any available port
        )
        print("ssh connection made sucessfully")
        # Start the tunnel
        tunnel.start()
        print("ssh tunnel is started successfully")
        connection = psycopg2.connect(
            database=dbname, host=tunnel.local_bind_host, port=tunnel.local_bind_port,
            user='farmersfirstappuser', password='iYCgasd',
            connect_timeout=20
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        print("database is connected sucessfully")
        # postgreSQL_select_Query = "select * from farmrise.blf_users where phone_number='9035344027';"
        print("Print each row and it's columns values")
        cursor.execute(postgreSQL_select_Query)
        feedback_records = cursor.fetchall()
        # Total records found in table
        print("Total rows are:  ", len(feedback_records))
        print(feedback_records)
        # Length of rows-
        print("No of  in rows displayed in table", len(feedback_records))
        cursor.execute(postgreSQL_select_Query)
        for i in range(len(feedback_records)):
            feedback_records[i] = cursor.fetchone()
            print("Printing rows of List in separate new line", feedback_records[i])

        # converting into List
        rows = list(feedback_records)
        print(rows)
        # Fetching the column names
        col_names = [cn[0] for cn in cursor.description]
        print(
            f'{col_names[0]} {col_names[1]} {col_names[2]} {col_names[3]} {col_names[4]} {col_names[5]} {col_names[6]} {col_names[7]}')
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


def extract_specific_single_column_qa(dbname, column_name, table_name):
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
        print("ssh tunnel is started successfully")

        connection = psycopg2.connect(
            database=dbname, host=tunnel.local_bind_host, port=tunnel.local_bind_port,
            user='farmersfirstappuser', password='iYCgasd',
            connect_timeout=20
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        print("database connected successfully")
        time.sleep(10)
        postgreSQL_select_Query = "select " + column_name + "from " + table_name + " where " \
                                                                                   "phone_number='9035344027'; "
        cursor.execute(postgreSQL_select_Query)
        feedback_records = cursor.fetchall()
        print("Print each row and it's columns values")
        for row in feedback_records:
            print(column_name, row[0], "\n")

        list_of_ids = list(itertools.chain.from_iterable(cursor))
        len(list_of_ids)
        print(list_of_ids)
        print("Total columns present in DB:  ", len(list_of_ids))
        # Fetching the column names
        col_names = [cn[0] for cn in cursor.description]
        col1 = f'{col_names[0]}'
        print(col1, list_of_ids)
        cursor.execute(postgreSQL_select_Query)
        for i in range(len(feedback_records)):
            feedback_records[i] = cursor.fetchone()
            print("Printing rows of List in separate new line", feedback_records[i])

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
            print("PostgreSQL connection is closed")


def extract_multiple_columns_qa(dbname, column1, column2, column3, table_name):
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
        print("ssh tunnel is started successfully")
        connection = psycopg2.connect(
            database=dbname, host=tunnel.local_bind_host, port=tunnel.local_bind_port,
            user='farmersfirstappuser', password='iYCgasd',
            connect_timeout=20
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        print("database connected successfully")
        time.sleep(10)
        postgreSQL_select_Query = "select " + column1 + "," + column2 + "," + column3 + " from " + table_name + "order by " \
                                                                                                                "created_at desc limit 5; "
        cursor.execute(postgreSQL_select_Query)
        feedback_records = cursor.fetchall()
        print("Print each row and it's columns values")
        for row in feedback_records:
            print("user_id = ", row[0], )
            print("commodity_id = ", row[1])
            print("market_id  = ", row[2], "\n")

        cursor.execute(postgreSQL_select_Query)
        list_of_ids = list(itertools.chain.from_iterable(cursor))
        len(list_of_ids)
        print(list_of_ids)
        print("Total columns present in DB:  ", len(list_of_ids))
        # Fetching the column names
        col_names = [cn[0] for cn in cursor.description]
        col1 = f'{col_names[0]}'
        col2 = f'{col_names[1]}'
        col3 = f'{col_names[2]}'
        print(col1, col2, col3)
        # Length of rows-
        print("No of  in rows displayed in table", len(feedback_records))
        cursor.execute(postgreSQL_select_Query)
        for i in range(len(feedback_records)):
            feedback_records[i] = cursor.fetchone()
            print("Printing rows of List in separate new line", feedback_records[i])

        cursor.execute(postgreSQL_select_Query)
        record_first_list = cursor.fetchone()
        print("First row is displayed successfully", record_first_list)

        print("Fetching next row")
        record_next_element = cursor.fetchone()
        print("First row is displayed successfully", record_next_element)

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
            print("PostgreSQL connection is closed")


def extract_specific_single_column_stage(dbname, column_name, table_name):
    subprocess.call('start', shell=True)
    os.chdir('/Users/rajan.kumar.manglani/Documents/DB')
    print('Navigated to Directory where ssh keys are present')
    output = subprocess.getoutput('ls')
    print(output)
    try:
        # Create an SSH tunnel
        tunnel = SSHTunnelForwarder(
            ('18.204.109.115', 22),
            ssh_private_key="/Users/rajan.kumar.manglani/Documents/DB/stage.pem",
            ssh_username="rajan.k",
            remote_bind_address=('fr-stage.cdgrcme2rcfh.us-east-1.rds.amazonaws.com', 5432),
            local_bind_address=('localhost', 6543),  # could be any available port
        )
        print("ssh connection made sucessfully")
        # Start the tunnel
        tunnel.start()
        print("ssh tunnel is started successfully")
        connection = psycopg2.connect(
            database=dbname, host=tunnel.local_bind_host, port=tunnel.local_bind_port,
            user='farmersfirstappuser', password='iYCgasd',
            connect_timeout=20
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        print("database connected successfully")
        time.sleep(10)
        postgreSQL_select_Query = "select " + column_name + "from " + table_name + " where " \
                                                                                   "phone_number='9035344027'; "
        cursor.execute(postgreSQL_select_Query)
        feedback_records = cursor.fetchall()
        print("Print each row and it's columns values")
        for row in feedback_records:
            print(column_name, row[0], "\n")

        list_of_ids = list(itertools.chain.from_iterable(cursor))
        len(list_of_ids)
        print(list_of_ids)
        print("Total columns present in DB:  ", len(list_of_ids))
        # Fetching the column names
        col_names = [cn[0] for cn in cursor.description]
        col1 = f'{col_names[0]}'
        print(col1, list_of_ids)
        cursor.execute(postgreSQL_select_Query)
        for i in range(len(feedback_records)):
            feedback_records[i] = cursor.fetchone()
            print("Printing rows of List in separate new line", feedback_records[i])

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
            print("PostgreSQL connection is closed")


def extract_multiple_columns_stage(dbname, column1, column2, column3, table_name):
    subprocess.call('start', shell=True)
    os.chdir('/Users/rajan.kumar.manglani/Documents/DB')
    print('Navigated to Directory where ssh keys are present')
    output = subprocess.getoutput('ls')
    print(output)
    try:
        # Create an SSH tunnel
        tunnel = SSHTunnelForwarder(
            ('18.204.109.115', 22),
            ssh_private_key="/Users/rajan.kumar.manglani/Documents/DB/stage.pem",
            ssh_username="rajan.k",
            remote_bind_address=('fr-stage.cdgrcme2rcfh.us-east-1.rds.amazonaws.com', 5432),
            local_bind_address=('localhost', 6543),  # could be any available port
        )
        print("ssh connection made sucessfully")
        # Start the tunnel
        tunnel.start()
        print("ssh tunnel is started successfully")
        connection = psycopg2.connect(
            database=dbname, host=tunnel.local_bind_host, port=tunnel.local_bind_port,
            user='farmersfirstappuser', password='iYCgasd',
            connect_timeout=20
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        print("database connected successfully")
        time.sleep(10)
        postgreSQL_select_Query = "select " + column1 + "," + column2 + "," + column3 + " from " + table_name + \
                                  "order by created_at desc limit 5; "

        cursor.execute(postgreSQL_select_Query)
        feedback_records = cursor.fetchall()
        print("Print each row and it's columns values")
        for row in feedback_records:
            print("user_id = ", row[0], )
            print("commodity_id = ", row[1])
            print("market_id  = ", row[2], "\n")

        cursor.execute(postgreSQL_select_Query)
        list_of_ids = list(itertools.chain.from_iterable(cursor))
        len(list_of_ids)
        print(list_of_ids)
        print("Total columns present in DB:  ", len(list_of_ids))
        # Fetching the column names
        col_names = [cn[0] for cn in cursor.description]
        col1 = f'{col_names[0]}'
        col2 = f'{col_names[1]}'
        col3 = f'{col_names[2]}'
        print(col1, col2, col3)
        # Length of rows-
        print("No of  in rows displayed in table", len(feedback_records))
        cursor.execute(postgreSQL_select_Query)
        for i in range(len(feedback_records)):
            feedback_records[i] = cursor.fetchone()
            print("Printing rows of List in separate new line", feedback_records[i])

        cursor.execute(postgreSQL_select_Query)
        record_first_list = cursor.fetchone()
        print("First row is displayed successfully", record_first_list)

        print("Fetching next row")
        record_next_element = cursor.fetchone()
        print("First row is displayed successfully", record_next_element)

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
            print("PostgreSQL connection is closed")


def clean_up_kill():
    # cleaning the ports opened
    cls = subprocess.call('clear', shell=True)
    print(cls)
    print("Terminals opened by python programs are cleaned up & killed ")
    sys.exit()


def delete_row_table(dbname, Column_value):
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
        print("ssh tunnel is started successfully")

        connection = psycopg2.connect(
            database=dbname, host=tunnel.local_bind_host, port=tunnel.local_bind_port,
            user='farmersfirstappuser', password='iYCgasd',
            connect_timeout=20
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        print("database connected successfully")
        time.sleep(10)
        cursor.execute("Delete from farmrise.blf_users where id=%s", (Column_value,))
        print("Row deleted from table successfully", "farmrise.blf_users")
        # get the number of updated rows
        rows_deleted = cursor.rowcount
        print("Count of row deleted", rows_deleted)
        # Commit the changes to the database
        connection.commit()

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


connect_to_qa_db()
connect_to_stage_db()
retrieve_all_column_values_database_qa('farmrise_users', "select * from farmrise.blf_users where "
                                                         "phone_number='9035344027'; ")

retrieve_all_column_values_database_staging('farmrise_users', "select * from farmrise.blf_users where "
                                                              "phone_number='9035344027'; ")

extract_specific_single_column_qa('farmrise_users', 'otp', 'farmrise.otp_verifications')
extract_multiple_columns_qa('farmrise_commodities', 'user_id', 'commodity_id', 'market_id', 'farmrise.user_feedback')
extract_specific_single_column_stage('farmrise_users', 'otp', 'farmrise.otp_verifications')
extract_multiple_columns_stage('farmrise_commodities', 'user_id', 'commodity_id', 'market_id', 'farmrise.user_feedback')
delete_row_table('farmrise_users', 6)
