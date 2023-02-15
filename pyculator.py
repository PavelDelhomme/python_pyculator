import tkinter as tk


class PyCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculatrice")
        master.resizable(False, False)

        # Couleurs
        button_color = "#aeaeae"
        button_active_color = "#cbcbcb"
        display_color = "#ffffff"
        display_active_color = "#f0f0f0"
        border_color = "#dfdfdf"

        # Affichage
        self.display = tk.Entry(master, width=30, font=('Arial', 16), bd=0, justify='right', bg=display_color,
                                highlightthickness=1, highlightbackground=border_color,
                                highlightcolor=display_active_color)
        self.display.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky='nsew')
        self.display.insert(0, "0")

        # Boutons
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '±',
            '1', '2', '3', '-', 'x²',
            '0', '.', '=', '+', '√'
        ]

        # Création des boutons
        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.click(x)
            tk.Button(master, text=button, width=5, height=2, bg=button_color, activebackground=button_active_color,
                      relief='flat', command=command).grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Ajouter un bouton pour quitter l'application
        tk.Button(master, text="Quitter", width=8, height=2, bg=button_color, activebackground=button_active_color,
                  relief='flat', command=master.quit).grid(row=5, column=4, padx=5, pady=5, sticky='nsew')

        # Appliquer un padding uniforme aux boutons et aux cellules de la grille
        for i in range(5):
            master.columnconfigure(i, weight=1)
        for i in range(6):
            master.rowconfigure(i, weight=1)

    def click(self, key):
        if key == '=':
            # Calculer le résultat
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Erreur")
        elif key == 'C':
            # Effacer le champ de saisie
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
        elif key == '±':
            # Changer le signe du nombre affiché
            value = self.display.get()
            if value and value[0] == '-':
                self.display.delete(0)
            else:
                self.display.insert(0, '-')
        elif key == 'x²':
            # Calculer le carré du nombre affiché
            try:
                value = float(self.display.get())
                result = value ** 2
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Erreur")
        elif key == '√':
            # Calculer la racine carrée du nombre affiché
            try:
                value = float(self.display.get())
                result = value ** 0.5
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Erreur")
        else:
            # Ajouter la touche appuyée au champ de saisie
            if self.display.get() == "0":
                self.display.delete(0)
            self.display.insert(tk.END, key)


if __name__ == '__main__':
    root = tk.Tk()
    calculator = PyCalculator(root)
    root.mainloop()
