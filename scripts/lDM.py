""" 
Te presento un lenguage muy rarito llamado el  "lenguage de la mano". Este trabaja con una memenoria indefinida de bytes  con todo los 
valores inicializados en 0. El lenguaje tiene 7 instrucciones:
👉 => Mueve el puntero a la siguiente posición de la memoria.
👈 => Mueve el puntero a la posición anterior de la memoria.
👆 => Incrementa el valor de la posición actual en 1.
👇 => Decrementa el valor de la posición actual en 1.
🤜 => Si la celda de memoria en la posición actual es 0, salta justo después del 🤛 correspondiente1.
🤛 => Si la celda de memoria en la posición actual es diferente de 0, salta justo después del 🤜 correspondiente.
🤚 => Imprime el código ASCII de la celda de memoria en la posición actual.

NOTA:
    - Las celdas son bytes (0-255).
    - 🤜 y 🤛 son bucles y se pueden anidar.

Ejemplo de un programa que imprime "Hello":
👇🤜👇👇👇👇👇👇👇👉👆👈🤛👉👇👊👇🤜👇👉👆👆👆👆👆👈🤛👉👆👆👊👆👆👆👆👆👆👆👊👊👆👆👆👊

"""

# 1. Crear un programa que imprima "Hello" en el lenguage de la mano.
# 2. Crear un programa que imprima "Hello World" en el lenguage de la mano.

MIN_CELL = 0
MAX_CELL = 255


def move_pointer_right(pointer, memory):
    if pointer < len(memory) - 1:
        pointer += 1
    return pointer


def move_pointer_left(pointer, memory):
    if pointer > 0:
        pointer -= 1
    return pointer


def increment_cell(pointer, memory):
    if memory[pointer] < MAX_CELL:
        memory[pointer] += 1
    return memory


def decrement_cell(pointer, memory):
    if memory[pointer] > MIN_CELL:
        memory[pointer] -= 1
    return memory


def print_cell(pointer, memory):
    print(chr(memory[pointer]), end="")
    return memory


def loop_start(pointer, memory, code):
    if memory[pointer] == 0:
        pointer = code.find("🤛", pointer)
    return pointer


def loop_end(pointer, memory, code):
    if memory[pointer] != 0:
        pointer = code.find("🤜", pointer)
    return pointer


def run(code):
    memory = [0] * 100
    pointer = 0
    for i, char in enumerate(code):
        if char == "👉":
            pointer = move_pointer_right(pointer, memory)
        elif char == "👈":
            pointer = move_pointer_left(pointer, memory)
        elif char == "👆":
            memory = increment_cell(pointer, memory)
        elif char == "👇":
            memory = decrement_cell(pointer, memory)
        elif char == "🤜":
            pointer = loop_start(pointer, memory, code)
        elif char == "🤛":
            pointer = loop_end(pointer, memory, code)
        elif char == "👊":
            memory = print_cell(pointer, memory)


if __name__ == '__main__':
    code = "👇🤜👇👇👇👇👇👇👇👉👆👈🤛👉👇👊👇🤜👇👉👆👆👆👆👆👈🤛👉👆👆👊👆👆👆👆👆👆👆👊👊👆👆👆👊"
    run(code)
