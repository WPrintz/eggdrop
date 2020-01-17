import numpy as np
import matplotlib.pyplot as plt
from time import sleep

def collectdata(filename):
    x = np.linspace(1,6,50)
    y = np.sin(x)
    z = np.asarray([x,y])
    np.savetxt('./static/data/{}.txt.gz'.format(filename), z, delimiter=',')
    sleep(5)

def saveimage(name, filename):
    plt.switch_backend('Agg')
    a = np.loadtxt('./static/data/{}.txt.gz'.format(filename), delimiter=',')
    fig = plt.figure(figsize=(12,6))
    plt.plot(a[0],a[1])
    plt.xlabel('Time')
    plt.ylabel('Acceleration')
    plt.legend(['X', 'Y'])
    plt.savefig('./static/data/{}.png'.format(filename), dpi=150)

if __name__ == '__main__':
    makedata('test')
    saveimage('test')
