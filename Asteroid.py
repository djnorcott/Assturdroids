import math
import pygame
import random

class Asteroid:
    points = []
    pos = (0, 0)
    velocity = (0, 0)
    radius = 0

    def __init__(self, pos, minRadius, maxRadius):
        # Define a random regular polygon of points, between 50px and 150px in diameter
        self.radius = random.randint(minRadius, maxRadius)
        self.numberOfPoints = random.randint(10, 20)
        
        # Define an array of points for the polygon
        self.points = []
        for i in range(self.numberOfPoints+1):
            angle = ((2 * math.pi) / self.numberOfPoints) * i

            # Make them not quite regular
            rx = random.random() * 0.2 + 0.9
            ry = random.random() * 0.2 + 0.9

            self.points.append((math.cos(angle) * self.radius * rx, math.sin(angle) * self.radius * ry))

        self.pos = pos

        self.velocity = (random.random() * 0.3 - 0.15, random.random() * 0.3 - 0.15)


    def draw(self, screen, playerPos):
        # Offset each point based on the player

        self.pos = (
            self.pos[0] + self.velocity[0],
            self.pos[1] + self.velocity[1],
        )

        offsetPoints = []
        
        for i in range(len(self.points)):
            offsetPoints.append((
                self.pos[0] + self.points[i][0] - playerPos[0],
                self.pos[1] + self.points[i][1] - playerPos[1],
            ))

        for i in range(len(offsetPoints) - 1):
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (offsetPoints[i][0], offsetPoints[i][1]),
                (
                    offsetPoints[i + 1][0],
                    offsetPoints[i + 1][1],
                ),
            )
        
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (offsetPoints[0][0], offsetPoints[0][1]),
            (
                offsetPoints[len(offsetPoints) - 1][0],
                offsetPoints[len(offsetPoints) - 1][1],
            ),
        )

    def hasBulletHit(self, bulletPos, playerPos):
        # If the length of the vector from the asteroid's center to the bullet is less than the asteroid's radius, return true
        offsetPos = (
            self.pos[0] - playerPos[0],
            self.pos[1] - playerPos[1],
        )

        if math.sqrt((bulletPos[0] - offsetPos[0])**2 + (bulletPos[1] - offsetPos[1])**2) < self.radius:
            return True
        else:
            return False