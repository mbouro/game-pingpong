import pygame, sys
from settings import WIDTH, HEIGHT
from table import Table

pygame.init()
pygame.mixer.init()  # Initialize the mixer module
start_sound = pygame.mixer.Sound("sound/Chance is music PSG2.mp3")  # Load the start sound

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

class Pong:
    def __init__(self, screen):
        self.screen = screen
        self.FPS = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 60)
        self.color = pygame.Color("white")

    def draw(self):
        pygame.display.flip()

    def show_welcome_screen(self):
        self.screen.fill("black")
        title = self.font.render("Welcome to Ping Pong", True, self.color)
        instructions = self.font.render("Press SPACE to Start", True, self.color)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
        self.screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, HEIGHT // 2))
        self.draw()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    start_sound.play()  # Play the start sound
                    return
            self.FPS.tick(30)

    def main(self):
        self.show_welcome_screen()
        while True:
            table = Table(self.screen)
            while not table.game_over:
                self.screen.fill("Gray")
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                table.player_move()
                table.update()
                self.draw()
                self.FPS.tick(30)
            self.show_game_over_screen()

    def show_game_over_screen(self):
        self.screen.fill("gray")
        game_over_text = self.font.render("Game Over", True, self.color)
        play_again_button = pygame.Rect(WIDTH // 4 - 100, HEIGHT // 2, 200, 50)
        quit_button = pygame.Rect((WIDTH // 4) * 3 - 100, HEIGHT // 2, 200, 50)
        
        pygame.draw.rect(self.screen, self.color, play_again_button)
        pygame.draw.rect(self.screen, self.color, quit_button)
        
        play_again_text = self.font.render("Play Again", True, pygame.Color("black"))
        quit_text = self.font.render("Quit", True, pygame.Color("black"))
        
        self.screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
        self.screen.blit(play_again_text, (play_again_button.x + (play_again_button.width - play_again_text.get_width()) // 2, play_again_button.y + (play_again_button.height - play_again_text.get_height()) // 2))
        self.screen.blit(quit_text, (quit_button.x + (quit_button.width - quit_text.get_width()) // 2, quit_button.y + (quit_button.height - quit_text.get_height()) // 2))
        self.draw()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_button.collidepoint(event.pos):
                        return  # Return to the main loop to start a new game
                    elif quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
            self.FPS.tick(30)

if __name__ == "__main__":
    play = Pong(screen)
    play.main()
