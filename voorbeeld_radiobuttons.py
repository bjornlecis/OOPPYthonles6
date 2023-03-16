import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter StringVar')
        self.geometry("500x350")
        self.aantal_personen_var = tk.StringVar()
        self.keuze_activiteit = tk.IntVar()


        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):

        padding = {'padx': 5, 'pady': 5}
        # label
        ttk.Label(self, text='Aantal personen:').grid(column=0, row=0, **padding)


        # Entry
        getal1 = ttk.Entry(self, textvariable=self.aantal_personen_var)
        getal1.grid(column=1, row=0, **padding)
        getal1.focus()


        #Radio buttons
        r1 = tk.Radiobutton(self, text="Bowlen", var=self.keuze_activiteit,value=1).grid(row=1,column=0)
        r2 = tk.Radiobutton(self, text="Paintballen", var=self.keuze_activiteit,value=2).grid(row=2,column=0)
        r3 = tk.Radiobutton(self, text="Snowboarden", var=self.keuze_activiteit,value=3).grid(row=3,column=0)


        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=2, row=0, **padding)

        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=4, columnspan=3, **padding)



    def submit(self):
        prijs = 0
        if self.keuze_activiteit.get() == 1:
            prijs = int(self.aantal_personen_var.get())*7
        elif self.keuze_activiteit.get() == 2:
            prijs = int(self.aantal_personen_var.get())*18
        elif self.keuze_activiteit.get() == 3:
            prijs = int(self.aantal_personen_var.get())*21
        else:
            print("prijs kan niet gehaald worden")

        res = f"De prijs bedraagt € {prijs}"
        self.output_label.config(text=res)
        self.output_label.configure(background="Cyan")
        self.output_label.configure(foreground="Orange",font=("Arial",24))





if __name__ == "__main__":
    app = App()
    app.mainloop()
