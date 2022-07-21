import tkinter as tk
import threading

class Message(threading.Thread):
    
    def __init__(self, message, police="Courier", size=30, foreground='black', time=5000):
        threading.Thread.__init__(self)
        self.message = message
        self.police = police
        self.size = size
        self.foreground = foreground
        self.time = time
        
    def run(self):
        self.window = tk.Tk()
        self.window.title("Message information")
        l = tk.Label(self.window, text=self.message)
        l.config(font=(self.police, self.size), fg=self.foreground)
        l.pack()
        self.window.after(self.time,self.window.destroy) # Ferme la fenêtre au bout de 2s
        self.window.mainloop()

