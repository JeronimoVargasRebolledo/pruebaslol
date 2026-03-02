import java.util.Scanner; // importamos scanner para leer por teclado

public class Persona {
    String nombre;
    String apellidos;
    String numeroDocumentoIdentidad;
    int añoNacimiento;
    String paisDeNacimiento;
    char genero;

    public Persona(String nombre, String apellidos, String numeroDocumentoIdentidad,
                   int añoNacimiento, String paisDeNacimiento, char genero) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.numeroDocumentoIdentidad = numeroDocumentoIdentidad;
        this.añoNacimiento = añoNacimiento;
        this.paisDeNacimiento = paisDeNacimiento;
        this.genero = genero;
    }

    public void imprimir() {
        System.out.println("\n--- DATOS DE LA PERSONA ---");
        System.out.println("Nombre: " + nombre);
        System.out.println("Apellidos: " + apellidos);
        System.out.println("Documento: " + numeroDocumentoIdentidad);
        System.out.println("Año de nacimiento: " + añoNacimiento);
        System.out.println("País: " + paisDeNacimiento);
        System.out.println("Género: " + genero);
    }

    public static void main(String[] args) {
        // objeto scanner para leer por teclado
        Scanner sc = new Scanner(System.in);

        System.out.println("=== Registro de Persona ===");

        System.out.print("Ingrese nombre: ");
        String nom = sc.nextLine();

        System.out.print("Ingrese apellidos: ");
        String ape = sc.nextLine();

        System.out.print("Ingrese número de documento: ");
        String doc = sc.nextLine();

        System.out.print("Ingrese año de nacimiento: ");
        int año = sc.nextInt();
        
        // limpiamos el buffer para seguir leyendo
        sc.nextLine(); 

        System.out.print("Ingrese país de nacimiento: ");
        String pais = sc.nextLine();

        System.out.print("Ingrese género (H/M): ");
        // tomamos la primera letra
        char gen = sc.next().charAt(0);

        // tomamos el objeto con los datos capturados 
        Persona p1 = new Persona(nom, ape, doc, año, pais, gen);
        
        
        p1.imprimir();

        //cerramos el scanner
        sc.close();
    }
}
