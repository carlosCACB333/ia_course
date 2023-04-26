from tkinter import *

#Crear la ventana principal
root = Tk()
root.title("Ejemplo de interfaz gráfica")
root.config(bg="#202123")

#Crear una entrada
entrada = Entry(
    root,
    width=35,
    font=("Arial", 16),
)
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#Crear una funcion para el botón
def envia_boton():
    valor_entrada = entrada.get()
    ventana_nueva1 = Toplevel(root)
    ventana_nueva1.config(bg="#202123")
    ventana_nueva1.geometry("400x200")
    ventana_nueva1.title("Ventana secundaria")
    etiqueta = Label(
        ventana_nueva1,
        bg="#202123",
        fg="white",
        text="El valor introducido en la ventana principal es:  " +
        valor_entrada).grid(row=0)
    etiqueta.grid(row=0)


#Crear un botón
envia = Button(root, text="Enviar", command=envia_boton)
envia.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

#Iniciar el loop principal
root.mainloop()
