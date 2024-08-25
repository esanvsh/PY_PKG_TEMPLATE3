
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
    feed_source: Any = Field(alias="feed-source")
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
    return json_as_string


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
        process_string(json_as_string)
        return JSONResponse(content=json_of_item, status_code=201)
        #return JSONResponse(content=item, status_code=201)
        #return JSONResponse(status_code=201)
    except ValueError:
        return JSONResponse(content=jsonable_encoder(item), status_code=400)



