# Pixel Runner 🎮

Pixel Runner is a simple 2D runner game made with **Python** and **Pygame**.  
The idea is easy: the player runs forward, jumps over enemies, and tries to survive as long as possible. The longer you stay alive, the higher your score becomes.

This project was created as a student game project to practice Python basics, game loops, sprites, collision detection, animation, sound, and project structure.

---

## What the game does

- Shows an intro screen before the game starts
- Starts the game when the player presses **Space**
- Lets the player jump using **Space**
- Spawns obstacles like snails and flies
- Moves obstacles from right to left
- Checks collision between the player and obstacles
- Counts the score based on survival time
- Plays background music and jump sound
- Shows the final score after losing


## Technologies used

- **Python** — main programming language
- **Pygame** — library for creating the game window, drawing images, handling keyboard input, sounds, sprites, and collision
- **Sprites** — used for the player and obstacles
- **Timers** — used to spawn enemies and animate them
- **Images and audio files** — used to make the game look and feel like a real small game

## Project files

The game needs folders like this:

text
project-folder/
│
├── Final.py
├── README.md
│
├── graphics/
│   ├── Sky.png
│   ├── ground.png
│   ├── player/
│   │   ├── player_walk_1.png
│   │   ├── player_walk_2.png
│   │   ├── jump.png
│   │   └── player_stand.png
│   ├── snail/
│   │   ├── snail1.png
│   │   └── snail2.png
│   └── fly/
│       ├── fly1.png
│       └── fly2.png
│
├── audio/
│   ├── music.wav
│   └── jump.mp3
│
└── font/
    └── Pixeltype.ttf
```

---

## How to run the game

First install Pygame:

```bash
pip install pygame
```

Then run the game:

```bash
python tutorial.py
```

On macOS, sometimes you may need:

```bash
python3 tutorial.py
```

---

## Controls

| Key | Action |
|---|---|
| Space | Start the game |
| Space | Jump |
| Close button | Quit the game |

---

## Main code idea

The game works inside a main loop. Every second, the program checks events, updates the player, moves obstacles, checks collisions, draws everything on the screen, and updates the display.

The player and obstacles are made using Pygame sprite classes. This makes the code cleaner because each object has its own image, position, movement, animation, and update logic.

---

## What I learned from this project

While making this game, I practiced:

- creating a game window with Pygame
- loading images, fonts, and sounds
- using classes and objects
- using sprite groups
- making a character jump with gravity
- creating simple animation
- spawning random obstacles
- detecting collisions
- using timers and events
- organizing code into functions and classes


## Future improvements

Some possible improvements for the game:

- add restart button on the screen
- add different difficulty levels
- make obstacles faster over time
- save the highest score
- add coins or power-ups
- add a better menu screen
- add more enemy types
проверь этот реадми
