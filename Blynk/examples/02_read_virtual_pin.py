"""
[READ VIRTUAL PIN EXAMPLE] ========================================================================

Environment prepare:
In your Blynk App project:
  - add "Value Display" widget,
  - bind it to Virtual Pin V11,
  - set values range 0-255
  - set the read frequency to 5 second.
  - optionally to have more visibility you can add "LED" widget and assign Virtual Pin V11 to it
  - Run the App (green triangle in the upper right corner).
  - define your auth token for current example and run it


This started program will periodically call and execute event handler "read_virtual_pin_handler".
Calling virtual_write operation inside handler updates widget value.
In app you can see updated values and optionally LED brightness change.

Schema:
=====================================================================================================
            +-----------+                        +--------------+                    +--------------+
            |           |                        |              |                    |              |
            | blynk lib |                        | blynk server |                    |  blynk app   |
            |           |                        |  virtual pin |                    |              |
            |           |                        |              |                    |              |
            +-----------+                        +--------------+                    +--------------+
                  |                                     |                                    |
                  |                                     |                                    |
                  |                                     |  widget read frequency = 5 sec     |
                  |                                     +<-----------------------------------+
                  |                                     |                                    |
                  |                                     |                                    |
                  |                                     |  send virtual pin value to widget  |
                  |                                     |                                    |
   event handler  |    read event to hw from server     +----------------------------------->+
  (user function) |                                     |                                    |
       +-----------<------------------------------------+                                    |
       |          |                                     |                                    |
       |          |   write random 0-255 value to pin   |                                    |
       +--------->------------------------------------->+         next widget read event     |
                  |                                     |                                    |
                  |                                     +<-----------------------------------+
                  |                                     |                                    |
                  |                                     |                                    |
                  +                                     +                                    +

====================================================================================================
Additional info about blynk you can find by examining such resources:

    Downloads, docs, tutorials:     https://blynk.io
    Sketch generator:               http://examples.blynk.cc
    Blynk community:                http://community.blynk.cc
    Social networks:                http://www.fb.com/blynkapp
                                    http://twitter.com/blynk_app
=====================================================================================================
"""

import blynklib
import random

BLYNK_AUTH = 'ZYfkIz9weN7YQ39yJufd9bPjLCa_i4ZQ'

# initialize blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"



    
    # register handler for virtual pin V0 ading
#CO2 level
@blynk.handle_event('read V0')
def read_virtual_pin_handler(pin):
    print(READ_PRINT_MSG.format(pin))
    blynk.virtual_write(pin,random.uniform(0.0,10.0))

    # register handler for virtual pin V1 reading
#CO level

   

    # Streetlight status
@blynk.handle_event('read V2')
def read_virtual_pin_handler(pin):
    print(READ_PRINT_MSG.format(pin))
    blynk.virtual_write(pin,random.randint(0,2))
    

   # Garbage filled status
@blynk.handle_event('read V3')
def read_virtual_pin_handler(pin):
    print(READ_PRINT_MSG.format(pin))
    blynk.virtual_write(pin,random.randint(0,1))
###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()
