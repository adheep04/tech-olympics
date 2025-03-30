# inconsistent behavior 
from threading import Thread

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

threads = [Thread(target=increment) for _ in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)  
