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
public class Pruebas5 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String palabraAEncriptar;
        String sinEspacios;
        int contador = 0;
        System.out.println("Introduce una palabra: ");
        palabraAEncriptar = sc.nextLine();
        // elimina todos los espacios
        palabraAEncriptar = palabraAEncriptar.replace(" ", "");
        // elimina espacios solo al principio y al final
//        palabraAEncriptar = palabraAEncriptar.trim();
        for (int i = 0; i < palabraAEncriptar.length(); i++) {
            contador++;
        }
        System.out.println("La palabra o frase tiene: " + contador + " ");
        System.out.println(palabraAEncriptar);
    }

}
