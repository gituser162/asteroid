import sys
import pygame
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE_SECONDS, ASTEROID_MAX_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    dt = 0
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = Asteroid(100, 100, ASTEROID_MIN_RADIUS)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
    
    # print("Starting Asteroids!")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Asteroid min radius: {ASTEROID_MIN_RADIUS}")
    # print(f"Asteroid kinds: {ASTEROID_KINDS}")
    # print(f"Asteroid spawn rate seconds: {ASTEROID_SPAWN_RATE_SECONDS}")
    # print(f"Asteroid max radius: {ASTEROID_MAX_RADIUS}")


if __name__ == "__main__":
    main()
