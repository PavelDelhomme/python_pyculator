import tkinter as tk

from pyculator import PyCalculator

if __name__ == '__main__':
    root = tk.Tk()
    calculator = PyCalculator(root)
    root.mainloop()