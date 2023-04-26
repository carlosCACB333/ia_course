"""
Se requiere leer y decodificar una lista de un archivo CSV, el cual tiene como contenido el siguiente texto:
Alejandro, Francisco, amanda,Fiorella,Flavio ,Adela,Arcadio,Azucena, Alvaro,feliciano,Franco,Maria

De esa lista se requiere que se separe en 4 listas, las cuales son:

•	Empiezan con A y terminan con O
•	Empiezan con A y terminan con A
•	Empiezan con F y terminan con O
•	Empiezan con G y terminan con A

"""

csv = "Alejandro, Francisco, amanda,Fiorella,Flavio ,Adela,Arcadio,Azucena, Alvaro,feliciano,Franco,Maria"

names = [name.strip().capitalize() for name in csv.split(",")]
names_a_o = [
    name for name in names if name.startswith("A") and name.endswith("o")
]
names_a_a = [
    name for name in names if name.startswith("A") and name.endswith("a")
]
names_f_o = [
    name for name in names if name.startswith("F") and name.endswith("o")
]
names_g_a = [
    name for name in names if name.startswith("F") and name.endswith("a")
]

print(names_a_o)
print(names_a_a)
print(names_f_o)
print(names_g_a)