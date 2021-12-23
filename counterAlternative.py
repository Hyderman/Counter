from queue import Queue, Empty
from threading import Thread, Event
import tkinter as tk
from time import sleep
 
def counter(queue, done):
    count = 0
    while not done.is_set():
        count += 1
        queue.put(count)
        sleep(1)
     
def do_update(label, queue, delay=200):
    try:
        n = queue.get(False)
    except Empty:
        pass
    else:
        label['text'] = n
    finally:
        label.after(delay, do_update, label, queue)
 
 
if __name__ == '__main__':
 
    root = tk.Tk()
    label = tk.Label(root)
    label.pack()
    queue = Queue()
    done = Event()
    th = Thread(target=counter, args=(queue, done))
    th.start()
    do_update(label, queue)
    tk.mainloop()
    done.set()
    th.join()