# ejercicio 2.10: sobrecarga de metodos - clase Pedido
# En Java se hace con varios metodos con el mismo nombre y distinta
# cantidad de parametros. En Python no existe la sobrecarga como tal,
# asi que se simula con parametros por defecto (None / 0).


class Pedido:

    def calcular_pedido(self, primer_plato, costo_primer_plato,
                        bebida, costo_bebida,
                        segundo_plato=None, costo_segundo_plato=0,
                        postre=None, costo_postre=0):
        """Calcula el costo total del pedido segun las partes que pida el cliente."""

        # caso 1: primer plato y bebida
        if segundo_plato is None and postre is None:
            total = costo_primer_plato + costo_bebida
            print("El costo de " + primer_plato + " y " + bebida +
                  " es = $" + str(total))

        # caso 2: primer plato, segundo plato y bebida
        elif postre is None:
            total = costo_primer_plato + costo_segundo_plato + costo_bebida
            print("El costo de " + primer_plato + " + " + segundo_plato +
                  " + " + bebida + " es = $" + str(total))

        # caso 3: primer plato, segundo plato, bebida y postre
        else:
            total = (costo_primer_plato + costo_segundo_plato +
                     costo_bebida + costo_postre)
            print("El costo de " + primer_plato + " + " + segundo_plato +
                  " + " + bebida + " + " + postre + " es = $" + str(total))


# programa principal: se usan las tres "versiones" del metodo
if __name__ == "__main__":
    pedido1 = Pedido()
    pedido2 = Pedido()
    pedido3 = Pedido()

    # pedido con primer plato y bebida
    pedido1.calcular_pedido("Sopa", 8000, "Jugo de mango", 3000)

    # pedido con primer plato, segundo plato y bebida
    pedido2.calcular_pedido("Sopa", 8000, "Gaseosa", 2500,
                            "Bandeja paisa", 15000)

    # pedido con primer plato, segundo plato, bebida y postre
    pedido3.calcular_pedido("Ensalada", 6000, "Limonada", 3500,
                            "Pechuga a la plancha", 12000,
                            "Flan de caramelo", 4000)
