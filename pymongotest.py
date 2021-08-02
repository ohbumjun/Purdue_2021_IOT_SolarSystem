import pymongo
from pymongo import MongoClient
import certifi
import time
import datetime
import random

ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://lee:mineral911@cluster0.kii4s.mongodb.net/test?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.test
collection = db["todos"]

# print(db.list_collection_names())


# Temperature Range: 0°C to 50°C
# Humidity Range: 20% to 90%
# Resolution: Temperature and Humidity both are 16-bit
# Accuracy: ±1°C and ±1%

TEMP_MIN = 0.0
TEMP_MAX = 50.0
HUM_MIN = 20.0
HUM_MAX = 90.0

curTemp = float(random.randrange(TEMP_MIN, TEMP_MAX))
curHum = float(random.randrange(HUM_MIN, HUM_MAX))


# Simulating current temperature and humidity and showing them every 10 seconds
while True:
    temperature = float(curTemp*(1 + random.randrange(-1, 2)/100))
    humidity = float(curHum*(1 + random.randrange(-1, 2)/100))
    print("Temperature: {} C\tHumidity: {} %".format(temperature, humidity))
    post = {"time": str(datetime.datetime.now()), "temperature": temperature, "humidity": humidity, "error": False}
    collection.insert_one(post)
    time.sleep(60)
    