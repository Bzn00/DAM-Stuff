/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pruebas;

import java.util.Scanner;

/**
 *
 * @author PC GAMER
 */
public class Pruebas3 {

    public static void main(String[] args) {
        int numeroSecreto = (int) (Math.random() * 10) + 1;
        Scanner sc = new Scanner(System.in);
        int respuesta;
        int vidas = 5;

        System.out.println("Introduce el numero a probar: ");
        respuesta = sc.nextInt();
        while (respuesta != numeroSecreto && vidas != 0) {
            if (respuesta != numeroSecreto) {
                System.out.println("Ese no era el numero");
                vidas--;
                System.out.println("Te quedan " + vidas + " intentos");
                System.out.println("Introduce el numero a probar: ");
                respuesta = sc.nextInt();
            } else if (vidas == 0 && respuesta != numeroSecreto) {
                System.out.println("Perdiste, el numero secreto era " + numeroSecreto);
            }
            else {
                System.out.println("Felicidades, ganaste, el numero que elegiste es: " + respuesta);
                System.out.println("El numero secreto era: " + numeroSecreto);
                System.out.println("Tu numero de vidas es: " + vidas);
            }
        }
    }
}
