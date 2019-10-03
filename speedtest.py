#!/usr/bin/env python

#Script to test speed of reading.


import time
from mpu6050 import mpu6050
import numpy as np

mpu = mpu6050(0x68)
mpu.set_accel_range(16)

def calibrate(caltime):
    stop = time.time()+caltime
    d = mpu.get_accel_data()
    a = np.array([d['x'], d['y'], d['z']])
    while time.time() < stop:
        d = mpu.get_accel_data()
        a = np.vstack([a, [d['x'], d['y'], d['z']]])
    return np.mean(a, axis=0)

calibrate(1)

#Make LED Blink
# echo heartbeat | sudo tee /sys/class/leds/led0/trigger >/dev/null

#Return LED to normal function
# echo mmc0 | sudo tee /sys/class/leds/led0/trigger >/dev/null

rec_duration = 10   # seconds

datapoints = int(rec_duration/.001)

# d = mpu.get_accel_data()
# a = np.array([time.time(), d['x'], d['y'], d['z']])
# for _ in range(datapoints):
#     d = mpu.get_accel_data()
#     a = np.vstack([a, [time.time(), d['x'], d['y'], d['z']]])
# print('Runtime: {}'.format(a[-1,0]-a[0,0]))
# print('Avg Time Slice: {}'.format((a[-1,0]-a[0,0])/datapoints))


a = np.zeros((datapoints, 4))
for i in range(datapoints):
    d = mpu.get_accel_data()
    a[i] = [time.time(), d['x'], d['y'], d['z']]
print('Runtime: {}'.format(a[-1,0]-a[0,0]))
print('Avg Time Slice: {}'.format((a[-1,0]-a[0,0])/datapoints))

namestr = 'output-{}.txt.gz'.format(time.strftime('%Y_%m_%d-%H_%M_%S'))
np.savetxt(namestr, a, delimiter=',', fmt='%1.5e')