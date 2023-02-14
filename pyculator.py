import tkinter as tk


# todo make better UI
class PyCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculatrice")

        # Entry and display system
        self.display = tk.Entry(master, width=30, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Buttons
        btns = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            ".", "0", "=", "+"
        ]

        # Buttons creation

        row = 1
        col = 0
        for btn in btns:
            command = lambda x=btn: self.click(x)
            tk.Button(master, text=btn, width=5, height=2, command=command).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            print(col)
            if col > 3:
                col = 0
                row += 1

    def click(self, key):
        if key == "=":
            # Result
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        elif key == 'C':
            # Canceled
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, key)
