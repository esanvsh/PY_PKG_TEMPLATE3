
import json
import time
#import metadata
import logging
import yaml
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import Dict
from typing import Any
from snakesay import mysqldb
#from mysqldb import conn_setup, sql_cmd
#from kafka import KafkaProducer, producer

from pydantic import BaseModel, Field
#from datetime import datetime

app = FastAPI()

############################################################################################
# LOGGING
############################################################################################
# Create and configure logger
logging.basicConfig(filename="./INGEST.log",
                    format='"INGEST" %(asctime)s %(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)

############################################################################################
# DATA DETAILS
############################################################################################

#{"version":"1.0.0",

#"metadata-list":{"correlation-id":"ff561bdb-112f-4799-b872-c066a12bd1b8","producer-fqdn":"10.251.74.72",
#"hop-by-hop-id":"1","timestamp":"1678705695995010066","message-direction":"REQUEST_INGRESS",

#"feed-source":{"nf-type":"SCP","nf-fqdn":"scp901xwp.5gc.mnc030.mcc234.3gppnetwork.org","nf-instance-id":"c7c359b2-01ad-44c0-9ab3-0610a42683bc",
#"pod-instance-id":"scp901xwp-scp-worker-6cfbdbf84-6wtgk"}},

#"header-list":{"host":["10.251.11.99:8000"],"x-http2-scheme":["http"],"3gpp-sbi-target-apiroot":["http://10.251.74.72:8080"],
#"content-type":["application/json"],"user-agent":["AUSF-auth"],"content-length":["113"],"x-http2-stream-id":["3"],":scheme":["http"],
#":authority":["10.251.11.99:8000"],":path":["/nudm-ueau/v1/suci-0-234-30-0-0-0-9000014975/security-information/generate-auth-data"],
#":method":["POST"]},

############################################################################################
# CLASS 
############################################################################################

#"5g-sbi-message":"{\"ausfInstanceId\":\"4178a864-7b8b-49f6-82c6-323d0a81a8ff\",\"servingNetworkName\":\"5G:mnc030.mcc234.3gppnetwork.org\"}"}

#class DDItems(BaseModel):
#    'metadata-list': Metadata
#    "feed-source": Feed
#    "header-list": Header
#    "5g-sbi-message": Message

class DDItems(BaseModel):
    metadata_list: Any = Field(alias="metadata-list")
    #feed_source: Any = Field(alias="feed-source")
    header_list: Any = Field(alias="header-list")
    g_sbi_message: Any = Field(alias="5g-sbi-message")
############################################################################################
# SSS
############################################################################################
metadata = {
    'testapi': ["/test"],
    'kafkaapi': ["/callproducer"],
    'instruction': "DO NOT USE WITHOUT FULL UNDERSTANDING",
    'author': "SSS"}

def process_string(json_as_string): 
    logging.info(type(json_as_string))
    json_object = json.loads(json_as_string)
    MSG_DIR_VAL=str(json_object["metadata-list"]["message-direction"])
    AUTH_VAL=str(json_object["header-list"][":authority"][0])
    PATH_VAL=str(json_object["header-list"][":path"][0])
    METHOD_VAL=str(json_object["header-list"][":method"][0])
    DB_NAME='test'
    TBL_NAME='test_tbl'
    sqlcmd="INSERT INTO  "+DB_NAME+"."+TBL_NAME+" (FlowID, MSG_DIR, AUTHORITY, PATH, METHOD) \
                  VALUES (NULL, '"+MSG_DIR_VAL+"', '"+AUTH_VAL+"', '"+PATH_VAL+"', '"+METHOD_VAL+"')"
    sqldict={'MSG_DIR': MSG_DIR_VAL, 'AUTHORITY': AUTH_VAL, 'PATH': PATH_VAL, 'METHOD': METHOD_VAL}
    return sqlcmd, sqldict


@app.get("/")
async def root():
    return {"ABOUT": metadata}

@app.post("/testnodata")
async def test_nodata():
    print('MESSAGE RECEIVED')
    try:
        return {"status":"success"}
    except ValueError:
        return {"status":"failure"}

@app.post("/test1")
async def test_data(test: str):
    print('MESSAGE RECEIVED')
    try:
        print(test)
        return {"status":"success"}
    except ValueError:
        return {"status":"failure"}

@app.post("/test2")
async def test_data(body: Dict):
    print('MESSAGE RECEIVED')
    try:
        print(body)
        return {"status":"success"}
    except ValueError:
        return {"status":"failure"}

@app.post("/callproducer")
async def post_dd_data(item: DDItems):
    logging.info('MESSAGE RECEIVED callproducer')
    #return {"status":"success"}
    try:
        json_of_item = jsonable_encoder(item)
        json_as_string = json.dumps(json_of_item)
        #print(json_as_string)
        # CALL PRODUCER KAFKA FUNCTION
        sqlcmd, rr1_dict=process_string(json_as_string)
        rr1_json=json.dumps(rr1_dict)
        USERNAME='root'
        PASSWORD='root'
        MYSQLIP='172.17.0.1'
        MYSQLPORT='3306'
        eng, conn = mysqldb.conn_setup(USERNAME,PASSWORD,MYSQLIP,MYSQLPORT)
        logging.info("CONNECTION ESTABLISHED")
        sql_create_table="CREATE TABLE IF NOT EXISTS test_tbl (\
        FlowID int NOT NULL AUTO_INCREMENT, MSG_DIR varchar(255) NOT NULL, AUTHORITY varchar(255) NOT NULL,\
        PATH varchar(255), METHOD varchar(255), PRIMARY KEY (FlowID));"
        p1, rowid = mysqldb.sql_cmd(conn, sql_create_table)
        logging.info("TABLE EXECUTED")
        logging.info("ROWID: ", rowid)
        p2, lastrowid = mysqldb.sql_cmd(conn, sqlcmd)
        logging.info("SQLCMD EXECUTED")
        logging.info("LASTROWID: ", lastrowid)
        conn.close()
        eng.dispose()
        #return JSONResponse(content=json_of_item, status_code=201)
        return JSONResponse(content=rr1_json, status_code=201)
        #return JSONResponse(status_code=201)
    except ValueError:
        return JSONResponse(content=jsonable_encoder(item), status_code=400)
@app.post("/get_fetch_data")
async def get_fetch_data():
    logging.info('MESSAGE RECEIVED get_fetch_data')
    #return {"status":"success"}
    try:
        selectsqlcmd="select * from test.test_tbl;"
        USERNAME='root'
        PASSWORD='root'
        MYSQLIP='172.17.0.1'
        MYSQLPORT='3306'
        eng, conn = mysqldb.conn_setup(USERNAME,PASSWORD,MYSQLIP,MYSQLPORT)
        logging.info("CONNECTION ESTABLISHED")
        r1, rid1 = mysqldb.sql_cmd(conn, selectsqlcmd)
        logging.info("SELECTSQLCMD EXECUTED")
        logging.info(r1)
        conn.close()
        eng.dispose()
        # result to dict
        r1_dict = r1.mappings().all()
        logging.info(r1_dict)
        r1_json=json.dumps(r1_dict)
        return JSONResponse(content=r1_json, status_code=201)
        #return JSONResponse(content=item, status_code=201)
        #return JSONResponse(status_code=201)
    except ValueError:
        #return JSONResponse(content=jsonable_encoder(item), status_code=400)
        return JSONResponse(status_code=400)



