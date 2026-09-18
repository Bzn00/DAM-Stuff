/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Personas;

/**
 *
 * @author alumno
 */
public class Cuidadores {

    String area;
    String id;

    public Cuidadores(String area, String id) {
        this.area = area;
        this.id = id;
    }

    public String getArea() {
        return area;
    }

    public void setArea(String area) {
        this.area = area;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public void alimentar(boolean alimento) {
        System.out.println("Alimentando...");
    }

    public void curar() {
        System.out.println("Curando...");
    }

    public void abrirCerradura() {
        System.out.println("Abriendo cerradura...");
    }
}
