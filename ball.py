import pygame
from settings import WIDTH, HEIGHT

class Ball:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = pygame.Color("red")
        self.size = size
        self.speed_x = 7
        self.speed_y = 7
        self.max_speed = 15
        self.speed_increment = 0.5

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Ball collision with top or bottom of the screen
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

    def update(self, screen):
        self.move()
        pygame.draw.ellipse(screen, self.color, self.rect)

    def increase_speed(self):
        if abs(self.speed_x) < self.max_speed:
            self.speed_x *= (1 + self.speed_increment)
        if abs(self.speed_y) < self.max_speed:
            self.speed_y *= (1 + self.speed_increment)
