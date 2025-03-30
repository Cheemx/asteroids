import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_obj = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        
        updatable.update(dt)
        
        screen.fill("black")

        for player in drawable:
            player.draw(screen)
            
        pygame.display.flip()
        
        dt = clock_obj.tick(60) / 1000
        

if __name__ == "__main__":
    main()
