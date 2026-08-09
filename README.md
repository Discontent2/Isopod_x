# isopod_x

A modular 2D retro platformer prototype built with Python and pygame-ce.

## Current prototype decisions

- Internal render resolution: `480x270`
- Integer window scale: `3x` (`1440x810`)
- Target frame rate: `60 FPS`
- World tile size: `16x16`
- Player animation display size: `64x64`
- Sprite sheet source cells: `95x95`
- Sprite rows: IDLE, RUN, JUMP, FALL, CROUCH, ROLL
- Native PNG alpha transparency via `convert_alpha()`
- Coordinate-separated horizontal/vertical tile collision resolution
- Subpixel vertical movement with a 1-pixel ground probe to keep the grounded/idle state stable

## Controls

- `A/D` or Left/Right: move
- `S` or Down: crouch
- `Space`: jump
- `Left Shift`: toggle shell roll
- `J`: primary melee state hook
- `K`: ranged acid state hook

`ATTACK` and `RANGED` currently fall back visually to IDLE until dedicated sprite rows are added.

## Player sprite sheet

The loader expects:

`assets/sprites/isopod_sheet.png`

The validated replacement sheet is `1300x1323` RGBA. An older `1549x516` asset was too short for the row-5 ROLL frames when slicing 95px grid cells.

## Run

```bash
source venv/bin/activate
python3 main.py
```

The codebase is intentionally modular. Individual scripts should remain below roughly 150-200 lines where practical.
