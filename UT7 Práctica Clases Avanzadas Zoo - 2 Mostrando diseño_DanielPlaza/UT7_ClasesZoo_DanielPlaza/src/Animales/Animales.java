/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Animales;

/**
 *
 * @author PC GAMER
 */
public class Animales {
    String Especie;
    String nombre;
    double peso;
    double altura;
    String Sexo;
    boolean sangreCaliente = true;

    public String getEspecie() {
        return Especie;
    }

    public void setEspecie(String Especie) {
        this.Especie = Especie;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    public String getSexo() {
        return Sexo;
    }

    public void setSexo(String Sexo) {
        this.Sexo = Sexo;
    }

    public boolean isSangreCaliente(boolean sangreCaliente) {
        sangreCaliente = true;
        System.out.println(sangreCaliente);
        return sangreCaliente;
    }

    public void setSangreCaliente(boolean sangreCaliente) {
        this.sangreCaliente = sangreCaliente;
    }

    public Animales(String Especie, String nombre, double peso, double altura, String Sexo, boolean sangreCaliente) {
        this.Especie = Especie;
        this.nombre = nombre;
        this.peso = peso;
        this.altura = altura;
        this.Sexo = Sexo;
        this.sangreCaliente = sangreCaliente;
    }
    
    public void comer() {
        System.out.println("Comiendo...");
    }
    public void beber() {
        System.out.println("Bebiendo...");
    }
    public void dormir() {
        System.out.println("Durmiendo...");
    }
    public void reproducirse() {
        if (Sexo.equals("Macho")) {
        System.out.println("Macho reproduciendose...");
        }
        if (Sexo.equals("Hembra")) {
            System.out.println("Hembra reproduciendose...");
        }
    }

    @Override
    public String toString() {
        return "Animales{" + "Especie=" + Especie + ", nombre=" + nombre + ", peso=" + peso + ", altura=" + altura + ", Sexo=" + Sexo + ", sangreCaliente=" + sangreCaliente + '}';
    }
    
}