/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Vista;
import Animales.Animales;
import Animales.AveAcuatica;
import Animales.Pez;
import Animales.Ganado;
import Animales.Rapaz;
import Personas.Cuidadores;
import Personas.Persona;
/**
 *
 * @author alumno
 */
public class UT7_ClasesZoo_DanielPlaza {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Pez pez1 = new Pez("Escamas placoides", 50.55, 500);
        Animales gato = new Animales("Gato", "Yuki", 5, 0, "Hembra", true);
        Animales gato2 = new Animales("Gato", "Ichigo", 5, 0, "Macho", true);
        Ganado cabra = new Ganado("Blanco", 0.33, true);
        Rapaz aguila = new Rapaz("Real", "Plumas águila", 4500.35, 25.5);
        AveAcuatica gaviota = new AveAcuatica("Blanco", 9000, 80);
        Cuidadores cuidador1 = new Cuidadores("Aves", "66553");
        Persona persona1 = new Persona("Negro", "Oscura", "Camiseta blanca", "Humano");
        // TODO code application logic here
        System.out.println("Pez");
        System.out.println("Tipo escamas: " + pez1.getEscamado());
        System.out.println("Profundidad buceo: " + pez1.getProfundidadBuceo());
        System.out.println("Velocidad nadado: " + pez1.getVelocidadNadado());
        System.out.println("");
        System.out.println("Nombre gato: " + gato.getNombre());
        gato.beber();
        gato.reproducirse();
        gato2.reproducirse();
        System.out.println("color pelo: " + cabra.getColorPelo());
        System.out.println("cm cuernos: " + cabra.getCmCuernos());
        cabra.darLeche();
        System.out.println("");
        System.out.println("Especie: " + aguila.getEspecie());
        System.out.println("Tipo Ave: " + aguila.getTipo());
        System.out.println("Altura Vuelo: " + aguila.getAlturaVuelo());
        System.out.println("Tipo plumaje: " + aguila.getTipoPlumaje());
        aguila.girarDerecha();
        aguila.girarIzquierda();
        aguila.atacar();
        System.out.println("");
        System.out.println(gaviota.getAlturaVuelo());
        System.out.println("");
        cuidador1.alimentar(true);
        System.out.println("");
        System.out.println("Persona 1");
        persona1.hablar();
        System.out.println("");
        System.out.println("Gaviota");
        gaviota.huir();
        System.out.println("");
        System.out.println("Gato");
        gato.isSangreCaliente(true);
        System.out.println("");
        persona1.getEspecie();
    }
}