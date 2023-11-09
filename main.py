# This is a basic pygbag template that creates a window as big as we can, and calls an external file called Game
# which has a play method

import asyncio
import pygame
import sys
from Game import Game

pygame.init()

# Detect the size of the viewport
screen = pygame.display.set_mode()  # Default to screen resolution.
area = screen.get_rect()

# Create the screen
screen = pygame.display.set_mode((area.width, area.height), pygame.RESIZABLE)

game = Game(screen)
game.setup()
game_state = game.play


async def main():
    global game_state

    while game_state:
        events = pygame.event.get()

        game_state = game.play(events)

        for event in events:
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                game_state = None

        pygame.display.update()
        await asyncio.sleep(0)

    # Closing the game. not strictly required, neither on desktop
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    asyncio.run(main())
