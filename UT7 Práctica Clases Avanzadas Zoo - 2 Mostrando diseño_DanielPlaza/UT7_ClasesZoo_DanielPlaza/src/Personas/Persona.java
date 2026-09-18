/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Personas;

/**
 *
 * @author alumno
 */
public class Persona implements Interfaces.Caminar {

    String colorPelo;
    String colorPiel;
    String ropa;
    String especie;

    public String getColorPelo() {
        return colorPelo;
    }

    public void setColorPelo(String colorPelo) {
        this.colorPelo = colorPelo;
    }

    public String getColorPiel() {
        return colorPiel;
    }

    public void setColorPiel(String colorPiel) {
        this.colorPiel = colorPiel;
    }

    public String getRopa() {
        return ropa;
    }

    public void setRopa(String ropa) {
        this.ropa = ropa;
    }
    
    public void getEspecie() {
        System.out.println(especie);
    }
    
    public void setEspecie(String especie) {
        this.especie = especie;
    }
    
    public Persona(String colorPelo, String colorPiel, String ropa, String especie) {
        this.colorPelo = colorPelo;
        this.colorPiel = colorPiel;
        this.ropa = ropa;
        this.especie = especie;
    }

    public void hablar() {
        System.out.println("Hablando...");
    }

    public void getColorPelo(String colorPelo) {
        System.out.println(colorPelo);
    }


    
}
