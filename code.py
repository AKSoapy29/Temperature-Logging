print("Running script")

DB_IP = '1.2.3.4'
DB_PORT = 8086
DB_USER = 'pi'
DB_PASS = 'raspberry'
DB_NAME = 'database'

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
POLL_FREQUENCY = 10 # Number of seconds to wait before grabbing and uploading data

import os
import time
import Adafruit_DHT
from influxdb import InfluxDBClient
from datetime import datetime

client = InfluxDBClient(DB_IP, DB_PORT, DB_USER, DB_PASS, DB_NAME)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR. DHT_PIN)

    if humidity is not None and temperature is not None:
        temp = (temperature * 9/5) + 32
        current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        json_body = [{
            "measurement": "state",
            "time": current_time,
            "fields": {
                "temperature": temp,
                "humidity": humidity
            }
        }]

        print("Temp={0:0.1f}*F  Humidity={1:0.1f}%".format(temp, humidity))

        client.write_points(json.body)

    else:
        print("Failed to retrieve data from humidity sensor")
    
    time.sleep(POLL_FREQUENCY) # Wait ten seconds