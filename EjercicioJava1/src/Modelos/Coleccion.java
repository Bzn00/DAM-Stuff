/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Modelos;

import java.util.ArrayList;

/**
 *
 * @author PC GAMER
 */
public class Coleccion {
    private String nombreColeccion;
    private ArrayList <Figura> listaFiguras;

    public Coleccion(String nombreColeccion, ArrayList<Figura> listaFiguras) {
        this.nombreColeccion = nombreColeccion;
        this.listaFiguras = listaFiguras;
    }

    public ArrayList <Figura> getListaFiguras() {
        return listaFiguras;
    }

    public void setListaFiguras(ArrayList <Figura> listaFiguras) {
        this.listaFiguras = listaFiguras;
    }

    public String getNombreColeccion() {
        return nombreColeccion;
    }

    public void setNombreColeccion(String nombreColeccion) {
        this.nombreColeccion = nombreColeccion;
    }
    
    public void añadirFigura(Figura figura) {
        listaFiguras.add(figura);
    }
    
}
