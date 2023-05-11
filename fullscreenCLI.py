import pygame
from colour import Color
import numpy as np

def temp_to_rgb(temp):
    temp = temp / 100
    if (temp <= 66):
        red = 255
        green = temp
        green = 99.4708025861 * np.log(green) - 161.1195681661
        if (temp <= 19):
            blue = 0
        else:
            blue = temp - 10
            blue = 138.5177312231 * np.log(blue) - 305.0447927307
    else:
        red = temp - 60
        red = 329.698727446 * (red ^ -0.1332047592)
        green = temp - 60
        green = 288.1221695283 * (green ^ -0.0755148492 )
        blue = 255
    return (clamp(red, 0, 255), clamp(green, 0, 255), clamp(blue, 0, 255))

def clamp(x, min_val, max_val):
    return max(min(x, max_val), min_val)

def fill_screen_with_temp(temp):
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    running = True

    rgb = temp_to_rgb(temp)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(rgb)
        pygame.display.flip()

    pygame.quit()

color_temp = int(input("Enter a color temperature (e.g., 2700): "))
fill_screen_with_temp(color_temp)
