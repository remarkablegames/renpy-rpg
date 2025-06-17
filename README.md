<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/renpy-roguelike/master/game/gui/window_icon.png" alt="Ren'Py Roguelike">
</p>

# Ren'Py Roguelike

![release](https://img.shields.io/github/v/release/remarkablegames/renpy-roguelike)
[![build](https://github.com/remarkablegames/renpy-roguelike/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/renpy-roguelike/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/renpy-roguelike/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/renpy-roguelike/actions/workflows/lint.yml)

⚔️ Ren'Py Roguelike Template.

Play the game on:

- [remarkablegames](https://remarkablegames.org/renpy-roguelike)

## Credits

### Art

- [Uncle Mugen](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)

### Audio

### Audio

- [Heal Up](https://pixabay.com/sound-effects/heal-up-39285/)
- [Health Pickup](https://pixabay.com/sound-effects/health-pickup-6860/)
- [Heartbeat 01 - BRVHRTZ](https://pixabay.com/sound-effects/heartbeat-01-brvhrtz-225058/)
- [Kenney Interface Sounds](https://kenney.nl/assets/interface-sounds)
- [Punch Sound Effects](https://pixabay.com/sound-effects/punch-sound-effects-28649/)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

Check the version:

```sh
renpy --version
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/renpy-roguelike.git
cd renpy-roguelike
```

Rename the project:

```sh
git grep -l 'Renpy Roguelike' | xargs sed -i '' -e 's/Renpy Roguelike/My Game/g'
```

```sh
git grep -l 'renpy-roguelike' | xargs sed -i '' -e 's/renpy-roguelike/my-game/g'
```

Replace the assets:

- [ ] `web-presplash.jpg`
- [ ] `game/gui/main_menu.png`
- [ ] `game/gui/window_icon.png`

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Press `Shift`+`D` to open the developer menu.

## Cache

Clear the cache:

```sh
find game -name "*.rpyc" -delete
```

Or open `Ren'Py Launcher` > `Force Recompile`:

```sh
renpy
```

## Lint

Lint the game:

```sh
renpy game lint
```

## License

[MIT](LICENSE)
