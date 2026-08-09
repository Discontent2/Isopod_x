"""Animated player entity for isopod_x."""

from pathlib import Path

import pygame

import config


GRID_SIZE = 95
GRID_MAP = {
    "IDLE": {"row": 0, "count": 1},
    "RUN": {"row": 1, "count": 7},
    "JUMP": {"row": 2, "count": 7},
    "FALL": {"row": 3, "count": 7},
    "CROUCH": {"row": 4, "count": 7},
    "ROLL": {"row": 5, "count": 7},
}


class Player(pygame.sprite.Sprite):
    """Controllable isopod with animation and tile collisions."""

    SPEED = 2
    ROLL_SPEED = 4
    GRAVITY = 0.5
    JUMP_STRENGTH = -8
    FRAME_SIZE = 64
    FRAME_DURATION_MS = 90

    def __init__(self) -> None:
        super().__init__()
        self.animations = self._load_frames()
        self.state = "IDLE"
        self.animation_index = 0
        self.last_frame_time = pygame.time.get_ticks()
        self.facing_left = False
        self.roll_active = False
        self._shift_was_down = False
        self._jump_was_down = False

        self.image = self.animations["IDLE"][0]
        self.rect = self.image.get_rect(
            center=(
                config.SCREEN_WIDTH // 2,
                config.SCREEN_HEIGHT // 2,
            )
        )
        self.vx = 0
        self.vy = 0.0
        self.y = float(self.rect.y)
        self.on_ground = False

    def _load_frames(self) -> dict[str, list[pygame.Surface]]:
        """Extract animations from the uniform 95px grid."""
        sheet_path = (
            Path(__file__).resolve().parents[1]
            / "assets"
            / "sprites"
            / "isopod_sheet.png"
        )
        sheet = pygame.image.load(str(sheet_path)).convert_alpha()
        sheet_width, sheet_height = sheet.get_size()
        animations: dict[str, list[pygame.Surface]] = {}

        for state, data in GRID_MAP.items():
            frames: list[pygame.Surface] = []
            for frame_index in range(data["count"]):
                frame_rect = pygame.Rect(
                    frame_index * GRID_SIZE,
                    data["row"] * GRID_SIZE,
                    GRID_SIZE,
                    GRID_SIZE,
                )
                if (
                    frame_rect.right > sheet_width
                    or frame_rect.bottom > sheet_height
                ):
                    raise ValueError(
                        f"{state} frame {frame_index} exceeds "
                        f"sprite sheet bounds {sheet.get_size()}."
                    )
                frame = sheet.subsurface(frame_rect).copy()
                frames.append(
                    pygame.transform.scale(
                        frame,
                        (self.FRAME_SIZE, self.FRAME_SIZE),
                    )
                )
            animations[state] = frames
        return animations

    def _set_state(self, new_state: str) -> None:
        if new_state == self.state:
            return
        self.state = new_state
        self.animation_index = 0
        self.last_frame_time = pygame.time.get_ticks()

    def _update_animation(self) -> None:
        visual_state = self.state if self.state in self.animations else "IDLE"
        frames = self.animations[visual_state]
        now = pygame.time.get_ticks()
        elapsed = now - self.last_frame_time

        if elapsed >= self.FRAME_DURATION_MS:
            steps = elapsed // self.FRAME_DURATION_MS
            self.animation_index = (
                self.animation_index + steps
            ) % len(frames)
            self.last_frame_time += steps * self.FRAME_DURATION_MS

        frame = frames[self.animation_index]
        self.image = pygame.transform.flip(
            frame,
            self.facing_left,
            False,
        )

    def _read_input(self) -> tuple[bool, bool, bool]:
        keys = pygame.key.get_pressed()
        move_left = keys[pygame.K_LEFT] or keys[pygame.K_a]
        move_right = keys[pygame.K_RIGHT] or keys[pygame.K_d]
        crouching = keys[pygame.K_DOWN] or keys[pygame.K_s]

        shift_down = keys[pygame.K_LSHIFT]
        if shift_down and not self._shift_was_down:
            self.roll_active = not self.roll_active
        self._shift_was_down = shift_down

        jump_down = keys[pygame.K_SPACE]
        if jump_down and not self._jump_was_down and self.on_ground:
            self.vy = self.JUMP_STRENGTH
            self.on_ground = False
        self._jump_was_down = jump_down

        direction = int(move_right) - int(move_left)
        if direction < 0:
            self.facing_left = True
        elif direction > 0:
            self.facing_left = False

        speed = self.ROLL_SPEED if self.roll_active else self.SPEED
        self.vx = direction * speed
        if crouching and not self.roll_active:
            self.vx = 0

        return crouching, keys[pygame.K_j], keys[pygame.K_k]

    def _resolve_state(
        self,
        crouching: bool,
        attacking: bool,
        ranged: bool,
    ) -> None:
        if attacking:
            self._set_state("ATTACK")
        elif ranged:
            self._set_state("RANGED")
        elif self.roll_active:
            self._set_state("ROLL")
        elif not self.on_ground and self.vy < 0:
            self._set_state("JUMP")
        elif not self.on_ground:
            self._set_state("FALL")
        elif crouching:
            self._set_state("CROUCH")
        elif self.vx:
            self._set_state("RUN")
        else:
            self._set_state("IDLE")

    def update(
        self,
        tiles_group: pygame.sprite.AbstractGroup,
    ) -> None:
        tile_rects = [tile.rect for tile in tiles_group]
        crouching, attacking, ranged = self._read_input()

        self.rect.x += self.vx
        hit = self.rect.collidelist(tile_rects)
        if hit != -1:
            tile = tile_rects[hit]
            if self.vx > 0:
                self.rect.right = tile.left
            elif self.vx < 0:
                self.rect.left = tile.right

        self.vy += self.GRAVITY
        self.y += self.vy
        self.rect.y = round(self.y)
        self.on_ground = False

        hit = self.rect.collidelist(tile_rects)
        if hit != -1:
            tile = tile_rects[hit]
            if self.vy > 0:
                self.rect.bottom = tile.top
                self.on_ground = True
            elif self.vy < 0:
                self.rect.top = tile.bottom
            self.vy = 0
            self.y = float(self.rect.y)
        elif self.vy >= 0:
            ground_probe = self.rect.move(0, 1)
            if ground_probe.collidelist(tile_rects) != -1:
                self.on_ground = True
                self.vy = 0
                self.y = float(self.rect.y)

        self._resolve_state(crouching, attacking, ranged)
        self._update_animation()
