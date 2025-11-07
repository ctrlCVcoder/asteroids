# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player
from shot import Shot
from logger import log_state
from logger import log_event
import sys


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()
    
    updatable.add(asteroid_field)
    updatable.add(player)
    drawable.add(player)


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))

        updatable.update(dt)

        #player collision with asteroieds
        for asteroid in asteroids:
            if player.colides_with(asteroid):
                log_event("player_hit") #, player_pos=(player.position.x, player.position.y), asteroid_pos=(asteroid.position.x, asteroid.position.y))
                print("Game Over!")
                sys.exit()

        #shot collision with asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.colides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    #asteroid.kill()
                    asteroid.split()

        for thing in drawable:
            thing.draw(screen)

        

        pygame.display.flip()

        

        

        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
