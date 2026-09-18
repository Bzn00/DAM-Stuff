/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Modelos;

/**
 *
 * @author PC GAMER
 */
public class Vehiculo {

    private String matricula;
    private String marca;
    private double precioBase;
    private boolean disponible;

    public Vehiculo(String matricula, String marca, double precioBase, boolean disponible) {
        this.matricula = matricula;
        this.marca = marca;
        setPrecioBase(precioBase);
        this.disponible = disponible;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public double getPrecioBase() {
        return precioBase;
    }

    public void setPrecioBase(double precioBase) {
        if (precioBase <= 0) {
            System.out.println("El precio base no puede ser negativo");
        } else {
            this.precioBase = precioBase;
        }
    }

    public boolean isDisponible() {
        return disponible;
    }

    public void setDisponible(boolean disponible) {
        this.disponible = disponible;
    }

    @Override
    public String toString() {
        return """
               
               Informacion del vehiculo
               Matricula: """ + matricula + " \nMarca: " + marca + " \nPrecio Base: " + precioBase + " \ndisponibilidad: " + disponible;
    }
    
    

}
