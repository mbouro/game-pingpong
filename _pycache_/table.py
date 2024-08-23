import pygame, time, sys
from player import Player
from ball import Ball
from settings import WIDTH, HEIGHT, player_width, player_height

class Table:
    def __init__(self, screen):
        self.screen = screen
        self.game_over = False
        self.score_limit = 5
        self.winner = None
        self._generate_world()
        self.font = pygame.font.SysFont('Arial', 60)
        self.inst_font = pygame.font.SysFont('Arial', 30)
        self.color = pygame.Color("white")

    def _generate_world(self):
        self.playerA = Player(0, HEIGHT // 2 - (player_height // 2), player_width, player_height)
        self.playerB = Player(WIDTH - player_width, HEIGHT // 2 - (player_height // 2), player_width, player_height)
        self.ball = Ball(WIDTH // 2 - player_width // 2, HEIGHT // 2 - player_width // 2, player_width)

    def _ball_hit(self):
        if self.ball.rect.left >= WIDTH:
            self.playerA.score += 1
            self.ball.rect.x = WIDTH // 2 - self.ball.size // 2
            self.ball.rect.y = HEIGHT // 2 - self.ball.size // 2
            self.ball.speed_x = -abs(self.ball.speed_x)  # Serve towards player B
            time.sleep(1)
        elif self.ball.rect.right <= 0:
            self.playerB.score += 1
            self.ball.rect.x = WIDTH // 2 - self.ball.size // 2
            self.ball.rect.y = HEIGHT // 2 - self.ball.size // 2
            self.ball.speed_x = abs(self.ball.speed_x)  # Serve towards player A
            time.sleep(1)
        if self.ball.rect.colliderect(self.playerA.rect):
            self.ball.speed_x = abs(self.ball.speed_x)  # Ball moves right
            self.ball.increase_speed()
        if self.ball.rect.colliderect(self.playerB.rect):
            self.ball.speed_x = -abs(self.ball.speed_x)  # Ball moves left
            self.ball.increase_speed()

    def _bot_opponent(self):
        if self.ball.rect.centery < self.playerA.rect.centery:
            if self.playerA.rect.top > 0:
                self.playerA.move_up()
        if self.ball.rect.centery > self.playerA.rect.centery:
            if self.playerA.rect.bottom < HEIGHT:
                self.playerA.move_bottom()
    #Schläger mit Maus
    
    #def player_move(self):
    #    mouse_y = pygame.mouse.get_pos()[1]
    #    self._bot_opponent()
    #    # Player B follows the mouse
    #    if mouse_y < self.playerB.rect.centery and self.playerB.rect.top > 0:
    #        self.playerB.move_up()
    #    elif mouse_y > self.playerB.rect.centery and self.playerB.rect.bottom < HEIGHT:
    #        self.playerB.move_bottom()

        #Player move with keybaord
    def player_move(self):
        keys = pygame.key.get_pressed()
        self._bot_opponent()
        if keys[pygame.K_UP]:
            if self.playerB.rect.top > 0:
                self.playerB.move_up()
        if keys[pygame.K_DOWN]:
            if self.playerB.rect.bottom < HEIGHT:
                self.playerB.move_bottom()



    def _show_score(self):
        A_score = self.font.render(str(self.playerA.score), True, self.color)
        B_score = self.font.render(str(self.playerB.score), True, self.color)
        self.screen.blit(A_score, (WIDTH // 4, 50))
        self.screen.blit(B_score, ((WIDTH // 4) * 3, 50))

    def _game_end(self):
        if self.winner is not None:
            self.game_over = True

    def update(self):
        self._show_score()
        self.playerA.update(self.screen)
        self.playerB.update(self.screen)
        self._ball_hit()
        if self.playerA.score == self.score_limit:
            self.winner = "Gegner"
            self._game_end()
        elif self.playerB.score == self.score_limit:
            self.winner = "Du"
            self._game_end()
        if not self.game_over:
            self.ball.update(self.screen)
