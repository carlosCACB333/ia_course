def adition(num1, num2):
    return num1 + num2


#  y = ax² + bx + c para x = 5.
def square_equation(a, b, c, x=5):
    if a == 0:
        return "No es una ecuación cuadrática"
    y = a * x**2 + b * x + c
    if y < 0:
        return "El valor de y es negativo"
    elif y == 0:
        return "El valor de y es 0"
    return y