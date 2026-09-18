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
public class Pruebas2 {

    public static void main(String[] args) {
        menu();
    }

    public static void menu() {
        int opcion;
        Scanner sc = new Scanner(System.in);
        System.out.println("Bienvenido a mi programa de terminal.");
        System.out.println("Pulsa intro para continuar");
        limpiarPantalla();
        System.out.println("1. Mostrar nombre.");
        System.out.println("2. Mostrar numeros del 1 al 10.");
        opcion = sc.nextInt();
        while (opcion != 1 && opcion != 2) {
            System.out.println("Opcion no valida, elige 1 o 2.");
            System.out.println("1. Mostrar nombre.");
            System.out.println("2. Mostrar numeros del 1 al 10.");
            opcion = sc.nextInt();
        }
        opcionesMenu(opcion);
    }

    public static void limpiarPantalla() {
        for (int i = 0; i < 100; i++) {
            System.out.println("");
        }
    }

    private static int opcionesMenu(int opcion) {
        switch (opcion) {
            case 1 -> {
                System.out.println("Tu nombre es Daniel");
            }
            case 2 -> {
                for (int i = 0; i < 10; i++) {
                    System.out.println(i);
                }
            }
        }

        return opcion;

    }
}
