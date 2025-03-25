import random
import pygame
from socket import *
from pygame.locals import *
from Objects.Card import Card
from Objects.Deck import Deck

# variables
cards = []
Deck = Deck()

# Initialise screen
pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Python')

# Fill background
background = pygame.image.load("Resources/Sprites/background.png").convert()
backgroundRect = pygame.transform.scale(background, (1280, 720))

screen.blit(backgroundRect, (0, 0))

# Initial deck creation
Deck.createDeck()
Deck.starter()

Deck.display_player_turn()  # Add this line
pygame.display.flip()

# Event loop
while True:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and pygame.Rect.collidepoint(Deck.stackRect, mouse):
                Deck.pullCards(1, Deck.currentPlayer)
                Deck.currentPlayer = 3 - Deck.currentPlayer  # Switch player
                Deck.redraw()
            else:
                current_hand = Deck.player1Cards if Deck.currentPlayer == 1 else Deck.player2Cards
                for playerCard in list(current_hand):
                    played_card_action = playerCard.playing(event, Deck.initialCard, mouse,
                                                          Deck.color_changing)
                    if played_card_action:
                        Deck.cardPlayed(playerCard, event, mouse)  # Place the card
                        if played_card_action == 'plus_two':
                            next_player = 3 - Deck.currentPlayer
                            Deck.pullCards(2, next_player)
                        elif played_card_action == 'color_change':
                            Deck.color_changing = True
                        Deck.redraw()
                        break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Deck.scroll_left()
                Deck.redraw()
            elif event.key == pygame.K_RIGHT:
                Deck.scroll_right()
                Deck.redraw()

    pygame.display.update()
