from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.geometry("800x450")
ventana.title("Bienvenido")
ventana.config(bg="#202123")

entrada = StringVar()
entrada2 = StringVar()
entrada3 = StringVar()
entrada4 = StringVar()
var = StringVar(ventana)
res1 = StringVar()
res2 = StringVar()
res3 = StringVar()
res4 = StringVar()

validate_entry = lambda text: text.isdecimal()

#clases


def close_window():
    ventana.destroy()


def calculo():

    sumando1 = float(entrada.get()) * 37.00
    sumando2 = float(entrada.get()) * 38.20
    sumando3 = float(entrada.get()) * 38.50

    sumando4 = sumando1 - (sumando1 * 15 / 100)
    sumando5 = sumando1 - (sumando1 * 17 / 100)

    sumando6 = sumando2 - (sumando2 * 15 / 100)
    sumando7 = sumando2 - (sumando2 * 17 / 100)

    sumando8 = sumando3 - (sumando3 * 15 / 100)
    sumando9 = sumando3 - (sumando3 * 17 / 100)

    mes = combo.get()

    if mes == "Mañana":

        res1.set(str("{:.2f}".format(sumando1)) + "  Soles")
        res2.set(str("{:.2f}".format(sumando1)) + "  Soles")
        res3.set(str("Tarifa ordinaria por hora del trabajador es: S/ 37,00"))

    if mes == "Tarde":

        res1.set(str("{:.2f}".format(sumando2)) + "  Soles")
        res2.set(str("{:.2f}".format(sumando2)) + "  Soles")
        res3.set(str("Tarifa ordinaria por hora del trabajador es: S/ 38,20"))

    if mes == "Noche":

        res1.set(str("{:.2f}".format(sumando3)) + "  Soles")
        res3.set(str("Tarifa ordinaria por hora del trabajador es: S/ 38,50"))
        if sumando3 >= 2000 and sumando3 <= 5000:
            res2.set(str("{:.2f}".format(sumando8)) + "  Soles")
            res4.set(str("Se le desconto el 15% del salario bruto"))
        elif sumando3 >= 8000 and sumando3 <= 10000:
            res2.set(str("{:.2f}".format(sumando9)) + "  Soles")
            res4.set(str("Se le desconto el 17% del salario bruto"))
        else:
            res2.set(str("{:.2f}".format(sumando3)) + "  Soles")


#creando campos de texto

etiqueta1 = Label(ventana,
                  text="CALCULO DE SALARIO",
                  font=("Docktrin", 30),
                  fg="White",
                  bg="#202123").pack()
etiqueta2 = Label(ventana,
                  text="Horas Trabajadas: ",
                  font=("impact", 15),
                  fg="White",
                  bg="#202123").place(x=50, y=140)
etiqueta3 = Label(ventana,
                  text="Turno de Trabajo: ",
                  font=("impact", 15),
                  fg="White",
                  bg="#202123").place(x=50, y=200)

etiqueta5 = Label(ventana,
                  text="Salario Bruto: ",
                  font=("Yu Gothic UI Semibold", 15),
                  fg="White",
                  bg="#202123").place(x=80, y=310)
etiqueta6 = Label(ventana,
                  text="Salario Neto: ",
                  font=("Yu Gothic UI Semibold", 15),
                  fg="White",
                  bg="#202123").place(x=80, y=360)

etiqueta7 = Label(ventana,
                  textvariable=res1,
                  font=("Bahnschrift SemiBold", 14),
                  fg="Red",
                  bg="white").place(x=220, y=310, width=200)
etiqueta8 = Label(ventana,
                  textvariable=res2,
                  font=("impact", 14),
                  fg="Red",
                  bg="white").place(x=220, y=360, width=200)

etiqueta9 = Label(ventana,
                  textvariable=res3,
                  font=("Bahnschrift SemiBold", 12),
                  fg="White",
                  bg="#202123").place(x=80, y=260, width=380)
etiqueta10 = Label(ventana,
                   textvariable=res4,
                   font=("Bahnschrift SemiBold", 12),
                   fg="Red",
                   bg="#202123").place(x=220, y=400, width=280)

#creando botones

boton2 = Button(ventana,
                text="CALCULAR",
                font=("Times New Roman", 12),
                fg="White",
                bg="seashell4",
                command=calculo).place(x=630, y=150)
boton3 = Button(ventana,
                text="SALIR",
                font=("Times New Roman", 12),
                fg="White",
                bg="seashell4",
                command=close_window).place(x=650, y=330)

#creando caja de texo
txHoras = Entry(ventana, textvariable=entrada, font=(12)).place(x=220,
                                                                y=145,
                                                                width=200)

#creando deslizable

combo = ttk.Combobox(ventana, font=("arial", 12), state="readonly")
combo.place(x=220, y=205, width=200)
combo["values"] = ("Mañana", "Tarde", "Noche")
combo.current(0)

ventana.resizable(width=False, height=False)
ventana.mainloop()
