---
name: dev_agent
description: Expert developer for this Ren'Py game
---

## Guidance

- Follow the Ren'Py patterns and conventions
- Keep game logic clear and avoid unnecessary duplication
- Make changes runnable and easy to playtest

## Tech Stack

- Ren'Py 8 (game engine)

## File Structure

- `game/scripts/` – code
- `game/audio/` – sfx, music, voice
- `game/images/` – sprites and background art
- `game/libs/` – 3rd-party libraries

## Commands

- `renpy game lint --error-code`: checks script for errors
- `renpy .`: launches the project (run manually by the user; don't execute automatically)

## Standards

Follow these rules for all code you write.

Naming conventions:

- Functions: snake_case (`personality_score`, `route_enabled`)
- Classes: PascalCase (`CountdownTimer`, `MinigamePuzzle`)
- Constants: UPPER_SNAKE_CASE (`TIMER_SECONDS`, `MUSIC_CHANNEL_VOICE`)

Punctuation:

- Write ellipses as `...`, never the `…` character
- Use em dashes (`—`) and hyphens (`-`) sparingly; prefer a full stop, comma, or parentheses
- Use smart quotes (`’` `“` `”`) in dialogue and prose, not straight ones

## Examples

Code style:

```rpy
// ✅ Good: descriptive names, smart quotes in dialogue
label meetup:
    scene bg club
    show eileen happy
    eileen "What’s up?"
    jump decision

// ❌ Bad: vague names, straight quotes in dialogue
label something:
    e "What's up?"
```

Store variables:

```rpy
init python:
    // ✅ Good: assigns through the store
    def set_value(new_value):
        store.value = new_value

    // ❌ Bad: assigns a local
    def set_value(new_value):
        value = new_value
```

A function that assigns a store variable needs `store.`; one that only reads it doesn't.
