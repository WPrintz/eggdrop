import time

def get():
    t, s = time.time(), time.asctime(time.localtime())
    return t, s
