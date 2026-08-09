"""Tile-based level generation for isopod_x."""

import pygame

import config


class Level:
    """Create and draw a simple tile-based test level."""

    def __init__(self) -> None:
        self.tiles = pygame.sprite.Group()
        columns = config.SCREEN_WIDTH // config.TILE_SIZE
        rows = config.SCREEN_HEIGHT // config.TILE_SIZE
        self.level_map = ["0" * columns for _ in range(rows)]
        self.level_map.append("1" * columns)
        self.generate_level()

    def generate_level(self) -> None:
        """Build solid tile sprites from the text matrix."""
        self.tiles.empty()

        for row_index, row in enumerate(self.level_map):
            for column_index, tile_code in enumerate(row):
                if tile_code != "1":
                    continue

                tile = pygame.sprite.Sprite()
                tile.image = pygame.Surface(
                    (config.TILE_SIZE, config.TILE_SIZE)
                )
                tile.image.fill(config.GRAY)
                tile.rect = tile.image.get_rect(
                    topleft=(
                        column_index * config.TILE_SIZE,
                        row_index * config.TILE_SIZE,
                    )
                )
                self.tiles.add(tile)

    def draw(self, surface: pygame.Surface) -> None:
        """Draw all solid level tiles."""
        self.tiles.draw(surface)
