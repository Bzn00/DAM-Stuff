/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Animales;

/**
 *
 * @author PC GAMER
 */
public class Rapaz extends Ave {

    
    
    
    public Rapaz(String especie, String tipoPlumaje, double alturaVuelo, double velocidadVuelo) {
        super(especie, tipoPlumaje, alturaVuelo, velocidadVuelo);

    }

    public void atacar() {
        System.out.println("Atacando...");
    }
    
    public void girarIzquierda() {
        System.out.println("Girando izquierda...");
    }
    
    public void girarDerecha() {
        System.out.println("Girando derecha...");
    }
    
    @Override
    public void moverAlas() {
        System.out.println("Moviendo alas...");
    }
}
