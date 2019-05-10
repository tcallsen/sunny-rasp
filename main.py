#
# imports
#

import sys

# configure python to search libraries
#   https://www.johnny-lin.com/cdat_tips/tips_pylang/path.html
sys.path.append('./SDL_Pi_SI1145');

import csv
import time
import SDL_Pi_SI1145

#
# confiugration parameters
#

CSV_FILENAME = "readings.swap.csv"

#
# start main script logic
#

# 1) take sensor readings
sensor = SDL_Pi_SI1145.SDL_Pi_SI1145()
vis = sensor.readVisible()
IR = sensor.readIR()
UV = sensor.readUV() / 100.0

# 2) capture date and timezone in ISO 8601 format
#   https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python
t = time.localtime(time.time())
formatted = time.strftime('%Y-%m-%dT%H:%M:%S', t)
tz = str.format('{0:+06.2f}', float(time.timezone) / -3600)
renderedDate = formatted + tz

# 2) append sensor readings to csv file
with open(CSV_FILENAME,'a+') as csv_file:
  csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  csv_writer.writerow([ renderedDate , vis , IR , UV ])