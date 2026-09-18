/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pruebas;

/**
 *
 * @author PC GAMER
 */
public class Pruebas4 {
    public static void main(String[] args) {
        System.out.println(sumar(22, 23));
        llamar("Daniel");
    }

    private static int sumar(int num1, int num2) {
        int sum;
        sum = num1 + num2;
        return sum;
    }
    
    private static void llamar(String nombre){
        System.out.println("Hola, " + nombre);
    }
}
