# ejercicio 4.6: metodos polimorficos - clases Profesor y ProfesorTitular
# La pregunta del libro es: ¿que pasa si en una variable de tipo Profesor
# (la clase padre) se llama el metodo imprimir_anios() que solo existe
# en la clase hija ProfesorTitular?
# En Java el programa NO COMPILA, porque la variable es de tipo Profesor
# y esa clase no tiene el metodo imprimirAños.
# En Python si funciona, porque el tipado es dinamico: lo que importa es
# el objeto real que hay guardado, no el "tipo" de la variable.


class Profesor:
    # clase padre: representa un profesor generico

    def imprimir(self):
        print("Es un profesor.")


class ProfesorTitular(Profesor):
    # clase hija: agrega el atributo anios y el metodo imprimir_anios()

    def __init__(self):
        self.anios = 0  # cantidad de anios que el profesor ha sido titular

    def imprimir(self):
        print("Es un profesor titular.")

    def imprimir_anios(self):
        print("Anios =", self.anios)


# programa principal (equivale a la clase Prueba3 del libro)
if __name__ == "__main__":
    # el objeto guardado realmente es un ProfesorTitular
    profesor1 = ProfesorTitular()
    profesor1.imprimir_anios()  # en Python imprime: Anios = 0

    # para ver el comportamiento de Java lo probamos con un Profesor puro:
    # ahi si falla porque la clase padre no tiene ese metodo
    profesor2 = Profesor()
    try:
        profesor2.imprimir_anios()
    except AttributeError:
        print("Error: la clase Profesor no tiene el metodo imprimir_anios")
        print("(esto equivale al error de compilacion que da Java)")
