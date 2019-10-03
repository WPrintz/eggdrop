#!/usr/bin/env python

#Script to test speed of reading.

# import sys
# print(sys.path)
# ipypaths = ['/home/pi/.local/bin', '/usr/lib/python37.zip', '/usr/lib/python3.7', '/usr/lib/python3.7/lib-dynload', '', '/home/pi/.local/lib/python3.7/site-packages', '/usr/local/lib/python3.7/dist-packages', '/usr/lib/python3/dist-packages', '/home/pi/.local/lib/python3.7/site-packages/IPython/extensions', '/home/pi/.ipython']
# sys.path.append('/usr/local/lib/python3.7/dist-packages')
# sys.path.append('/usr/lib/python3/dist-packages')
# print(sys.path)

import time
from mpu6050 import mpu6050
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# from matplotlib.figure import Figure


mpu = mpu6050(0x68)
mpu.set_accel_range(24)  #Acceptable  values: 0, 8, 16, 24

# def calibrate(caltime):
#     stop = time.time()+caltime
#     d = mpu.get_accel_data()
#     a = np.array([d['x'], d['y'], d['z']])
#     while time.time() < stop:
#         d = mpu.get_accel_data()
#         a = np.vstack([a, [d['x'], d['y'], d['z']]])
#     return np.mean(a, axis=0)

# cal = calibrate(1)


def print_figure(a, namestr):
#     ax = fig.subplots()
    begin = 0       #Starting time step
    end = len(a)    #Number of steps from begin
#     end = 2000
    timeseries = range(begin, end)

    fig, ax = plt.subplots(figsize=(12,6))
    line0, = ax.plot([timeseries[0], timeseries[-1]], [0,0], '--k', alpha=0.25)
    line1, = ax.plot(timeseries, a[begin:end,1])
    line2, = ax.plot(timeseries, a[begin:end,2])
    line3, = ax.plot(timeseries, a[begin:end,3])
    line4, = ax.plot(timeseries, np.sqrt(np.sum(np.square(a[begin:end,1:4]), axis=1))-1, '--k')


    ax.set_xlabel('Time')
    ax.set_ylabel('Acceleration')
    ax.legend(['X', 'Y', 'Z'], loc='upper right')
    fig.savefig(namestr+'.png', dpi=150)
    return None

    

#Make LED on or off
ledblinkon = 'echo heartbeat | sudo tee /sys/class/leds/led0/trigger >/dev/null'
ledsolidon = 'echo 1 | sudo tee /sys/class/leds/led0/brightness >/dev/null'
ledsolidoff = 'echo 0 | sudo tee /sys/class/leds/led0/brightness >/dev/null'

#Turn on and off LED control
lednorm = 'echo mmc0 | sudo tee /sys/class/leds/led0/trigger >/dev/null'
ledoff = 'echo none | sudo tee /sys/class/leds/led0/trigger >/dev/null'


def cal_clock(rec_duration):
    a = np.zeros((2000, 4))
    for i in range(2000):
        t, d = time.clock(), mpu.get_accel_data(g = True)
        a[i] = [t, d['x'], d['y'], d['z']]
    return int(rec_duration/((a[-1,0]-a[0,0])/len(a)))

def main(datapoints):
    os.system(ledoff)
    os.system(ledsolidon)

    a = np.zeros((datapoints, 4))
    for i in range(datapoints):
        t, d = time.clock(), mpu.get_accel_data(g = True)
        a[i] = [t, d['x'], d['y'], d['z']]
    print('Runtime: {}'.format(a[-1,0]-a[0,0]))
    differ = np.diff(a[:,0])
    print('Time Slice Avg, Max, Min: {} {} {}'.format((a[-1,0]-a[0,0])/datapoints, max(differ), min(differ)))

    os.system(ledsolidoff)
    os.system(lednorm)

    namestr = 'output-{}'.format(time.strftime('%Y_%m_%d-%H_%M_%S'))

    np.savetxt(namestr+'.txt.gz', a, delimiter=',', fmt='%1.9e')
    print('Data file saved: {}'.format(namestr))

    print_figure(a, namestr)

if __name__ == "__main__":
#     datapoints = cal_clock(3)
#     print(datapoints)
    main(6000)