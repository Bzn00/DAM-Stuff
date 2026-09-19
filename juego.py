# Juego Facil
import pygame
import sys

pygame.init()
ancho, alto = 640, 480
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.get_caption("Juego simple")

pelota_img = pygame.image.load("E:\Descargas\Pfp Nazuna Nanakusa.jpg")
pelota_rect = pelota_img.get_rect()
velocidad = [4, 4]

jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Mover pelota
    pelota_rect = pelota_rect.move(velocidad)

    if pelota_rect.left < 0 or pelota_rect.right > ancho:
        velocidad[0] = -velocidad[0]
    if pelota_rect.top < 0 or pelota_rect.bottom > alto:
        velocidad[1] = -velocidad[1]

    # Dibujar
    pantalla.fill((255, 255, 255))
    pantalla.blit(pelota_img, pelota_rect)
    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()