import os
import subprocess

import paramiko
import psycopg2
from paramiko import SSHClient


def connect_to_db():
    subprocess.call('start', shell=True)
    print("shell launched")
    os.chdir('/Users/rajan.kumar.manglani/Documents/DB')
    print("shell launched")
    output = subprocess.getoutput('ls')
    print(output)
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('rajan.k@34.195.7.84:/Users/rajan.kumar.manglani/Documents/DB/test.pem')
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
    print(ssh_stdout)
    output = subprocess.getoutput('yes')
    print(output)

    # output = subprocess.getoutput('ssh -i "test.pem" rajan.k@34.195.7.84')
    # Set up a connection to the postgres server.
    con = psycopg2.connect(database="farmrise", user="farmersfirstappuser", password="iYCgasd", host="fr-test"
                                                                                                     ".cdgrcme2rcfh"
                                                                                                     ".us-east-1.rds"
                                                                                                     ".amazonaws.com",
                           port="5432")
    print("Database opened successfully")


connect_to_db()
