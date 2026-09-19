import java.util.Scanner;
public class prueba {
    public static void main(String[] args) {
        Persona p1 = new Persona();
        Scanner sc = new Scanner(System.in);
        String nombre;
        System.out.println("Introduce el nombre de la persona que te gusta: ");
        nombre = sc.nextLine();

        p1.gustar(nombre);
    }
}