import pygame

class Card():
    def __init__(self, number, color):
        CARD_WIDTH = 180
        CARD_HEIGHT = 180
        self.number = number
        self.color = color

        #graphics
        path = "Resources/Sprites/Cards/" + str(self.color) + "/card_" + str(self.number) + ".png"
        self.card = pygame.image.load(path).convert_alpha()
        self.card = pygame.transform.scale(self.card, (CARD_WIDTH, CARD_HEIGHT))

        # Use self.card's rect for BOTH positioning and blitting
        self.rect = self.card.get_rect()

    def playing(self, event, objective):
        # and self.rect.contains(event.pos)
        if event.button == 1 and self.rect.contains(event.pos):    # if cards do not match
            if self.color is not objective.color or self.number is not objective.number:
                print("The cards are not matching")
                return False
            else:
                return True


    def moveTo(self, x, y):
        self.rect.topleft = (x, y) # Use topleft for positioning

    def draw(self, surface):
        surface.blit(self.card, self.rect)