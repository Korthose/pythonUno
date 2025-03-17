import pygame

class Card():
    def __init__(self, number, color):
        self.CARD_WIDTH = 180
        self.CARD_HEIGHT = 180
        self.number = number
        self.color = color

        #graphics
        path = "Resources/Sprites/Cards/" + str(self.color) + "/card_" + str(self.number) + ".png"
        self.card = pygame.image.load(path).convert_alpha()
        self.card = pygame.transform.scale(self.card, (self.CARD_WIDTH, self.CARD_HEIGHT))

        # Use self.card's rect for BOTH positioning and blitting
        self.rect = self.card.get_rect()

    def playing(self, event, objective, mouse):
        if event.button == 1 and pygame.Rect.collidepoint(self.rect, mouse):
            if self.color is not objective.color:
                if self.number is not objective.number:
                    print("The cards are not matching")
                    return False
                else:
                    print('matched')
                    return True
            else:
                print('matched')
                return True

    def moveTo(self, x, y):
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.card, self.rect)