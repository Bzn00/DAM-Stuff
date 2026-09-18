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
public class Concesionario {

    ArrayList<Vehiculo> vehiculos = new ArrayList<>();
    Vehiculo v1 = new Vehiculo("123123GFG", "Ford", 7765.34, true);
    public void agregarVehiculo(Vehiculo vehiculo) {
        vehiculos.add(vehiculo);
    }

    public void buscarMatricula(String matricula) {
        if (matricula.equals(v1.getMatricula())) {
            System.out.println("El vehiculo con la matricula que busca esta disponible " + v1.toString());
        } else {
            System.out.println("No se ha encontrado el vehiculo con la matricula " + matricula);
        }
    }

    public void listarDisponibles() {
        for (Vehiculo Vehiculo1 : vehiculos) {
            if (Vehiculo1.isDisponible()) {
                System.out.println(Vehiculo1);
            }
        }
    }
    
    public void listarVehiculos() {
        for (Vehiculo vehiculo : vehiculos) {
            System.out.println(vehiculo);
        }
    }
}
