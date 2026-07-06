# ejercicio 4.7: clases abstractas - jerarquia de animales
# Animal es la clase raiz (abstracta), Canido y Felino son subclases,
# y de ellas heredan Perro, Lobo, Leon y Gato.
# En Python las clases abstractas se hacen con el modulo abc.

from abc import ABC, abstractmethod


class Animal(ABC):
    # clase abstracta raiz: no se puede instanciar directamente

    def __init__(self):
        self.sonido = ""
        self.alimentos = ""
        self.habitat = ""
        self.nombre_cientifico = ""

    @abstractmethod
    def get_nombre_cientifico(self):
        pass

    @abstractmethod
    def get_sonido(self):
        pass

    @abstractmethod
    def get_alimentos(self):
        pass

    @abstractmethod
    def get_habitat(self):
        pass


class Canido(Animal):
    # subclase de Animal, sigue siendo abstracta (no define los metodos)
    pass


class Felino(Animal):
    # subclase de Animal, sigue siendo abstracta (no define los metodos)
    pass


class Perro(Canido):
    def __init__(self):
        super().__init__()
        self.sonido = "Ladrido"
        self.alimentos = "Carnivoro"
        self.habitat = "Domestico"
        self.nombre_cientifico = "Canis lupus familiaris"

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Lobo(Canido):
    def __init__(self):
        super().__init__()
        self.sonido = "Aullido"
        self.alimentos = "Carnivoro"
        self.habitat = "Bosque"
        self.nombre_cientifico = "Canis lupus"

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Leon(Felino):
    def __init__(self):
        super().__init__()
        self.sonido = "Rugido"
        self.alimentos = "Carnivoro"
        self.habitat = "Pradera"
        self.nombre_cientifico = "Panthera leo"

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Gato(Felino):
    def __init__(self):
        super().__init__()
        self.sonido = "Maullido"
        self.alimentos = "Ratones"
        self.habitat = "Domestico"
        self.nombre_cientifico = "Felis silvestris catus"

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


# programa principal: array de animales y se imprimen sus atributos
if __name__ == "__main__":
    animales = [Perro(), Lobo(), Leon(), Gato()]

    for animal in animales:
        print("--- " + type(animal).__name__ + " ---")
        print("Nombre cientifico:", animal.get_nombre_cientifico())
        print("Sonido:", animal.get_sonido())
        print("Alimentos:", animal.get_alimentos())
        print("Habitat:", animal.get_habitat())
        print()
