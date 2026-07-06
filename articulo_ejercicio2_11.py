# ejercicio 2.11: sobrecarga de constructores - clase ArticuloCientifico
# En Java se definen tres constructores y unos llaman a otros con this().
# En Python solo puede haber un __init__, asi que la forma sencilla de
# lograr lo mismo es con parametros por defecto: si no se pasan, quedan
# con un valor "vacio" igual que en el primer constructor.


class ArticuloCientifico:

    # "primer constructor": solo titulo y autor
    # "segundo constructor": + palabras claves, publicacion y anio
    # "tercer constructor": + resumen
    def __init__(self, titulo, autor, palabras_claves=None,
                 publicacion="", anio=0, resumen=""):
        # esta parte equivale al primer constructor
        self.titulo = titulo
        self.autor = autor

        # esta parte equivale al segundo constructor (invoca al primero)
        if palabras_claves is None:
            palabras_claves = []
        self.palabras_claves = palabras_claves
        self.publicacion = publicacion
        self.anio = anio

        # esta parte equivale al tercer constructor (invoca al segundo)
        self.resumen = resumen

    def imprimir(self):
        # imprime todos los atributos del articulo en pantalla
        print("Titulo:", self.titulo)
        print("Autor:", self.autor)
        print("Palabras claves:")
        for palabra in self.palabras_claves:
            print(" -", palabra)
        print("Publicacion:", self.publicacion)
        print("Anio:", self.anio)
        print("Resumen:", self.resumen)


# programa principal: se usa el "tercer constructor" (todos los datos)
if __name__ == "__main__":
    articulo = ArticuloCientifico(
        "La inteligencia artificial en la educacion",
        "Jeronimo Vargas",
        ["inteligencia artificial", "educacion", "aprendizaje"],
        "Revista Colombiana de Computacion",
        2026,
        "Este articulo analiza el impacto de la IA en la educacion superior.")

    articulo.imprimir()
