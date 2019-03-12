# Faça um app que tocará um arquivo mp3.

import pygame

pygame.mixer.init()
pygame.mixer.music.load('megaman.mp3')
pygame.mixer.music.play()
input('Ouviu?') # Gambiarra, pq não funcionou, hehe
