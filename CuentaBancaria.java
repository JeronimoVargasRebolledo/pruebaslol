import java.util.Scanner;

public class CuentaBancaria {
    // Atributos
    String nombresTitular;
    String apellidosTitular;
    int numeroCuenta;
    enum Tipo { AHORROS, CORRIENTE }
    Tipo tipoCuenta;
    float saldo = 0;
    float tasaInteresMensual; // nuevo atributo

    // constructor
    public CuentaBancaria(String nombresTitular, String apellidosTitular, int numeroCuenta, Tipo tipoCuenta, float tasaInteresMensual) {
        this.nombresTitular = nombresTitular;
        this.apellidosTitular = apellidosTitular;
        this.numeroCuenta = numeroCuenta;
        this.tipoCuenta = tipoCuenta;
        this.tasaInteresMensual = tasaInteresMensual;
        this.saldo = 0; // El saldo inicial siempre es cero según el enunciado
    }

    // metodo imprimir todos los datos 
    void imprimir() {
        System.out.println("\n--- DATOS DE LA CUENTA ---");
        System.out.println("Titular: " + nombresTitular + " " + apellidosTitular);
        System.out.println("Número de cuenta: " + numeroCuenta);
        System.out.println("Tipo de cuenta: " + tipoCuenta);
        System.out.println("Saldo actual: $" + saldo);
        System.out.println("Tasa de interés mensual: " + tasaInteresMensual + "%");
    }

    void consultarSaldo() {
        System.out.println("El saldo actual es: $" + saldo);
    }

    boolean consignar(float valor) {
        if (valor > 0) {
            saldo += valor;
            System.out.println("Consignación exitosa. Nuevo saldo: $" + saldo);
            return true;
        } else {
            System.out.println("El valor a consignar debe ser mayor que cero.");
            return false;
        }
    }

    boolean retirar(float valor) {
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            System.out.println("Retiro exitoso. Nuevo saldo: $" + saldo);
            return true;
        } else {
            System.out.println("Retiro fallido. Verifique el valor o el saldo disponible.");
            return false;
        }
    }

    // nuevo metodo de interes mensual
    void aplicarInteres() {
        float interes = saldo * (tasaInteresMensual / 100);
        saldo += interes;
        System.out.println("Se ha aplicado un interés del " + tasaInteresMensual + "%.");
        System.out.println("Interés sumado: $" + interes);
        System.out.println("Nuevo saldo: $" + saldo);
    }

    // METODO MAIN PARA INTERACCIÓN POR TECLADO
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("=== Registro de Nueva Cuenta Bancaria ===");
        System.out.print("Ingrese nombres del titular: ");
        String nombres = sc.nextLine();
        System.out.print("Ingrese apellidos del titular: ");
        String apellidos = sc.nextLine();
        System.out.print("Ingrese número de cuenta: ");
        int numero = sc.nextInt();
        
        System.out.print("Tipo de cuenta (1 para Ahorros, 2 para Corriente): ");
        int opcionTipo = sc.nextInt();
        Tipo tipo = (opcionTipo == 1) ? Tipo.AHORROS : Tipo.CORRIENTE;

        System.out.print("Ingrese la tasa de interés mensual (%): ");
        float tasa = sc.nextFloat();

        // creacion del objeto
        CuentaBancaria cuenta = new CuentaBancaria(nombres, apellidos, numero, tipo, tasa);

        int opcionMenu;
        do {
            System.out.println("\n--- MENÚ DE OPERACIONES ---");
            System.out.println("1. Consultar saldo");
            System.out.println("2. Consignar dinero");
            System.out.println("3. Retirar dinero");
            System.out.println("4. Aplicar interés mensual");
            System.out.println("5. Ver información completa");
            System.out.println("6. Salir");
            System.out.print("Seleccione una opción: ");
            opcionMenu = sc.nextInt();

            switch (opcionMenu) {
                case 1:
                    cuenta.consultarSaldo();
                    break;
                case 2:
                    System.out.print("Monto a consignar: ");
                    cuenta.consignar(sc.nextFloat());
                    break;
                case 3:
                    System.out.print("Monto a retirar: ");
                    cuenta.retirar(sc.nextFloat());
                    break;
                case 4:
                    cuenta.aplicarInteres();
                    break;
                case 5:
                    cuenta.imprimir();
                    break;
                case 6:
                    System.out.println("Saliendo del sistema...");
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
        } while (opcionMenu != 6);

        sc.close();
    }
}
