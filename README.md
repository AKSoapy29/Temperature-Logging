# Temperature-Logging
This repository is to collect data from the DHT22/AM2302 temperature and humidity sensor connected to a Raspberry Pi Zero, then store the data in an InfluxDB database to be later used with Grafana

# Installing dependencies
pip3 install influxdb
pip3 install Adafruit-DHT

# Running the script
python3 code.py

# Running at boot
To run this code on boot, make sure you do this:
Put the code somewhere in /bin (Can be in its own folder): sudo cp -i /path/to/your_script.py /bin
Add a new cron job: sudo crontab -e
At the bottom, add your script: @reboot python3 /bin/code.py &
Reboot: sudo reboot