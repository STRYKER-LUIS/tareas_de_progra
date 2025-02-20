import random
import timeit

class Usuario:
    def __init__(self, user_id, nombre, edad):
        self.user_id = user_id
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Usuario(ID={self.user_id}, Nombre='{self.nombre}', Edad={self.edad})"

nombres = ["luis", "carlos", "chepe", "david", "diego", "fernando", "gabriela", "paco", "isabel", "jorge"]
usuarios = [Usuario(user_id=i, nombre=random.choice(nombres), edad=random.randint(18, 60)) for i in range(100000)]

def busqueda_lineal(usuarios, user_id):
    for usuario in usuarios:
        if usuario.user_id == user_id:
            return usuario
    return None

def busqueda_binaria(usuarios, user_id):
    izquierda, derecha = 0, len(usuarios) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if usuarios[medio].user_id == user_id:
            return usuarios[medio]
        elif usuarios[medio].user_id < user_id:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

usuarios_ordenados = sorted(usuarios, key=lambda u: u.user_id)

target_id = random.randint(0, 99999)

print("Comparación de tiempos de búsqueda:")
tiempo_lineal = timeit.timeit(lambda: busqueda_lineal(usuarios, target_id), number=10)
tiempo_binaria = timeit.timeit(lambda: busqueda_binaria(usuarios_ordenados, target_id), number=10)

print(f"Búsqueda Lineal: {tiempo_lineal:.6f} segundos")
print(f"Búsqueda Binaria: {tiempo_binaria:.6f} segundos")
