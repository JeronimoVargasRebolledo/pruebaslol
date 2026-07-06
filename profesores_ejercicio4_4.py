# ejercicio 4.4: polimorfismo - clases Profesor y ProfesorTitular
# La pregunta del libro es: ¿que imprime el programa si se guarda un
# ProfesorTitular en una variable de tipo Profesor y se llama imprimir()?
# Respuesta: "Es un profesor titular.", porque por el polimorfismo se
# ejecuta el metodo de la clase hija, que sobreescribe al del padre.


class Profesor:
    # clase padre: representa un profesor generico

    def imprimir(self):
        print("Es un profesor.")


class ProfesorTitular(Profesor):
    # clase hija: hereda de Profesor y sobreescribe imprimir()

    def imprimir(self):
        print("Es un profesor titular.")


# programa principal (equivale a la clase Prueba del libro)
if __name__ == "__main__":
    # la variable "es" un Profesor pero contiene un ProfesorTitular
    profesor1 = ProfesorTitular()
    profesor1.imprimir()  # imprime: Es un profesor titular.
