/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejerciciojava1;

import Modelos.Figura;

/**
 *
 * @author PC GAMER
 */
public class EjercicioJava1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Figura f1 = new Figura("Iron man", 123.23);
        System.out.println("Precio normal: ");
        System.out.println(f1.getPrecio());
        System.out.println("Precio subido: ");
        System.out.println(f1.getCodigo());
        f1.subirPrecio(113.23);
        System.out.println(f1.getPrecio());
    }
    
}
