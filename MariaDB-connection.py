import mariadb
import boto3
import sys
import os

#os.environ.DBEndpoint_value
#env.DBPort_value
#env.DBIdentifier

try
    env_vars = {}
with open("db_details.txt", "r") as file:
    for line in file:
        key, value = line.strip().split("=")
        env_vars[key] = value
print(f"Address of Database {env_vars['Address']}")
print(f"Address of DBPort {env_vars['Port']}")


try: # connection
    connection = mariadb.connect(host = os.getenv('DBIdentifier'), database = env_vars['Address'], port = env_vars['Port'], user = 'root', passwd = '')
    cursor = connection.cursor()
    
    
    print('')
    print('\033[0;32mCONNECTION ESTABLISHED\033[m')
    
    established = 1
    sleep(2)
    os.system('cls')
    
except:
    print('')
    print('\033[0;31mERROR CONNECTING DATABASE...\033[m')
    
    sleep(1)
    established = 0
    
 
    
if established == 1: # if connection is established
    
    try:
    
        #"psql -h ${Endpoint} -p ${DatabasePort} -U ${MasterUserName} -d {databaseName} -f 
         bash /workspace/PUCENGG/aws-rds/RDSPostgresSQL/scripts/queries.sql
    
    except mariadb.Error as e:
    print(f"Credentials Error: {e}")
    sys.exit(1)








