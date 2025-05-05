# python-cli-rhythm-game
rhythm game made a while back for a cli project

# Terminal Rhythm Game

This is a terminal-based rhythm game where notes fall down a grid and you press keys in time to score points. The game also features a shop, settings, and a high score screen.

## How to Play

- Notes fall down a 4-column grid.
- Use the following keys to hit notes in each column:
  - 's' for column 1
  - 'd' for column 2
  - 'j' for column 3
  - 'k' for column 4
- Time your key presses to hit notes as they reach the bottom row.
- Earn 10 points per correct note.
- Missed notes are tracked and shown at the end.

## Features

- Shop system to buy new note colors using your score.
- Settings room to change game speed and note color.
- Arcade room to play the game.
- High score display after each round.
- Uses threading for real-time key press detection.
- Colored notes using the `termcolor` module.

## Requirements

- Python 3.x
- termcolor
- keyboard

Install the required modules with: pip install termcolor keyboard

## Controls

- 's', 'd', 'j', 'k': Hit notes
- 'q': Quit game
- Type responses to navigate menus and rooms

## Files

All game logic is contained in one Python file. Just run the script to get started: py rhythmGame.py

## Notes

- Game runs in the terminal using `cls` to clear the screen, so it works best on Windows.
- You can customize note colors and speed in the settings room.
- New note colors are unlocked by spending score points in the shop.
