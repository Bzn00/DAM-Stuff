/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Animales;

/**
 *
 * @author alumno
 */
public class Pez {
    String escamado;
    double velocidadNadado;
    int profundidadBuceo;

    @Override
    public String toString() {
        return "Pez{" + "escamado=" + escamado + ", velocidadNadado=" + velocidadNadado + ", profundidadBuceo=" + profundidadBuceo + '}';
    }

    public String getEscamado() {
        return escamado;
    }

    public void setEscamado(String escamado) {
        this.escamado = escamado;
    }

    public double getVelocidadNadado() {
        return velocidadNadado;
    }

    public void setVelocidadNadado(double velocidadNadado) {
        this.velocidadNadado = velocidadNadado;
    }

    public int getProfundidadBuceo() {
        return profundidadBuceo;
    }

    public void setProfundidadBuceo(int profundidadBuceo) {
        this.profundidadBuceo = profundidadBuceo;
    }

    public Pez(String escamado, double velocidadNadado, int profundidadBuceo) {
        this.escamado = escamado;
        this.velocidadNadado = velocidadNadado;
        this.profundidadBuceo = profundidadBuceo;
    }
}
