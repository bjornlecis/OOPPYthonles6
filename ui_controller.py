from Combobox_vb import App as cba
from voorbeeld_radiobuttons import App as rb

keuze = input("welke programma wil je runnen")
if keuze == "1":
    app = cba()
    app.mainloop()
elif keuze == "2":
    app = rb()
    app.mainloop()
else:
    print("foute invoer")


