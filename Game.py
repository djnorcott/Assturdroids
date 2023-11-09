import pygame
import pygame.sprite
import pygame.joystick
import random
from Bullet import Bullet
from Player import Player
from Asteroid import Asteroid


class Game:

    minRadius = 40
    maxRadius = 200

    def __init__(self, screen):
        self.isTouchScreen = False
        self.screen = screen
        self.startingColour = (255, 0, 255)
        self.asteroids = []


    def setup(self):
        self.player = Player(self.screen.get_rect().center)

        self.bullets = []
        self.timeSinceLastBullet = 0

        self.scale = self.screen.get_width()

        for i in range(80):
            self.asteroids.append(
                Asteroid(
                    (
                        random.randint(-self.scale, self.scale),
                        random.randint(-self.scale, self.scale),
                    ),
                    self.minRadius,
                    self.maxRadius,
                )
            )

    def play(self, events):
        self.screen.fill((0, 0, 0))

        # If space is pressed
        if pygame.key.get_pressed()[pygame.K_w]:
            self.player.thrust()
        else:
            self.player.noThrust()

        # If Q or E are pressed, rotate left or right accordingly
        if pygame.key.get_pressed()[pygame.K_a]:
            self.player.rotateBy(-1)
        elif pygame.key.get_pressed()[pygame.K_d]:
            self.player.rotateBy(1)

        # If space is pressed, fire a bullet
        if pygame.key.get_pressed()[pygame.K_SPACE] and pygame.time.get_ticks() - self.timeSinceLastBullet > 30:
            self.timeSinceLastBullet = pygame.time.get_ticks()
            self.bullets.append(Bullet(self.player.centre, self.player.rotation))

        # Update the player
        self.player.update()

        # Draw the player in the center of the screen
        self.player.draw(self.screen)
        
        # Draw the asteroids
        for asteroid in self.asteroids:
            asteroid.draw(self.screen, self.player.pos)


        # Draw a white box around self.scale, offset by the player's position
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            (
                -self.player.pos[0],
                -self.player.pos[1],
                self.scale * 2,
                self.scale * 2,
            ),
            1,
        )

        # Draw the bullets
        for bullet in self.bullets:
            bullet.draw(self.screen, (0,0))
            killThisBullet = False

            if not bullet.animate():
                self.bullets.remove(bullet)

            # Check for collisions between the bullet and the asteroids
            for asteroid in self.asteroids:
                if asteroid.hasBulletHit(bullet.pos, self.player.pos):
                    
                    # If the asteroid is big enough, create asteroid.radius // self.minRadius new ones
                    if asteroid.radius > self.minRadius * 2:
                        numberToSpawn = asteroid.radius // self.minRadius
                        if numberToSpawn > 3:
                            numberToSpawn = 3

                        for i in range(numberToSpawn):
                            self.asteroids.append(
                                Asteroid(
                                    (
                                        asteroid.pos[0] + random.randint(-asteroid.radius // 2, asteroid.radius // 2),
                                        asteroid.pos[1] + random.randint(-asteroid.radius // 2, asteroid.radius // 2),
                                    ),
                                    asteroid.radius // numberToSpawn,
                                    asteroid.radius // numberToSpawn,
                                )
                            )
                        

                    self.asteroids.remove(asteroid)
                    killThisBullet = True
            
            if killThisBullet:
                
                # Only remove it if it's in the list
                if bullet in self.bullets:
                    self.bullets.remove(bullet)
                    

        return self.play