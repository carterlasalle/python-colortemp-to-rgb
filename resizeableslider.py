import pygame
import numpy as np

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SLIDER_WIDTH = 20
SLIDER_HEIGHT = 200

# Color for slider
SLIDER_COLOR = (0, 0, 0)

# Minimum and maximum color temperature
MIN_TEMP = 1000
MAX_TEMP = 10000

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
        red = 329.698727446 * (red ** -0.1332047592)
        green = temp - 60
        green = 288.1221695283 * (green ** -0.0755148492)
        blue = 255
    return (clamp(red, 0, 255), clamp(green, 0, 255), clamp(blue, 0, 255))

def clamp(x, min_val, max_val):
    return max(min(int(x), max_val), min_val)

def run():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    slider_y = 0
    dragging = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] < SLIDER_WIDTH and 0 <= event.pos[1] <= SLIDER_HEIGHT:
                    dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    if screen.get_flags() & pygame.FULLSCREEN:
                        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
                    else:
                        pygame.display.set_mode((event.w, event.h), pygame.FULLSCREEN)

        if dragging:
            _, y = pygame.mouse.get_pos()
            slider_y = clamp(y, 0, SCREEN_HEIGHT - SLIDER_HEIGHT)

        temp = MIN_TEMP + (MAX_TEMP - MIN_TEMP) * slider_y / (SCREEN_HEIGHT - SLIDER_HEIGHT)
        rgb = temp_to_rgb(temp)

        screen.fill(rgb)
        pygame.draw.rect(screen, SLIDER_COLOR, pygame.Rect(0, slider_y, SLIDER_WIDTH, SLIDER_HEIGHT))
       
        pygame.display.flip()
        clock.tick(60)

run()
