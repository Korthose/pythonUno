import random

import pygame

from Objects.Card import Card
from testing import randCards


class Deck:
    def __init__(self):
        self.card_width = 180
        self.card_height = 180

        # for deck creation
        self.red = 'Red'
        self.blue = 'Blue'
        self.yellow = 'Yellow'
        self.green = 'Green'
        self.special = 'Special'

        self.player1Cards = []
        self.player2Cards = []
        self.discard_pile = []

        self.cards = []

        # card back graphic for card stack (pull another card)
        self.cardStack = pygame.image.load("Resources/Sprites/Cards/Special/card_back.png").convert_alpha()
        self.cardStack = pygame.transform.scale(self.cardStack, (180, 180))
        self.stackRect = self.cardStack.get_rect()

        # initial Card on the table
        self.initialCard = Card(random.randint(0, 9), random.choice(['Red', 'Blue', 'Yellow', 'Green']))

        self.screen = pygame.display.set_mode((1280, 720))
        # Load the background image
        self.background = pygame.image.load("Resources/Sprites/background.png").convert()
        self.background = pygame.transform.scale(self.background, (1280, 720))

        # Scrolling variables
        self.visible_start_index = 0
        self.visible_cards = 5
        self.scroll_speed = 20
        self.dragging = False
        self.drag_start_x = 0
        self.scroll_offset = 0

        self.font = pygame.font.Font('Resources/Sprites/Font/Tiny5-Regular.ttf', 42)
        self.currentPlayer = 1
        self.plus_two_stack = 0  # Track +2 cards

        # not used color changing variables
        self.color_changing = False
        self.awaiting_second_card = False

    def randColor(self):
        randColour = []

        randColour.extend([self.red] * 21)
        randColour.extend([self.blue] * 21)
        randColour.extend([self.yellow] * 21)
        randColour.extend([self.green] * 21)

        random.shuffle(randColour)
        return randColour

    def randInt(self):
        randNum = []

        randNum.extend([0] * 4)
        randNum.extend([1] * 8)
        randNum.extend([2] * 8)
        randNum.extend([3] * 8)
        randNum.extend([4] * 8)
        randNum.extend([5] * 8)
        randNum.extend([6] * 8)
        randNum.extend([7] * 8)
        randNum.extend([8] * 8)
        randNum.extend([9] * 8)
        randNum.extend([10] * 8)

        random.shuffle(randNum)
        return randNum

    def createDeck(self):
        colors = self.randColor()
        numbers = self.randInt()

        self.stackedCards()

        # 88 - 84 without color change cards

        for i in range(84):
            # make card instance
            self.cards.append(Card(numbers[i], colors[i]))

        # change color cards
        for i in range(4):
            self.cards.append(Card(11, self.special))

        random.shuffle(self.cards)
        # Deal initial hands
        self.pullCards(7, 1)
        self.pullCards(7, 2)
        self.discard_pile.append(self.initialCard)  # Add initial card to discard pile

    def pullCards(self, pulledCard, player):
        # if the stack is empty, fill it again will all discards
        if not self.cards:
            self.reshuffleDeck()

        target_hand = self.player1Cards if player == 1 else self.player2Cards
        for _ in range(min(pulledCard, len(self.cards))):
            target_hand.append(self.cards.pop(0))

    def stackedCards(self):
        self.stackRect.topleft = (((1280 - 180) // 2) + 160, (720 - 180) // 2)
        self.screen.blit(self.cardStack, self.stackRect)

    # redrawing the graphics
    def redraw(self):
        self.screen.blit(self.background, (0, 0))
        self.starter()
        self.stackedCards()
        self.display_player_turn()
        pygame.display.flip()

    # played card, removing for each player
    def cardPlayed(self, matchedCard, event, mouse):
        if self.currentPlayer == 1:
            self.player1Cards.remove(matchedCard)
        else:
            self.player2Cards.remove(matchedCard)
        # Declare played card as next card on table
        self.discard_pile.append(self.initialCard)
        self.initialCard = matchedCard

        # 2+ cards have the number 10 assigned to fit in the system
        # elif would be color cards
        if matchedCard.number == 10:
            next_player = 3 - self.currentPlayer
            self.pullCards(2, next_player)
            self.currentPlayer = 3 - self.currentPlayer
        elif self.awaiting_second_card:
            self.awaiting_second_card = False
        elif matchedCard.color == 'Special':
            self.awaiting_second_card = True

        else:
            self.currentPlayer = 3 - self.currentPlayer  # Switch player (1 becomes 2, 2 becomes 1)

        self.redraw()

    def starter(self):
        start_x = (1280 - (self.visible_cards * self.card_width)) // 2
        start_y = 670 - self.card_width
        self.initialCard.moveTo(((1280 - self.card_width) // 2) - 180, (720 - 180) // 2)
        self.initialCard.draw(self.screen)
        # Draw the current player's hand
        current_hand = self.player1Cards if self.currentPlayer == 1 else self.player2Cards
        num_cards_to_draw = min(self.visible_cards, len(current_hand))
        for i in range(self.visible_start_index,
                       min(self.visible_start_index + num_cards_to_draw, len(current_hand))):
            card = current_hand[i]
            x = start_x + (i - self.visible_start_index) * self.card_width - self.scroll_offset
            y = start_y
            card.moveTo(x, y)
            card.draw(self.screen)

        # Display card counts
        self.display_card_counts(start_x, start_y)

    def scroll_left(self):
        self.visible_start_index = max(0, self.visible_start_index - 1)

    def scroll_right(self):
        current_hand = self.player1Cards if self.currentPlayer == 1 else self.player2Cards
        self.visible_start_index = min(len(current_hand) - self.visible_cards, self.visible_start_index + 1)

    def start_drag(self, mouse_x):
        self.dragging = True
        self.drag_start_x = mouse_x

    def update_drag(self, mouse_x):
        if self.dragging:
            drag_distance = mouse_x - self.drag_start_x
            scroll_amount = -drag_distance  # Invert for correct scroll direction
            self.scroll_offset = scroll_amount

    def end_drag(self):
        self.dragging = False
        current_hand = self.player1Cards if self.currentPlayer == 1 else self.player2Cards
        self.visible_start_index -= int(self.scroll_offset / self.card_width)
        self.visible_start_index = max(0, min(len(current_hand) - self.visible_cards, self.visible_start_index))
        self.scroll_offset = 0

    # text for player, card count
    def display_card_counts(self, start_x, start_y):
        current_hand = self.player1Cards if self.currentPlayer == 1 else self.player2Cards
        cards_left = self.visible_start_index
        cards_right = len(current_hand) - (
                self.visible_start_index + min(self.visible_cards, len(current_hand) - self.visible_start_index))
        cards_remaining = len(current_hand)

        text_left = self.font.render(f"<- {cards_left}", True, (0, 0, 0))
        text_right = self.font.render(f"{cards_right} ->", True, (0, 0, 0))
        text_remaining = self.font.render(f"Verbleibend: {cards_remaining}", True, (0, 0, 0))

        text_left_pos = (
            start_x - 10 - text_left.get_width(), start_y + self.card_height // 2 - text_left.get_height() // 2)
        text_right_pos = (
            start_x + self.visible_cards * self.card_width + 10,
            start_y + self.card_height // 2 - text_right.get_height() // 2)
        text_remaining_pos = (950, 360)


        self.screen.blit(text_left, text_left_pos)
        self.screen.blit(text_right, text_right_pos)
        self.screen.blit(text_remaining, text_remaining_pos)

    def display_player_turn(self):
        turn_text = self.font.render(f"Spieler {self.currentPlayer}'s Zug", True, (0, 0, 0))
        turn_text_pos = (10, 10)
        self.screen.blit(turn_text, turn_text_pos)

    def reshuffleDeck(self):
        if len(self.discard_pile) > 1:

            # save current top card
            top_card = self.discard_pile[-1]
            self.discard_pile.remove(top_card)

            # assign discard pile to cards
            self.cards = self.discard_pile[:]
            self.discard_pile = [top_card]
            random.shuffle(self.cards)
        else:
            print("No cards to reshuffle!")