# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
  print('Starting Asteroids!')
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

  Player.containers = (updatable,drawable)
  Asteroid.containers = (updatable,drawable,asteroids)
  AsteroidField.containers = updatable

  player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
  asteroid_field = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill('black')
    updatable.update(dt)
    for instance in drawable:
      instance.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()