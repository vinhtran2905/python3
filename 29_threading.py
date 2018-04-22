import threading
#inheritance class Thread
class messenger(threading.Thread):
    def run(self):
        #_ dont care the variable, just make a loop 10 times
        for _ in range(10):
            print(threading.current_thread().getName())

x = messenger(name='Send out messages')

y = messenger(name='receive messages')

x.start()
y.start()
