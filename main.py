import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    time = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = time.tick(60.00)/1000
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game Over !")
                sys.exit()
            for bullet in shots:
                if asteroid.collisions(bullet):
                    bullet.kill()
                    asteroid.split()
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
    
print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
