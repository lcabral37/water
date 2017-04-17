#!/usr/bin/env python
from time import sleep
from common import Water

water = Water()
water.on()
print("Water is on...")
print("Waiting " +  str(water.time) + "s")
sleep(water.time)
water.off()
print("Water is off!")
