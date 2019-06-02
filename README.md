**Sunny Rasp**

Basic python script designed to capture light sensor data and append it to a CSV. Designed to be used with crontab or some other scheduler.

**Installation**

Requires that Python 2 is installed.

 1. Check out git repository code
 2. Navigate into ./Adafruit_Python_PureIO directory and execute: `sudo python setup.py install`
 3. Test sensor data collection with script ./SDL_Pi_SI1145/simpletest.py

**Configuration**

Once executed, the main.py script will append to a CSV file stored at the location set in the `CSV_FILENAME` variable. The default location is into a file named `readings.swap.csv` in the same directory as the main.py script.

**Crontab Configuration**

A Python shebang is included at the top of the main file, so simply adding a crontab entry similar to the one below should be all that is required:

    */4 * * * * /home/pi/Documents/dev/sunny-rasp/main.py

**Misc**

Here is a blog post I wrote about the project, and provides links to the sensor and connectors used: https://taylor.callsen.me/the-smart-shoe-a-raspberry-pi-sunlight-sensor/