# isopod_x Sprite Generation Directive

This document is the production contract for generated 2D pixel-art sprites used by `isopod_x`.

## Purpose

Generated assets must be technically usable in Pygame Community Edition, not merely concept art. The game uses a low-resolution internal canvas, nearest-neighbor scaling, and a crisp retro presentation.

## Visual Direction

- Internal game canvas: **480x270**.
- Rendering: nearest-neighbor upscale.
- Style: crisp retro pixel art with strong silhouettes and readable poses.
- No anti-aliased edges.
- Preserve X's established anatomy, shell segmentation, proportions, outline thickness, palette, appendages, and scale between animation states.
- Sprites normally face **right**. The engine mirrors frames for left-facing movement.

## Master Sprite Grid

Unless another layout is explicitly approved:

- Cell size: **95x95 px**
- Columns: **7**
- Rows: **6**
- Final sheet size: **665x570 px**
- Background: **fully transparent RGBA**
- No padding around the grid
- No text labels
- No dividing lines
- No decorative borders
- No artwork outside cells

Every frame occupies exactly one 95x95 cell.

```python
GRID_SIZE = 95

GRID_MAP = {
    "IDLE":   {"row": 0, "count": 7},
    "RUN":    {"row": 1, "count": 7},
    "JUMP":   {"row": 2, "count": 7},
    "FALL":   {"row": 3, "count": 7},
    "CROUCH": {"row": 4, "count": 7},
    "ROLL":   {"row": 5, "count": 7},
}
```

## Animation Requirements

### General

- Keep the character anchored consistently inside every cell.
- Feet/contact points should not wander unless the animation genuinely requires it.
- Avoid accidental sprite jitter from changing frame bounds.
- Do not change scale, lighting direction, palette, outline thickness, or anatomy between frames.

### IDLE

Use very restrained motion. Stability matters more than constant activity. Small breathing, antenna, leg, or shell shifts are enough.

### RUN

Use clearly readable locomotion with contact, passing, compression, and extension poses. The sequence must loop cleanly.

### JUMP

Use rising/upward poses with a silhouette that clearly communicates ascent.

### FALL

Use descending poses visibly distinct from the jump sequence.

### CROUCH

Lower X's profile while keeping a readable grounded silhouette.

### ROLL

Show X curling into and/or moving as a defensive shell ball. It must remain visually distinct from crouching.

## In-Game Scale

Source cells remain 95x95, but X currently renders at approximately **64x64 px**. Important visual features must survive reduction to this size. Favor strong pixel clusters and silhouettes over tiny details.

## Technical Rules

- Always use true transparency.
- Never use green-screen, white, black, checkerboard, or other simulated backgrounds.
- Preserve hard pixel edges.
- No blur, painterly effects, excessive glow, motion blur, or smooth vector-style outlines.
- Keep loopable animation rows coherent.
- Never change grid dimensions, frame dimensions, row order, frame count, character design, or palette without explicitly noting that the sprite-loading contract must change.

## Future Combat Animations

Controls reserve:

- `J`: melee attacks
- `K`: ranged acid / ranged attack actions

Attack animations do not yet have rows in the six-row sheet. Do not replace an existing row with `ATTACK` or `RANGED`. First define an expanded grid layout that preserves all six current states and update the loader contract accordingly.

## Existing Sprite References

When an existing sprite or sheet is supplied, treat it as canonical. Preserve the character rather than redesigning it. Match pixel density, palette, outlines, proportions, shell geometry, and shading language as closely as possible.

## Preflight Checklist

Before accepting a generated sheet, verify:

- Grid dimensions are correct.
- Every cell is 95x95.
- Frames align exactly to the grid.
- Background is genuinely transparent.
- There are no labels, separators, or decorative elements.
- Character placement is stable between frames.
- Rows match the required state order.
- Artwork remains readable at approximately 64x64.

The goal is production-ready sprites with predictable coordinates and zero cleanup before import into `isopod_x`.
