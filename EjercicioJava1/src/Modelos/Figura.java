/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Modelos;

/**
 *
 * @author PC GAMER
 */
public class Figura extends Superheroe {
    private String codigo;
    private double precio;

    public Figura(String nombre, String descripcion, boolean capa) {
        super(nombre, descripcion, capa);
    }

    public Figura() {
    }

    public Figura(String codigo, double precio) {
        this.codigo = codigo;
        this.precio = precio;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    @Override
    public String toString() {
        return "Figura{" + "codigo=" + codigo + ", precio=" + precio + '}';
    }
    
    public double subirPrecio(double precioAñadido) {
        precio = precio + precioAñadido;
        return precio;
    }
    
}
