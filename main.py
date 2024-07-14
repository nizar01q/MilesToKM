from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300, 100)
window.config(padx=40)


def m_to_km():
    m = float(input.get())
    km = round(m * 1.609344, 4)
    label2.config(text=km)



input = Entry(width=15)
input.grid(column=1, row=0)

label1 = Label(text="is equal to")
label1.grid(column=0, row=1)

label2 = Label(text="0")
label2.grid(column=1, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

label4 = Label(text="Miles")
label4.grid(column=2, row=0)

button = Button(text="Calculate", command=m_to_km)
button.grid(column=1, row=2)












window.mainloop()