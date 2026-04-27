# TSIS4 Snake Game

Project structure:

```text
TSIS4_snake/
├── main.py
├── game.py
├── db.py
├── config.py
├── settings.json
├── requirements.txt
└── images/
    ├── PNG_NAMES.txt
    └── .gitkeep
```

## PNG names for `images/`

You can add images later with these exact names:

- `food.png`
- `poison.png`
- `speed.png`
- `slow.png`
- `shield.png`
- `snake_head.png`
- `snake_body.png`
- `obstacle.png`
- `background.png`

If PNG files are missing, the game draws simple colored rectangles automatically.

## How to run

```bash
pip install -r requirements.txt
python main.py
```

## PostgreSQL

Create database `snake_db`, then change login/password in `config.py` if needed.
Tables are created automatically when the game starts.

Suggested database:

```sql
CREATE DATABASE snake_db;
```

The code creates these tables automatically:

```sql
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE game_sessions (
    id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES players(id),
    score INTEGER NOT NULL,
    level_reached INTEGER NOT NULL,
    played_at TIMESTAMP DEFAULT NOW()
);
```

## Controls

- Arrow keys or WASD — move snake
- Enter on menu — start game
- Esc during game — go back to menu
