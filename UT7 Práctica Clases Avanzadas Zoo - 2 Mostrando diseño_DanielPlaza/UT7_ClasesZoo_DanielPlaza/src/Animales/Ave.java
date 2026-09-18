/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Animales;

/**
 *
 * @author alumno
 */
public class Ave {

    String especie;
    String tipoPlumaje;
    double alturaVuelo;
    double velocidadVuelo;

    public String getEspecie() {
        return especie;
    }

    public void setEspecie(String especie) {
        this.especie = especie;
    }

    public String getTipo() {
        return tipoPlumaje;
    }

    public void setTipo(String tipo) {
        this.tipoPlumaje = tipo;
    }

    public double getAlturaVuelo() {
        return alturaVuelo;
    }

    public void setAlturaVuelo(double alturaVuelo) {
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

    
    

    public Ave(String especie, String tipoPlumaje, double alturaVuelo, double velocidadVuelo) {
        this.especie = especie;
        this.tipoPlumaje = tipoPlumaje;
        this.alturaVuelo = alturaVuelo;
        this.velocidadVuelo = velocidadVuelo;
    }

    public void Ataca() {
        System.out.println("Atacando...");
    }
    public void noAtaca() {
        System.out.println("No ataca... ");
    }
    
    public void moverAlas() {
        System.out.println("Moviendo alas...");
    }
}
