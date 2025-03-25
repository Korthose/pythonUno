import pygame

class Card():
    def __init__(self, number, color):
        self.CARD_WIDTH = 180
        self.CARD_HEIGHT = 180
        self.number = number
        self.color = color

        #load sprite through given color- and number parameters
        path = "Resources/Sprites/Cards/" + str(self.color) + "/card_" + str(self.number) + ".png"
        self.card = pygame.image.load(path).convert_alpha()
        self.card = pygame.transform.scale(self.card, (self.CARD_WIDTH, self.CARD_HEIGHT))


        self.rect = self.card.get_rect()

    def playing(self, event, objective, mouse, color_changing):
        if event.button == 1 and pygame.Rect.collidepoint(self.rect, mouse):
            if self.color != objective.color:
                if self.color != 'Special':
                    if self.number != objective.number:
                        if self.number != 10:
                            print("The cards are not matching")
                            return False
                        else:
                            print('+2 card played')
                            return 'plus_two'
                    else:
                        print('matched')
                        return True
                else:
                    print('Color change card played')
                    return 'color_change'
            else:
                print('matched')
                return True
        return False

    def moveTo(self, x, y):
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.card, self.rect)