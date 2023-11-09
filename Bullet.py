import pygame
import math


class Bullet:
    velocity = (0, 0)
    pos = (0, 0)
    speed = 1.5

    def __init__(self, pos, angle):
        super(Bullet, self).__init__()

        self.pos = pos

        self.startTime = pygame.time.get_ticks()

        # Convert angle to radians
        angle = (angle-90) * math.pi / 180

        self.velocity = (
            math.cos(angle) * self.speed,
            math.sin(angle) * self.speed,
        )

        self.pos = (
            self.pos[0] + self.velocity[0]*14,
            self.pos[1] + self.velocity[1]*14,
        )

        self.startTime = pygame.time.get_ticks()

    def draw(self, screen, playerPos):
        # Offset each point based on the player
        offsetPoint = (
            self.pos[0] - playerPos[0],
            self.pos[1] - playerPos[1],
        )

        # Define a pentagon 5 pixels in diameter
        self.points = []
        for i in range(6):
            angle = ((2 * math.pi) / 5) * i

            self.points.append((math.cos(angle) * 5, math.sin(angle) * 5))

        # Draw the bullet
        for i in range(len(self.points) - 1):
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (self.points[i][0] + offsetPoint[0], self.points[i][1] + offsetPoint[1]),
                (
                    self.points[i + 1][0] + offsetPoint[0],
                    self.points[i + 1][1] + offsetPoint[1],
                ),
            )

    def animate(self):

        # Move the bullet 
        self.pos = (
            self.pos[0] + self.velocity[0],
            self.pos[1] + self.velocity[1],
        )

        # If the bullet has been around for more than two seconds, kill it
        if pygame.time.get_ticks() - self.startTime > 2000:
            return False
        
        return True
