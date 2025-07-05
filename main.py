import pygame
import constants


def main():
    pygame.init()  # Initialize pygame

    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )  # Set the screen size

    # Colors
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    black = (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill the screen with black
        screen.fill(black)


if __name__ == "__main__":
    main()
