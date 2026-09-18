/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package gdjava;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.Timer;

/**
 *
 * @author PC GAMER
 */
public class GeometryDashLite extends JPanel {
   private static final int ALTURA = 1600;
    private static final int ANCHURA = 400;
    private static final int GROUND_Y = 700;

    // Propiedades del jugador (Cubo)
    private final int playerX = 100;
    private int playerY = GROUND_Y - 40;
    private final int playerSize = 40;
    private double velocityY = 0;
    private final double gravity = 0.8;
    private final double jumpStrength = -13;
    private boolean isGrounded = true;

    // Obstáculos y estado del juego
    private final ArrayList<Rectangle> obstacles = new ArrayList<>();
    private final int speed = 6;
    private boolean gameOver = false;

    public GeometryDashLite() {
        setPreferredSize(new Dimension(ALTURA, ANCHURA));
        setBackground(Color.BLACK);
        setFocusable(true);

        // Generar obstáculos de prueba (Triángulos representados por Rectángulos para simplicidad)
        obstacles.add(new Rectangle(600, GROUND_Y - 40, 30, 40));
        obstacles.add(new Rectangle(1000, GROUND_Y - 40, 30, 40));
        obstacles.add(new Rectangle(1400, GROUND_Y - 40, 30, 40));

        // Listener de teclado
        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if ((e.getKeyCode() == KeyEvent.VK_SPACE || e.getKeyCode() == KeyEvent.VK_UP) && isGrounded && !gameOver) {
                    velocityY = jumpStrength;
                    isGrounded = false;
                }
                if (e.getKeyCode() == KeyEvent.VK_R && gameOver) {
                    restartGame();
                }
            }
        });

        // Bucle del juego (~60 FPS)
        Timer timer = new Timer(16, e -> updateGame());
        timer.start();
    }

    private void updateGame() {
        if (gameOver) return;

        // Aplicar gravedad
        velocityY += gravity;
        playerY += velocityY;

        // Colisión con el suelo
        if (playerY >= GROUND_Y - playerSize) {
            playerY = GROUND_Y - playerSize;
            velocityY = 0;
            isGrounded = true;
        }

        // Mover obstáculos hacia la izquierda (Simula el avance del jugador)
        Rectangle playerBounds = new Rectangle(playerX, playerY, playerSize, playerSize);
        for (Rectangle obstacle : obstacles) {
            obstacle.x -= speed;

            // Detectar colisión con obstáculo
            if (playerBounds.intersects(obstacle)) {
                gameOver = true;
            }

            // Reciclar obstáculos que salen de la pantalla
            if (obstacle.x + obstacle.width < 0) {
                obstacle.x = ALTURA + 200;
            }
        }

        repaint();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;

        // Dibujar Suelo
        g2d.setColor(Color.WHITE);
        g2d.drawLine(0, GROUND_Y, ALTURA, GROUND_Y);

        // Dibujar Jugador (Cubo)
        g2d.setColor(Color.GREEN);
        g2d.fillRect(playerX, playerY, playerSize, playerSize);

        // Dibujar Obstáculos
        g2d.setColor(Color.RED);
        for (Rectangle obstacle : obstacles) {
            g2d.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
        }

        // Pantalla de Game Over
        if (gameOver) {
            g2d.setColor(Color.WHITE);
            g2d.setFont(new Font("Arial", Font.BOLD, 26));
            g2d.drawString("¡OH NO, ERES TERRIBLE NIGGA, PULSA R PARA VOLVER A JUGAR", 180, ANCHURA / 2);
        }
    }

    private void restartGame() {
        playerY = GROUND_Y - playerSize;
        velocityY = 0;
        gameOver = false;
        obstacles.get(0).x = 600;
        obstacles.get(1).x = 1000;
        obstacles.get(2).x = 1400;
    }

    
}
