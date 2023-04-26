import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.display = tk.Entry(master,
                                width=30,
                                justify="right",
                                font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("=", 5, 0, columnspan=4)

    def create_button(self, text, row, column, columnspan=1, padx=5, pady=5):
        button = tk.Button(self.master,
                           text=text,
                           width=5,
                           height=2,
                           font=("Arial", 16),
                           command=lambda: self.button_click(text),
                           fg="white",
                           bg="#1B4F72",
                           border=0)
        button.grid(row=row,
                    column=column,
                    columnspan=columnspan,
                    padx=padx,
                    pady=pady)

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "=":
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        else:
            self.display.insert(tk.END, text)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
