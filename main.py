import pygame
from constants import *
#source venv/bin/activate

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x=0
    while x==0:
        pygame.Surface.fill(screen, "black")
        pygame.display.flip()
    
    

if __name__ == "__main__":
    main()