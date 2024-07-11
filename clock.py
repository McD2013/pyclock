import tkinter as tk
import time

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("400x200")
        self.root.configure(bg='black')
        
        self.time_label = tk.Label(self.root, font=("Helvetica", 48), bg="black", fg="cyan")
        self.date_label = tk.Label(self.root, font=("Helvetica", 24), bg="black", fg="lightgreen")
        
        self.time_label.pack(pady=20)
        self.date_label.pack()
        
        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%A, %d %B %Y")
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()
