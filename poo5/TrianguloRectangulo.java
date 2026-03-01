
/**
 * Write a description of class TrianguloRectangulo here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class TrianguloRectangulo {
    int base;
    int altura;

    public TrianguloRectangulo(int base, int altura) {
        this.base = base;
        this.altura = altura;
    }

    double calcularArea() {
        return (base * altura / 2.0);
    }

    double calcularPerimetro() {
        return (base + altura + calcularHipotenusa());
    }

    double calcularHipotenusa() {
        return Math.pow(base * base + altura * altura, 0.5);
    }

    void determinarTipoTriangulo() {
        double hipo = calcularHipotenusa();
        if ((base == altura) && (base == hipo)) {
            System.out.println("Es un triángulo equilátero");
        } else if ((base != altura) && (base != hipo) && (altura != hipo)) {
            System.out.println("Es un triángulo escaleno");
        } else {
            System.out.println("Es un triángulo isósceles");
        }
    }
}