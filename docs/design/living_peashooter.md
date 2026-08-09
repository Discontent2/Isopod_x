# Living Peashooter and Essence System

This document captures the ranged-weapon concept established for `isopod_x`.

## Core Idea

X's default ranged weapon is not a conventional firearm. The **Peashooter** is a small living alien isopod-like organism that acts as a symbiotic hand-cannon.

When not in use, it can crawl independently and normally lives attached to X's abdomen. When X draws it, the creature crawls or transfers to one of X's hands and **latches directly onto the hand/forearm** using gripping legs and underside hooks.

The weapon should visually read as both:

1. a tiny isopod creature, and
2. a compact alien gun.

## Peashooter Visual Identity

- Miniature isopod body plan.
- Segmented chitin shell with overlapping plates.
- Silver-gray / bone-gray palette tied to X.
- Short antennae or feelers.
- Small dark or essence-lit eyes.
- Tiny mandible-like structures forming the muzzle.
- Purple bio-essence glow inside the mouth/barrel.
- Small gripping limbs, clasping appendages, or hooks on the underside.
- Curled abdomen / clinging belly structure that explains how it perches on X when holstered.
- Small red `X` accent tying it visually to X's gear.
- Compact silhouette that remains readable at gameplay scale.

The firing end should feel like a creature opening its mouth rather than a conventional machined barrel.

## Drawn / Firing Behavior

When drawn:

- the Peashooter clamps onto one hand,
- X extends that arm forward in a classic side-scroller blaster stance,
- the creature's shell and gripping legs remain visibly distinct from X's arm,
- purple essence shots emerge from the mouth-like muzzle.

The living weapon should not simply turn X's arm into a generic arm cannon. It must remain visibly recognizable as a separate creature latched onto him.

## Holstered Behavior

When not in combat, the Peashooter normally lives on X's abdomen rather than in a normal physical holster.

Potential presentation/animation ideas:

- idle leg movement while attached,
- antenna twitching,
- crawling from abdomen to hand during weapon draw,
- curling tightly against X while stored,
- reacting to nearby essence or loot.

## Essence Progression

The Peashooter evolves through **Essence** collected during play.

Current concept:

- kills provide essence,
- defeated players can be looted for their essence,
- essence points are spendable,
- essence can purchase attachments,
- essence can also trigger larger biological morphs that transform the weapon into substantially different gun forms,
- morphing/upgrading can happen **on the fly** rather than requiring a traditional gunsmith screen.

The visual fantasy is that the creature consumes essence and physically grows or rearranges its shell, organs, and weapon structures.

## Upgrade Language

Potential attachment/evolution concepts established during design exploration include:

- essence chamber / essence canister,
- living shell reinforcement,
- flexible mandibles,
- antenna sight,
- shell scope,
- toxin sac,
- barrel growth,
- spore bloom,
- adaptive pods,
- essence overdrive,
- chitin stock.

These are working concepts, not a finalized upgrade tree.

## Morphing Philosophy

Small upgrades should feel like attachments grown or attached to the living organism. Major upgrades may morph the Peashooter into a substantially different weapon class while preserving recognizable biological traits.

A major morph should preserve at least some recurring identity markers such as:

- shell segmentation,
- antennae,
- mandible muzzle geometry,
- essence glow,
- red `X` ownership marking.

The result should feel like the same organism evolving, not a completely unrelated gun appearing from inventory.

## Craftable Equipment

Essence also supports craftable carry items. Current concept space includes alien-biotech grenades and mines that share the same chitin/essence visual language.

Possible grenade concepts:

- essence grenade,
- toxin/spore grenade,
- spike/fragmentation pod.

Possible mine concepts:

- claw/proximity mine,
- burrow/delayed-emerge mine,
- spine/directional-burst mine.

These names and exact behaviors are provisional, but all crafted equipment should look biologically related to the Peashooter ecosystem rather than conventional military hardware.

## Gameplay / Art Contract

Future ranged sprites should preserve the existing six-row player animation sheet unless an expanded layout is explicitly designed. Do not silently replace an existing player animation row with shooting frames.

When ranged attack animation is implemented, define a loader-compatible expansion for the existing sprite contract and keep right-facing source art as the default orientation.
