/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package pruebas;

import java.util.Scanner;

/**
 *
 * @author PC GAMER
 */
public class Pruebas {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcion;
        menu();
        opcion = sc.nextInt();
        limpiarPantalla();
        elegiropcion(opcion);
        while (opcion != 0) {
            menu();
            opcion = sc.nextInt();
            limpiarPantalla();
            elegiropcion(opcion);
        }
    }

    private static void menu() {
        System.out.println("----------");
        System.out.println("|  MENU  |");
        System.out.println("----------");
        System.out.println("1. Mostrar nombre");
        System.out.println("2. Mostrar numeros del 1 al 10");
        System.out.println("0. Salir");
        System.out.println("Introduce que opcion quieres realizar.");
        System.out.print("Elige 1, 2 o 0: ");

    }

    private static int elegiropcion(int opcion) {
        String nombre;
        Scanner sc = new Scanner(System.in);
        switch (opcion) {
            case 1 -> {
                System.out.println("Introduce tu nombre: ");
                nombre = sc.nextLine();
                System.out.println("Mi nombre es " + nombre);
                System.out.println("Pulsa intro para contunuar.");
                sc.nextLine();
                limpiarPantalla();
            }
            case 2 -> {
                for (int i = 1; i <= 10; i++) {
                    System.out.println(i);
                }
                System.out.println("Pulsa intro para contunuar.");
                sc.nextLine();
                limpiarPantalla();
            }
            case 0 -> {
                System.out.println("Saliendo...");
                System.out.println("Pulsa intro para contunuar.");
                sc.nextLine();
                limpiarPantalla();
                System.exit(opcion);
            }
        }
        return opcion;

    }

    private static void limpiarPantalla() {
        for (int i = 0; i < 100; i++) {
            System.out.println("");
        }
    }

}
