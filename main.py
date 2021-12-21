import queue
from threading import Thread
import tkinter as tk
from time import sleep


class Counter(tk.Tk):
    def __init__(self, queue, font="Courier", size=1000, foreground="green"):
        super().__init__()
        self.attributes('-fullscreen', True)
        self.queue = queue
        self.data = self.queue.get()
        self.font = font
        self.size = size
        self.foreground = foreground
        self.l = tk.Label(self, text=self.data)
        self.l.config(font=(self.font, self.size), fg=self.foreground)
        self.l.pack()
        
    def getNumber(self):
        self.data = self.queue.get()
        print(self.data)
        self.l.configure(text=self.data)
        self.l.after(500, self.getNumber)
            
        
class ThreadCounter(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        self.root = Counter(self.queue) # create my tkinter object
        self.root.after(500, self.root.getNumber) # Find value in the main thread
        self.root.mainloop()
        
q = queue.Queue()
cnt = 0
q.put(cnt)
threadCounter = ThreadCounter(q)
threadCounter.start()
while True:
    sleep(2)
    cnt += 1
    q.put(cnt)