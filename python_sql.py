import pandas as pd 
from sqlalchemy import create_engine
import sqlalchemy 
from dotenv import load_dotenv
import os

load_dotenv()

mysqluser = os.getenv('mysqluser')
mysqlpassword = os.getenv('mysqlpassword')

MYSQL_HOSTNAME = '20.62.193.224:3305'
MYSQL_USER = mysqluser
MYSQL_PASSWORD = mysqlpassword
MYSQL_DATABASE = 'synthea'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

### Test connection 
print (engine.table_names())


### Way 1A - using engine.execute
engine.execute("SELECT * FROM allergies LIMIT 100").fetchall()

### Way 1B - using engine.execute wrapped in pd.DataFrame
tempTable = pd.DataFrame(engine.execute("SELECT * FROM allergies LIMIT 100").fetchall())

### Way 2A - using PANDAS function: read_sql OR readL_sql_table 
tempTable2 = pd.read_sql('SELECT * FROM allergies LIMIT 100', engine)