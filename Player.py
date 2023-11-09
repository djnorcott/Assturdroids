import math
import pygame


class Player:
    thrusting = False
    rotation = 0
    gravity = 0.0
    velocity = (0.0, 0.0)
    points = []
    centre = (0, 0)

    rotationSpeed = 0.6
    thrustSpeed = 0.006
    drag = 0.005
    maxSpeed = 1.5

    def __init__(self, pos):
        self.centre = pos
        self.pos = (0, 0)

    def moveTo(self, pos):
        self.pos = pos

    def moveBy(self, vector):
        self.pos = (self.pos[0] + vector[0], self.pos[1] + vector[1])

    def rotateBy(self, angle):
        self.rotation += angle * self.rotationSpeed

    def update(self):
        self.changeVelocity((0, self.gravity))
        
        # Apply drag
        self.changeVelocity((-self.velocity[0] * self.drag, -self.velocity[1] * self.drag))

        self.moveBy(self.velocity)

    def changeVelocity(self, vector):
        self.velocity = (self.velocity[0] + vector[0], self.velocity[1] + vector[1])

        # Don't allow the length of the velocity vector to be greater than the maximum speed
        speed = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)
        if speed > self.maxSpeed:
            self.velocity = (
                self.velocity[0] * self.maxSpeed / speed,
                self.velocity[1] * self.maxSpeed / speed,
            )

    def draw(self, screen):
        # Define an array of points drawing an isosceles triangle centered on 0,0
        points = [
            (-10, 20),
            (0, -20),
            (10, 20),
        ]

        if self.thrusting and self.startedThursting < pygame.time.get_ticks() - 5:
            points.append((0, 30))
            self.startedThursting = pygame.time.get_ticks()

        self.points = []

        # Rotate points by the current rotation of the sprite
        currentAngle = (self.rotation) * math.pi / 180
        for i in range(len(points)):
            self.points.append(
                (
                    points[i][0] * math.cos(currentAngle)
                    - points[i][1] * math.sin(currentAngle)
                    + self.centre[0],
                    points[i][0] * math.sin(currentAngle)
                    + points[i][1] * math.cos(currentAngle)
                    + self.centre[1],
                )
            )

        # Draw lines between each point
        for i in range(len(self.points)):
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (self.points[i][0], self.points[i][1]),
                (
                    self.points[(i + 1) % len(self.points)][0],
                    self.points[(i + 1) % len(self.points)][1],
                ),
            )

    def thrust(self):
        if not self.thrusting:
            self.startedThursting = pygame.time.get_ticks()

        self.thrusting = True

        # Increase velocity based on the current rotation of the sprite
        currentAngle = (self.rotation - 90) * math.pi / 180

        self.changeVelocity(
            (
                math.cos(currentAngle) * self.thrustSpeed,
                math.sin(currentAngle) * self.thrustSpeed,
            )
        )

    def noThrust(self):
        self.thrusting = False
