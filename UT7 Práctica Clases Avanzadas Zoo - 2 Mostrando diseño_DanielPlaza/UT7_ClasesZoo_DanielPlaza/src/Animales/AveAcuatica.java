/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Animales;

/**
 *
 * @author alumno
 */
public class AveAcuatica implements Interfaces.Volar{
    String tipoPlumaje;
    double velocidadVuelo;
    double alturaVuelo;

    public AveAcuatica(String tipoPlumaje, double velocidadVuelo, double alturaVuelo) {
        this.tipoPlumaje = tipoPlumaje;
        this.velocidadVuelo = velocidadVuelo;
        this.alturaVuelo = alturaVuelo;
    }

    public String getTipoPlumaje() {
        return tipoPlumaje;
    }

    public void setTipoPlumaje(String tipoPlumaje) {
        this.tipoPlumaje = tipoPlumaje;
    }

    public double getVelocidadVuelo() {
        return velocidadVuelo;
    }

    public void setVelocidadVuelo(double velocidadVuelo) {
        this.velocidadVuelo = velocidadVuelo;
    }

    public double getAlturaVuelo() {
        return alturaVuelo;
    }

    public void setAlturaVuelo(double alturaVuelo) {
        this.alturaVuelo = alturaVuelo;
    }
    
    public void huir(){
        System.out.println("Huyendo...");
    }

    public void moverAlas() {
        System.out.println("Moviendo alas...");
    }
    
    public void bucear() {
        System.out.println("Buceando...");
    }
    
    public void alzarVuelo() {
        System.out.println("Alzando vuelo...");
    }
    
    public void planear() {
        System.out.println("Planeando...");
    }
    
    public void girarIzquierda() {
        System.out.println("Girando izquierda...");
    }
    
    public void girarDerecha() {
        System.out.println("Girando derecha...");
    }
    
    @Override
    public String toString() {
        return "AveAcuatica{" + "tipoPlumaje=" + tipoPlumaje + ", velocidadVuelo=" + velocidadVuelo + ", alturaVuelo=" + alturaVuelo + '}';
    }
    
}
