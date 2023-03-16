import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter StringVar')
        self.geometry("300x150")
        self.configure(bg="Blue")
        self.getal1_var = tk.StringVar()
        self.getal2_var = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):

        padding = {'padx': 5, 'pady': 5}
        # label
        ttk.Label(self, text='Getal 1:').grid(column=0, row=0, **padding)
        ttk.Label(self, text='Getal 2:').grid(column=0, row=1, **padding)

        # Entry
        getal1 = ttk.Entry(self, textvariable=self.getal1_var)
        getal1.grid(column=1, row=0, **padding)
        getal1.focus()

        getal2 = ttk.Entry(self, textvariable=self.getal2_var)
        getal2.grid(column=1, row=1, **padding)

        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=2, row=0, **padding)

        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=3, columnspan=3, **padding)



    def submit(self):
        som = int(self.getal1_var.get())+int(self.getal2_var.get())
        res = f"De uitkomst is: {str(som)}"
        self.config(bg="Red")
        self.output_label.config(text=res)
        self.output_label.configure(background="Green")
        self.output_label.configure(foreground="Red",font=("Comic Sans",44))





if __name__ == "__main__":
    app = App()
    app.mainloop()
