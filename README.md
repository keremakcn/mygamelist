# 🎮 MyGameList

A personal video game tracking application built with **Python, Flask, SQLite, PyWebView, and PyInstaller**.

MyGameList lets you search for games, add them to your personal library, track your playing status, rate games, write notes, record played dates, and mark your favorite games.

Game information such as cover art, platforms, genres, developers, publishers, and Metacritic scores is provided by the **RAWG Video Games Database API**. Your personal library information is stored locally and kept separate from the external game data.

---

## ✨ Features

* 🔍 **Game search** — Search for games using the RAWG API
* 📚 **Personal library** — Add and manage games in your collection
* 🎮 **Status tracking** — Track games as:

  * Want to Play
  * Playing
  * Played
  * Dropped
* ⭐ **Personal rating** — Rate games on your own 0–10 scale
* 📝 **Notes** — Write your own notes and thoughts about games
* ❤️ **Favorites** — Mark games as favorites
* 📅 **Played date** — Record when you finished a game
* 🔀 **Filtering & sorting** — Filter and sort your library in different ways
* 🌐 **Bilingual interface** — Turkish / English language support
* 🎨 **Custom design** — Dark theme with a game cartridge / HUD-inspired interface
* 🛡️ **Error handling** — Handles API failures, incomplete data, and connection problems without crashing
* 🖥️ **Desktop application** — Runs as a standalone Windows application
* 💾 **Local data storage** — Your personal library is stored locally in SQLite

---

# 📥 Download & Installation

## 🪟 Windows

You do **not** need Python or any programming knowledge to use the Windows version.

### 1. Download MyGameList

Go to the **[Releases](https://github.com/your-username/mygamelist/releases)** page and download the latest:

```text
MyGameList-v1.0.0.zip
```

### 2. Extract the ZIP

Extract the ZIP file to a location of your choice.

It is recommended to keep the entire application inside its own folder:

```text
MyGameList/
├── MyGameList.exe
├── ...
└── ...
```

**Do not move or delete individual files from this folder.**

The application may create additional files and folders while it is running, so keeping the complete folder together is important.

### 3. Start the application

Open:

```text
MyGameList.exe
```

The application will open in its own desktop window.

No browser is required.

---

# 🔑 First-Time Setup — RAWG API Key

MyGameList uses the **RAWG Video Games Database API** to retrieve game information.

A RAWG API key is required for the application to search for and retrieve game data. RAWG's API documentation states that an API key must be included with API requests.

**You only need to do this during the initial setup.**

### Step 1 — Open the application

Run:

```text
MyGameList.exe
```

If an API key has not been configured yet, MyGameList will display a setup screen explaining that an API key is required.

### Step 2 — Create a RAWG account

The application provides a link to the RAWG website.

Open the link and create a free RAWG account if you do not already have one.

### Step 3 — Get your API key

After creating/logging into your RAWG account, go to the RAWG API page:

**[RAWG API Documentation](https://rawg.io/apidocs)**

RAWG provides API keys through its API service.

Copy your API key.

### Step 4 — Enter the API key in MyGameList

Return to MyGameList and paste the API key into the API key field.

Save/continue to complete the setup.

After the API key is configured, you can start searching for games and using the application normally.

> 🔐 **Your API key is personal. Do not share it publicly or upload it to GitHub.**

---

# 🎮 Using MyGameList

Once the setup is complete, you can start building your game library.

### 🔍 Search

Use the search bar to find games through the RAWG database.

Search results can include information such as:

* Cover art
* Metacritic score
* Platforms
* Genres
* Developer
* Publisher

### 📚 Add a game

Open a game from the search results and add it to your personal library.

The game's external information and your personal library information are stored separately.

### 🎯 Manage your library

For games in your library, you can:

* Change the game status
* Add your own rating
* Write notes
* Mark the game as a favorite
* Record the played date
* Edit information
* Remove the game from your library

### 🔀 Filter and sort

Your library can be filtered and sorted according to different criteria, including:

* Status
* Favorites
* Game name
* Metacritic score
* Personal rating
* Date added

---

# 💾 Your Data

MyGameList stores your personal library locally.

The main database file is:

```text
games.db
```

This database contains information such as:

* Games in your library
* Your ratings
* Your notes
* Favorite status
* Playing status
* Played dates

Your library is **not stored on a MyGameList online account**.

### ⚠️ Important

Keep the complete `MyGameList` folder together.

Do not delete:

```text
games.db
```

if you want to keep your library.

It is also recommended to make a backup of your application folder if your library is important to you.

---

# 🛠️ Running from Source

If you want to inspect, modify, or develop MyGameList, you can run it directly from the source code.

## Requirements

* Python 3.10+
* Git
* A RAWG API key

## 1. Clone the repository

```bash
git clone https://github.com/your-username/mygamelist.git
cd mygamelist
```

## 2. Create a virtual environment

Recommended:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure the RAWG API key

Create a `.env` file in the project root:

```env
RAWG_API_KEY=your_key_here
```

**Do not commit your `.env` file to GitHub.**

The repository contains `.env.example` as a template.

## 5. Initialize the database

```bash
python database.py
```

## 6. Run the application

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

in your browser.

---

# 🧱 Tech Stack

| Layer          | Technology                    |
| -------------- | ----------------------------- |
| Backend        | Python, Flask                 |
| Database       | SQLite                        |
| Frontend       | HTML, CSS, Jinja2             |
| External API   | RAWG Video Games Database API |
| Desktop Window | PyWebView                     |
| Packaging      | PyInstaller                   |

---

# 📁 Project Structure

```text
mygamelist/
├── app.py                 # Flask routes and RAWG API logic
├── database.py            # SQLite database setup and queries
├── translations.py        # Turkish / English translations
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment configuration
├── templates/             # Jinja2 HTML templates
│   ├── layout.html
│   ├── index.html
│   ├── search.html
│   ├── game.html
│   ├── edit.html
│   └── 404.html
└── static/
    └── style.css
```

Local files such as `.env`, `games.db`, configuration files, and application-generated data are not included in the Git repository.

---

# 🗄️ Database Design

MyGameList deliberately separates **external game data** from the user's **personal game data**.

### `games`

Stores game information retrieved from RAWG, such as:

* RAWG ID
* Name
* Metacritic score
* Platforms
* Genres
* Developer
* Publisher
* Cover art

### `my_games`

Stores the user's personal relationship with each game:

* Status
* Personal rating
* Notes
* Favorite status
* Played date

Conceptually:

```text
games                         my_games
------                        ---------
id (RAWG id)  ◄────────────── game_id
name                          status
metacritic                    my_rating
platforms                     note
genres                        favorite
...                           played_date
```

This separation means that external game information and personal library information remain independent.

It also provides a foundation for a future multi-user system. A future `user_id` could be added to `my_games` while the shared `games` table remains reusable.

---

# 🗺️ Roadmap

## ✅ Completed

* [x] RAWG API integration
* [x] Game search
* [x] Personal game library
* [x] Game status tracking
* [x] Personal ratings
* [x] Notes
* [x] Favorites
* [x] Played dates
* [x] Filtering and sorting
* [x] Turkish / English language support
* [x] Custom dark interface
* [x] Error handling
* [x] Desktop application packaging
* [x] Windows `.exe` release

## 🔮 Future

* [ ] User accounts
* [ ] Signup / login system
* [ ] Multi-user support
* [ ] Web deployment
* [ ] Personal libraries for multiple users

---

# 📄 License

This project is a personal project and currently does not have a specified open-source license.

---

# 🙏 Acknowledgments

Game data and images are provided by the **[RAWG Video Games Database API](https://rawg.io/apidocs)**.

MyGameList is an independent personal project and is not affiliated with RAWG.

---

## 🎮 MyGameList

A personal game library and tracking application built to make managing a personal game collection simple, organized, and enjoyable.
