import pygame.sprite
import pygame

class Card():
    def __init__(self, number, color):
        CARD_WIDTH = 32
        CARD_HEIGHT = 32
        super().__init__()
        self.image = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
        self.rect = self.image.get_rect()
        self.number = number
        self.colour = color

        #graphics
        path = "Resources/Sprites/Cards/" + str(self.colour) + "/card_" + str(self.number) + ".png"
        self.card = pygame.image.load(path).convert_alpha()
        self.card = pygame.transform.scale(self.card, (CARD_WIDTH, CARD_HEIGHT))

        self.cardRect = self.card.get_rect()

    def moveTo(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        surface.blit(self.card, self.cardRect)
