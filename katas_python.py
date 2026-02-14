
# ==========================================================
# 1. Frecuencia de letras en una cadena (sin contar espacios)
# ==========================================================

def frecuencia_letras(texto):
    frecuencias = {}
    for letra in texto.replace(" ", ""):
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias


# ==========================================================
# 2. Doble de cada valor usando map()
# ==========================================================

def doble_lista(lista):
    return list(map(lambda x: x * 2, lista))


# ==========================================================
# 3. Palabras que contienen una palabra objetivo
# ==========================================================

def palabras_con_objetivo(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]


# ==========================================================
# 4. Diferencia entre valores de dos listas usando map()
# ==========================================================

def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))


# ==========================================================
# 5. Media y estado (aprobado o suspenso)
# ==========================================================

def evaluar_notas(notas, nota_aprobado=5):
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado


# ==========================================================
# 6. Factorial recursivo
# ==========================================================

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0:
        return 1
    return n * factorial(n - 1)


# ==========================================================
# 7. Lista de tuplas a lista de strings usando map()
# ==========================================================

def tuplas_a_strings(lista):
    return list(map(str, lista))


# ==========================================================
# 8. División con manejo de excepciones
# ==========================================================
    
def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        raise ZeroDivisionError("No se puede dividir entre cero")

# ==========================================================
# 9. Filtrar mascotas prohibidas en España usando filter()
# ==========================================================

def filtrar_mascotas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, mascotas))


# ==========================================================
# 10. Promedio con excepción personalizada
# ==========================================================

class ListaVaciaError(Exception):
    pass

def promedio_lista(lista):
    if not lista:
        raise ListaVaciaError("La lista está vacía")
    return sum(lista) / len(lista)


# ==========================================================
# 11. Validación de edad con excepciones
# ==========================================================

def validar_edad(edad):
    if edad < 0 or edad > 120:
        raise ValueError("Edad fuera de rango")
    return True
# ==========================================================
# 12. Longitud de cada palabra de una frase
# ==========================================================

def longitud_palabras(frase):
    return list(map(len, frase.split()))


# ==========================================================
# 13. Letras en mayúsculas y minúsculas sin repetir
# ==========================================================

def letras_may_min(caracteres):
    letras = set(filter(str.isalpha, caracteres))
    return list(map(lambda l: (l.upper(), l.lower()), letras))


# ==========================================================
# 14. Palabras que empiezan por una letra
# ==========================================================

def palabras_por_letra(lista, letra):
    return [palabra for palabra in lista if palabra.startswith(letra)]


# ==========================================================
# 15. Lambda que suma 3 a cada número
# ==========================================================

sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))


# ==========================================================
# 16. Palabras más largas que n usando filter()
# ==========================================================

def palabras_largas(texto, n):
    return list(filter(lambda p: len(p) > n, texto.split()))


# ==========================================================
# 17. Lista de dígitos a número usando reduce()
# ==========================================================

from functools import reduce

def digitos_a_numero(lista):
    return reduce(lambda x, y: x * 10 + y, lista)


# ==========================================================
# 18. Filtrar estudiantes con nota >= 90
# ==========================================================

estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota": 95},
    {"nombre": "Luis", "edad": 22, "nota": 85},
    {"nombre": "María", "edad": 21, "nota": 90}
]

mejores_estudiantes = list(filter(lambda e: e["nota"] >= 90, estudiantes))


# ==========================================================
# 19. Lambda que filtra números impares
# ==========================================================

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))


# ==========================================================
# 20. Filtrar solo valores enteros
# ==========================================================

def solo_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))


# ==========================================================
# 21. Cubo de un número usando lambda
# ==========================================================

cubo = lambda x: x ** 3


# ==========================================================
# 22. Producto total usando reduce()
# ==========================================================

def producto_total(lista):
    if not lista:
        return 0
    return reduce(lambda x, y: x * y, lista)
# ==========================================================
# 23. Concatenar palabras usando reduce()
# ==========================================================

def concatenar_palabras(lista):
    return reduce(lambda x, y: x + " " + y, lista)


# ==========================================================
# 24. Diferencia total usando reduce()
# ==========================================================

def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)


# ==========================================================
# 25. Contar caracteres de una cadena
# ==========================================================

def contar_caracteres(texto):
    return len(texto)


# ==========================================================
# 26. Resto de una división usando lambda
# ==========================================================

resto_division = lambda a, b: a % b


# ==========================================================
# 27. Promedio de una lista
# ==========================================================

def promedio(lista):
    return sum(lista) / len(lista)


# ==========================================================
# 28. Primer elemento duplicado
# ==========================================================

def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None


# ==========================================================
# 29. Enmascarar variable excepto últimos 4 caracteres
# ==========================================================


def enmascarar(valor):
    texto = str(valor)
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]
# ==========================================================
# 30. Comprobar anagramas
# ==========================================================

def son_anagramas(p1, p2):
    return sorted(p1.lower()) == sorted(p2.lower())


# ==========================================================
# 31. Buscar nombre en lista o lanzar excepción
# ==========================================================

def buscar_nombre(nombres, nombre):
    if nombre in nombres:
        return True
    raise ValueError("Nombre no encontrado")


# ==========================================================
# 32. Buscar empleado y devolver puesto
# ==========================================================

def buscar_empleado(nombre, empleados):
    return empleados.get(nombre, "La persona no trabaja aquí")


# ==========================================================
# 33. Sumar elementos de dos listas usando lambda
# ==========================================================

sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))


# ==========================================================
# 34. Clase Árbol
# ==========================================================

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)

    def info_arbol(self):
        return self.tronco, len(self.ramas), self.ramas


# ==========================================================
# 35. Clase UsuarioBanco
# ==========================================================

def transferir_dinero(self, otro, cantidad):
    self.retirar_dinero(cantidad)
    otro.agregar_dinero(cantidad)

# ==========================================================
# 36. Procesamiento de texto
# ==========================================================

def contar_palabras(texto):
    palabras = texto.split()
    resultado = {}
    for p in palabras:
        resultado[p] = resultado.get(p, 0) + 1
    return resultado

def reemplazar_palabras(texto, original, nueva):
    return texto.replace(original, nueva)

def eliminar_palabra(texto, palabra):
    return " ".join(filter(lambda p: p != palabra, texto.split()))

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])


# ==========================================================
# 37. Día, tarde o noche según la hora
# ==========================================================

def momento_del_dia(hora):
    if 6 <= hora < 12:
        return "Día"
    elif 12 <= hora < 20:
        return "Tarde"
    else:
        return "Noche"

# ==========================================================
# 38. Calificación en texto
# ==========================================================

def calificacion_texto(nota):
    if nota <= 69:
        return "Insuficiente"
    elif nota <= 79:
        return "Bien"
    elif nota <= 89:
        return "Muy bien"
    else:
        return "Excelente"


# ==========================================================
# 39. Área de figuras
# ==========================================================

import math

def calcular_area(figura, datos):
    if figura == "rectangulo":
        return datos[0] * datos[1]
    elif figura == "triangulo":
        return (datos[0] * datos[1]) / 2
    elif figura == "circulo":
        return math.pi * datos[0] ** 2


# ==========================================================
# 40. Tienda con descuento
# ==========================================================

def precio_final(precio, descuento=0):
    if descuento > 0:
        precio -= descuento
    return precio
