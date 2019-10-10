#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sqlalchemy import create_engine, inspect
import pymysql
pymysql.install_as_MySQLdb()

# Local Testing
# USERNAME="root"
# PASSWORD="TODO: Fill in password here"
# HOST="localhost"
# PORT="3357"
# SCHEMA="CHRISTUS"

# Christus Dev on Amazon RDS
USERNAME="root"
PASSWORD="narang"
HOST="127.0.0.1"
PORT="3306"
SCHEMA="sys"

# Setup Connection String
connection_string = f"{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{SCHEMA}"
engine = create_engine(f'mysql://{connection_string}')

# Table Names
# FO - Fin Ops
FO_ACCOUNTS = "FO_ACCOUNTS"
FO_FX_RATES = "FO_FX_RATES"
FO_VOLUMES = "FO_VOLUMES"
FO_ENTITIES = "FO_ENTITIES"
FO_FINANCIALS = "FO_FINANCIALS"
FO_AGGREGATED = "FO_AGGREGATED"
FO_HEADCOUNTS = "FO_HEADCOUNTS"
FO_INTL_NOI = "FO_INTL_NOI"
FO_MISSION = "FO_MISSION"
FO_REVENUE_CYCLE="FO_REVENUE_CYCLE"
FO_SUPPLY_CHAIN = "FO_SUPPLY_CHAIN"
sample_data = 'sample_data'

# CL - Clinical
CL_HARM_INDEX = "CL_HARM_INDEX"
CL_HARM_INDEX_BENCHMARK = "CL_HARM_INDEX_BENCHMARK"
CL_HARM_INDEX_YEARLY = "CL_HARM_INDEX_YEARLY"
CL_HARM_INDEX_MONTHLY = "CL_HARM_INDEX_MONTHLY"

from sqlalchemy.types import DATE
import pandas as pd
def load_to_table (file_name, table_name):
    df = pd.read_csv(file_name)
    df['CREATED_DT'] = pd.to_datetime('now')
    df['CREATED_BY'] = 'di_user'
    print("Writing {} rows, {} columns to table {}".format(df.shape[0], df.shape[1], table_name))
    sqltypes = {}
    if 'EOM_DATE' in df.columns:
        sqltypes['EOM_DATE'] = DATE
    if 'FISCAL_BOM_DATE' in df.columns:
        sqltypes['FISCAL_BOM_DATE'] = DATE
        
    df.to_sql(name=table_name, con=engine, index=False, if_exists='replace', dtype=sqltypes)
    return df.head()

