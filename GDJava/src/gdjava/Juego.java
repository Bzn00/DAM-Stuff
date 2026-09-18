/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package gdjava;

import javax.swing.JFrame;

/**
 *
 * @author PC GAMER
 */
public class Juego {

    public static void main(String[] args) {

        JFrame frame = new JFrame("Geometry Dash - Prototipo Java");
        GeometryDashLite game = new GeometryDashLite();
        frame.add(game);
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
