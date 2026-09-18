/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package pruebaexamen;

import Modelos.Concesionario;
import Modelos.Vehiculo;

/**
 *
 * @author PC GAMER
 */
public class PruebaExamen {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Vehiculo v1 = new Vehiculo("123123GFG", "Ford", 7765.34, true);
        Vehiculo v2 = new Vehiculo("123678GG", "Honda", 763.34, false);
        Concesionario c1 = new Concesionario();
        System.out.println("--- Vehiculos ---");
        c1.agregarVehiculo(v1);
        c1.agregarVehiculo(v2);
        c1.listarVehiculos();
        System.out.println("");
        System.out.println("");
        System.out.println(" --- Lista de Disponibles ---");
        c1.listarDisponibles();
        System.out.println("");
        System.out.println("");
        System.out.println("--- Buscar Matricula Vehiculo disponible ---");
        c1.buscarMatricula(v1.getMatricula());
        System.out.println("");
        System.out.println("");
        System.out.println("");
        System.out.println("--- Buscar Matricula vehiculo no disponible ---");
        c1.buscarMatricula(v2.getMatricula());
    }
    
}
