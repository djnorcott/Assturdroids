import math
import pygame


class Level1:
    points = []

    def draw(self, screen, playerPos):
        # Define an array of points drawing a flat landscape a cave going down and across under the surface
        self.points = [
            (0, 500),
            (100, 500),
            (100, 400),
            (200, 400),
            (200, 500),
            (300, 500),
            (300, 300),
            (400, 300),
            (400, 500),
            (500, 500),
            (500, 200),
            (600, 200),
            (600, 500),
            (700, 500),
            (700, 100),
            (800, 100),
            (800, 500),
            (900, 500),
            (900, 0),
            (1000, 0),
            (1000, 500),
            (1100, 500),
            (1100, 200),
            (1200, 200),
            (1200, 500),
            (1300, 500),
            (1300, 300),
            (1400, 300),
            (1400, 500),
            (1500, 500),
            (1500, 400),
            (1600, 400),
        ]

        # Draw lines between each point
        for i in range(len(self.points) - 1):
            self.points[i] = (
                self.points[i][0] - playerPos[0],
                self.points[i][1] - playerPos[1],
            )

        for i in range(len(self.points) - 1):
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (self.points[i][0], self.points[i][1]),
                (
                    self.points[i + 1][0],
                    self.points[i + 1][1],
                ),
            )
