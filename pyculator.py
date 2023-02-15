import tkinter as tk
from tkinter import ttk


class PyCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculatrice")
        master.resizable(False, False)

        # Couleurs
        background_color = "#343434"
        button_color = "#333333"
        button_active_color = "#666666"
        display_color = "#6d6d6d"
        display_active_color = "#6e6e6e"
        border_color = "#808080"
        font_color = "#ffffff"
        font_active_color = "#f2f2f2"

        # Affichage
        style = ttk.Style()
        style.configure('TEntry', background=display_color, fieldbackground=display_color, foreground=font_color,
                        insertbackground=font_color, highlightthickness=1, highlightbackground=border_color,
                        highlightcolor=display_active_color, relief='flat', borderwidth=0, font=('Arial', 16))
        self.display = ttk.Entry(master, width=30, style='TEntry')
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
            ttk.Button(master, text=button, width=5, style='TButton', command=command).grid(row=row, column=col, padx=5,
                                                                                            pady=5, sticky='nsew')
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Ajouter un bouton pour quitter l'application
        ttk.Button(master, text="Quitter", width=8, style='TButton', command=master.quit).grid(row=5, column=4, padx=5,
                                                                                               pady=5, sticky='nsew')

        # Appliquer un padding uniforme aux boutons et aux cellules de la grille
        for i in range(5):
            master.columnconfigure(i, weight=1)
        for i in range(6):
            master.rowconfigure(i, weight=1)

        # Lier les touches du clavier aux boutons
        master.bind("<Key>", self.keypress)

        # Changer le style de l'application
        style.theme_use('clam')
        style.configure('.', background=background_color)
        style.configure('TButton', background=button_color, foreground=font_color, activebackground=button_active_color,
                        activeforeground=font_active_color, borderwidth=0, font=('Arial', 12), padding=5)
        style.map('TButton', background=[('active', button_active_color), ('pressed', button_color)])
        style.configure('TLabel', background=background_color, foreground=font_color, font=('Arial', 12), padding=5)

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

    def keypress(self, event):
        key = event.char
        if key == '\r':
            key = '='
        elif key == '\x08':
            key = 'C'
        elif key == '\x1b':
            self.master.quit()
        elif key == '+':
            key = '+'
        elif key == '-':
            key = '-'
        elif key == '*':
            key = '*'
        elif key == '/':
            key = '/'
        elif key == '.':
            key = '.'
        elif key == '0':
            key = '0'
        elif key == '1':
            key = '1'
        elif key == '2':
            key = '2'
        elif key == '3':
            key = '3'
        elif key == '4':
            key = '4'
        elif key == '5':
            key = '5'
        elif key == '6':
            key = '6'
        elif key == '7':
            key = '7'
        elif key == '8':
            key = '8'
        elif key == '9':
            key = '9'
        elif key == '\x16':
            key = 'x²'
        elif key == '\x1a':
            key = '√'
        else:
            key = ''
        if key:
            self.click(key)
