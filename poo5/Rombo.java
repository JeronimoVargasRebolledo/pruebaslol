
/**
 * Write a description of class Rombo here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Rombo {
    double diagonalMayor;
    double diagonalMenor;

    public Rombo(double diagonalMayor, double diagonalMenor) {
        this.diagonalMayor = diagonalMayor;
        this.diagonalMenor = diagonalMenor;
    }

    double calcularArea() {
        return (diagonalMayor * diagonalMenor) / 2;
    }

    double calcularPerimetro() {
        // El lado se calcula con las mitades de las diagonales (Pitágoras)
        double lado = Math.sqrt(Math.pow(diagonalMayor/2, 2) + Math.pow(diagonalMenor/2, 2));
        return 4 * lado;
    }
}
