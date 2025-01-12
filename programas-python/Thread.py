import threading

lock = threading.Lock()

def worker(a,b):
    lock.acquire()
    for i in range(20):
        print("worker", a,b,i)
    lock.relase()

threads = []
for i in range(10):
    t = threading.Thread(target=worker, args=(i,i+5))
    threads.append(t)
    t.start()

for i in range(10):
    print("esperando por ", i)
    t = threads[i]
    t.join()