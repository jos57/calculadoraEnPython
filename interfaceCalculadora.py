#aquí interface gráfica de calculadora

from this import s
from tkinter import *



body = Tk()
body.geometry("360x400")
body.configure(background="#5C0120")

######################pantalla######################################################

input = Entry(body, font="Roboto 20").grid(columnspan=4, rowspan=2,padx=20, pady=20)

#####################fila 1#########################################################

button7   = Button(body, text="7", height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=2, column=0, sticky="ew")
button8   = Button(body, text="8", height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=2, column=1, sticky="ew")
button9   = Button(body, text="9", height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=2, column=2, sticky="ew")
buttonDiv = Button(body, text="/", height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=2, column=3, sticky="ew")

#####################fila 2#########################################################

button4    = Button(body, text="4", width=3, height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=3, column=0, sticky="ew")
button5    = Button(body, text="5", width=3, height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=3, column=1, sticky="ew")
button6    = Button(body, text="6", width=3, height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=3, column=2, sticky="ew")
buttonMult = Button(body, text="x", width=3, height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=3, column=3, sticky="ew")

#####################fila 3#########################################################

button1     = Button(body, text="1", width=3, height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=4, column=0, sticky="ew")
button2     = Button(body, text="2", width=3, height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=4, column=1, sticky="ew")
button3     = Button(body, text="3", width=3, height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=4, column=2, sticky="ew")
buttonResta = Button(body, text="-", width=3, height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=4, column=3, sticky="ew")

####################fila 4###########################################################

buttonPunto = Button(body, text=".", width=3, height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=5, column=0, sticky="ew")
buttonCero  = Button(body, text="0", width=3, height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=5, column=1, sticky="ew")
buttonIgual = Button(body, text="=", width=3, height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=5, column=2, sticky="ew")
buttonSuma  = Button(body, text="+", width=3, height=3, font="Roboto 15", bg="black", fg="#5C0120").grid(row=5, column=3, sticky="ew")






body.mainloop()