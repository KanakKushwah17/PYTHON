import winsound



import tkinter as tk
import winsound

window = tk.Tk()

def success():
    winsound.Beep(1200, 300)

button = tk.Button(
    window,
    text="Click Me",
    command=success
)

button.pack()

window.mainloop()