# Repository Structure

## Runtime assets

`assets/` contains files loaded by the game at runtime. Production sprites belong under `assets/sprites/`; future audio, UI, VFX, tiles, and other runtime media should use dedicated subfolders. Files in this tree must obey the game's loader contracts.

## Art specifications

`docs/art/` contains technical art contracts such as sprite-grid dimensions, frame ordering, transparency requirements, palette/readability rules, and character visual specifications.

## Design specifications

`docs/design/` contains gameplay and systems documentation, including the living Peashooter and Essence progression system.

## Reference art

`docs/reference_art/` contains concept and visual-reference imagery only. It is not loaded by the game and should not be treated as production-ready sprite data unless a file is explicitly promoted into `assets/`.

The PNGs currently stored in `docs/reference_art/` are compact repository previews derived from the generated design references. They preserve the important visual direction while keeping the repository lightweight. Future production sprite sheets should be exported separately at their exact loader dimensions and placed under `assets/`.
