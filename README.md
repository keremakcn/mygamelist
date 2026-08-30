# 🎮 MyGameList

A personal video game tracking app. Search for games, add them to your library, track your status, rate them yourself, write notes, and mark favorites.

Powered by the [RAWG Video Games Database API](https://rawg.io/apidocs) for game data (Metacritic score, cover art, platforms, genres, developer, publisher). Your personal relationship with a game (status, rating, notes, favorites) is kept completely separate from that data.

Currently built as a single-user app, but the database is designed so it can evolve into a multi-user system (with accounts) later without a rewrite.

---

## ✨ Features

- 🔍 **Game search** — search via the RAWG API, results shown as cards
- 📚 **Personal library** — status tracking (Want to Play / Playing / Played / Dropped)
- ⭐ **Your own rating** — a 0–10 scale, fully independent from Metacritic
- 📝 **Notes** — write your own thoughts on each game
- ❤️ **Favorites** — mark your all-time favorites
- 📅 **Played date** — record when you finished a game
- 🔀 **Filtering & sorting** — filter by status/favorites, sort by name, Metacritic, your rating, or date added
- 🌐 **Bilingual** — Turkish / English, switch instantly
- 🎨 **Custom design** — dark theme, cartridge/HUD-inspired look
- 🛡️ **Resilient error handling** — the app won't crash if the RAWG API fails, returns incomplete data, or the connection drops

---

## 📥 Download (No Setup Required)

If you just want to use the app without touching code:

1. Download the latest `MyGameList.exe` from the [**Releases**](https://github.com/your-username/mygamelist/releases) page.
2. In the same folder, create a file named `.env` and add:
   ```
   RAWG_API_KEY=your_key_here
   ```
3. Get a free RAWG API key at: [rawg.io/apidocs](https://rawg.io/apidocs) — sign up and copy your key.
4. Double-click `MyGameList.exe` — the app opens in its own window, no browser needed.

> 💡 Your library is stored in a file called `games.db`, next to the exe. As long as you keep that file, your data persists.

---

## 🛠️ Running from Source (Developers)

### Requirements
- Python 3.10+
- A free [RAWG API key](https://rawg.io/apidocs)

### Steps

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/mygamelist.git
   cd mygamelist
   ```

2. Create and activate a virtual environment *(recommended, not required)*:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS / Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and add your API key:
   ```
   RAWG_API_KEY=your_key_here
   ```

5. Create the database:
   ```bash
   python database.py
   ```

6. Run the app:
   ```bash
   python app.py
   ```

7. Open in your browser: **http://127.0.0.1:5000**

---

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite |
| Frontend | HTML, CSS, Jinja2 |
| External API | [RAWG Video Games Database](https://rawg.io/apidocs) |
| Desktop packaging | PyWebView + PyInstaller |

---

## 📁 Project Structure

```
mygamelist/
├── app.py                # Flask routes, RAWG API logic
├── database.py            # SQLite connection and queries
├── translations.py        # TR/EN translation strings
├── requirements.txt        # Python dependencies
├── .env.example             # Example environment file
├── .env                        # RAWG API key (not committed)
├── games.db                     # SQLite database (not committed)
├── templates/                    # Jinja2 HTML templates
│   ├── layout.html
│   ├── index.html
│   ├── search.html
│   ├── game.html
│   ├── edit.html
│   └── 404.html
└── static/
    └── style.css
```

---

## 🗄️ Database Design

RAWG's **objective data** and your **personal data** are deliberately split into two tables:

### `games`
Game data pulled from RAWG — name, Metacritic score, platforms, genres, cover art.

### `my_games`
Your relationship with that game — status, your rating, your note, favorite flag, played date.

```
games                    my_games
------                    ---------
id (RAWG id)  ◄──────────  game_id
name                       status
metacritic                 my_rating
platforms                  note
...                        favorite
                           played_date
```

**Why this matters:** if a login system is added later, only the `my_games` table needs a `user_id` column. The `games` table can stay shared across all users, so the same game is never fetched from RAWG twice.

---

## 🗺️ Roadmap

- [x] RAWG API integration and search
- [x] SQLite database, library management
- [x] Filtering and sorting
- [x] TR/EN language support
- [x] Custom design, dark theme
- [x] Desktop `.exe` packaging
- [ ] User accounts (signup/login), multi-user support
- [ ] Web deployment (a version anyone can use with their own account)

---

## 📄 License

Personal project, no license specified.

---

## 🙏 Acknowledgments

Game data provided by the [RAWG Video Games Database API](https://rawg.io/apidocs).
