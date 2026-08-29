import tkinter as tk

window = tk.Tk()

window.title("My Python App")#---------Title--------------------------
window.geometry("500x300")#--------------Window size-------------------------



label = tk.Label(window, text="Hello Python")#------------------------Label--------------
label.pack()


button=tk.Button(window,text="click Me!")
button.pack()

entry=tk.Entry(window)
entry.pack()

window.mainloop()