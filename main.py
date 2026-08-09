"""Main entry point for isopod_x."""

import sys

import pygame

from config import (
    FPS,
    NAVY,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
from entities.player import Player
from world.level import Level


def handle_events() -> None:
    """Process window events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def draw(
    canvas: pygame.Surface,
    window: pygame.Surface,
    level: Level,
    sprites: pygame.sprite.Group,
) -> None:
    """Draw the low-res world and scale it to the display."""
    canvas.fill(NAVY)
    level.draw(canvas)
    sprites.draw(canvas)

    scaled_canvas = pygame.transform.scale(
        canvas,
        (WINDOW_WIDTH, WINDOW_HEIGHT),
    )
    window.blit(scaled_canvas, (0, 0))
    pygame.display.flip()


def main() -> None:
    """Initialize pygame and run the main loop."""
    pygame.init()

    window = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT)
    )
    pygame.display.set_caption("isopod_x")

    canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    level = Level()
    player = Player()
    all_sprites = pygame.sprite.Group(player)

    while True:
        handle_events()
        all_sprites.update(level.tiles)
        draw(canvas, window, level, all_sprites)
        clock.tick(FPS)


if __name__ == "__main__":
    main()
