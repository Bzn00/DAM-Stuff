/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Animales;

/**
 *
 * @author alumno
 */
public class Ganado {

    String colorPelo;
    double cmCuernos;
    boolean daLeche;

    public String getColorPelo() {
        return colorPelo;
    }

    public void setColorPelo(String colorPelo) {
        this.colorPelo = colorPelo;
    }

    public double getCmCuernos() {
        return cmCuernos;
    }

    public void setCmCuernos(double cmCuernos) {
        this.cmCuernos = cmCuernos;
    }

    public boolean isDaLeche() {
        return daLeche;
    }

    public void setDaLeche(boolean darLeche) {
        this.daLeche = darLeche;
    }

    public Ganado(String colorPelo, double cmCuernos, boolean darLeche) {
        this.colorPelo = colorPelo;
        this.cmCuernos = cmCuernos;
        this.daLeche = darLeche;
    }

    public void darLeche() {
            System.out.println("Dando leche...");
    }

    @Override
    public String toString() {
        return "Ganado{" + "colorPelo=" + colorPelo + ", cmCuernos=" + cmCuernos + ", darLeche=" + daLeche + '}';
    }

}
