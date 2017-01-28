import threading, time, random

def worker(num):
    """thread worker function"""
    print 'Worker: %s' % num
    return

threads = []
for i in range(20):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()