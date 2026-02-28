public class Persona {
    // atributos originales
    String nombre;
    String apellidos;
    String numeroDocumentoIdentidad;
    int añoNacimiento;

    // nuevos atributos agregados
    String paisDeNacimiento;
    char genero; // 'H' o 'M'

    // constructor actualizado para incluir los dos nuevos campos
    public Persona(String nombre, String apellidos, String numeroDocumentoIdentidad,
                   int añoNacimiento, String paisDeNacimiento, char genero) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.numeroDocumentoIdentidad = numeroDocumentoIdentidad;
        this.añoNacimiento = añoNacimiento;
        this.paisDeNacimiento = paisDeNacimiento;
        this.genero = genero;
    }

    // metodo imprimir actualizado para mostrar toda la información
    public void imprimir() {
        System.out.println("Nombre = " + nombre);
        System.out.println("Apellidos = " + apellidos);
        System.out.println("Número de documento de identidad = " + numeroDocumentoIdentidad);
        System.out.println("Año de nacimiento = " + añoNacimiento);
        System.out.println("País de nacimiento = " + paisDeNacimiento);
        System.out.println("Género = " + genero);
        System.out.println(); // Salto de línea para mayor legibilidad
    }

    public static void main(String[] args) {
        Persona p1 = new Persona("Juan", "Perez", "12345", 2000, "Colombia", 'H');
        p1.imprimir();
    }
}
