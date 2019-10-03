#!/usr/bin/env python

#Script to test speed of reading.

# import sys
# sys.path.append('/usr/local/lib/python3.7/dist-packages')

import time
from mpu6050 import mpu6050
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# from matplotlib.figure import Figure


mpu = mpu6050(0x68)
mpu.set_accel_range(8)

def calibrate(caltime):
    stop = time.time()+caltime
    d = mpu.get_accel_data()
    a = np.array([d['x'], d['y'], d['z']])
    while time.time() < stop:
        d = mpu.get_accel_data()
        a = np.vstack([a, [d['x'], d['y'], d['z']]])
    return np.mean(a, axis=0)

calibrate(1)


def print_figure(a):
#     ax = fig.subplots()
    begin = 0       #Starting time step
    end = len(a)    #Number of steps from begin
#     end = 2000
    timeseries = range(begin, end)

    fig, ax = plt.subplots(figsize=(12,6))
#     fig.figure(figsize=(12,6))
    line1, = ax.plot(timeseries, a[begin:end,1])
    line2, = ax.plot(timeseries, a[begin:end,2])
    line3, = ax.plot(timeseries, a[begin:end,3])
    
#     plt.plot(timeseries, np.max(np.abs(a[begin:end,1:4]), axis=1), '--r')
    line4, = ax.plot(timeseries, np.sqrt(np.sum(np.square(a[begin:end,1:4]), axis=1))-9.80665, '--k')


    ax.set_xlabel('Time')
    ax.set_ylabel('Acceleration')
    ax.legend(['X', 'Y', 'Z'], loc='upper right')
    fig.savefig('testfig.png', dpi=150)
    return None

    

#Make LED on or off
ledblinkon = 'echo heartbeat | sudo tee /sys/class/leds/led0/trigger >/dev/null'
ledsolidon = 'echo 1 | sudo tee /sys/class/leds/led0/brightness >/dev/null'
ledsolidoff = 'echo 0 | sudo tee /sys/class/leds/led0/brightness >/dev/null'

#Turn on and off LED control
lednorm = 'echo mmc0 | sudo tee /sys/class/leds/led0/trigger >/dev/null'
ledoff = 'echo none | sudo tee /sys/class/leds/led0/trigger >/dev/null'


os.system(ledoff)
os.system(ledsolidon)

rec_duration = 2   # seconds

datapoints = int(rec_duration/.001)

a = np.zeros((datapoints, 4))
for i in range(datapoints):
    d = mpu.get_accel_data()
    a[i] = [time.time(), d['x'], d['y'], d['z']]
print('Runtime: {}'.format(a[-1,0]-a[0,0]))
print('Avg Time Slice: {}'.format((a[-1,0]-a[0,0])/datapoints))

os.system(ledsolidoff)
os.system(lednorm)

namestr = 'output-{}.txt.gz'.format(time.strftime('%Y_%m_%d-%H_%M_%S'))

# np.savetxt(namestr, a, delimiter=',', fmt='%1.5e')

print_figure(a)