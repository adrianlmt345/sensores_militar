# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:51:18 2022

@author: precision
"""

# March 2020
#
from __future__ import print_function
# Python imports
import http.client
import time
import urllib


# API KEY
THINGSPEAK_APIKEY = 'Z0KZ88519FYD74YY'
print("Welcome to the ThingSpeak Raspberry Pi temperature sensor! Press CTRL+C to stop.")
try:
  while 1:
     # Get temperature in Celsius
     temp_c = ((500 * 3.30) - 0.5) * 10
     # Calculate temperature in Fahrenheit
     temp_f = (temp_c * 9.0 / 5.0) + 32.0
     # Display the results for diagnostics
     print("Uploading {0:.2f} C, {1:.2f} F" "".format(temp_c, temp_f), end=' ... ')
     # Setup the data to send in a JSON (dictionary)
     params = urllib.parse.urlencode(
          {
             'field1': temp_c,
             'field2': temp_f,
             'key': THINGSPEAK_APIKEY,
          }
     )
     # Create the header
     headers = { "Content-type": "application/x-www-form-urlencoded", 'Accept': "text/plain"}
     # Create a connection over HTTP
     conn = http.client.HTTPConnection("api.thingspeak.com:80")
     try:
         # Execute the post (or update) request to upload the data
         conn.request("POST", "/update", params, headers)
         # Check response from server (200 is success)
         response = conn.getresponse()
         # Display response (should be 200)
         print("Response: {0} {1}".format(response.status,response.reason))
         # Read the data for diagnostics
         data = response.read()
         conn.close()
     except Exception as err:
         print("WARNING: ThingSpeak connection failed: {0}, " "data: {1}".format(err, data))
     # Sleep for 20 seconds
     time.sleep(20)
except KeyboardInterrupt:
     print("Thanks, bye!")
exit(0)