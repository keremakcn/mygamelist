# 🎮 MyGameList

**MyGameList** is a personal game library and tracking application.

Search for games, add them to your library, track what you're playing, rate games yourself, write notes, mark favorites, and keep track of when you finished a game.

Game information is provided by the **RAWG Video Games Database API**, while your personal library is stored locally on your computer.

---

## 📸 Features

* 🔍 Search for games
* 📚 Build your personal game library
* 🎮 Track your status:

  * Want to Play
  * Playing
  * Played
  * Dropped
* ⭐ Give games your own rating from 0–10
* 📝 Write personal notes
* ❤️ Mark favorite games
* 📅 Record played dates
* 🔀 Filter and sort your library
* 🌐 Turkish / English interface
* 🎨 Custom dark gaming-themed interface
* 🖥️ Windows desktop application
* 💾 Local SQLite database
* 🛡️ Error handling for API and connection problems

---

# 📥 Download

You can download the latest Windows version from the **[Releases](https://github.com/your-username/mygamelist/releases)** page.

Download:

```text
MyGameList-v1.0.0.zip
```

### Installation

1. Download the ZIP file.
2. Extract it anywhere you want.
3. Open the extracted `MyGameList` folder.
4. Run **`MyGameList.exe`**.

That's it. You don't need to install Python or any other dependencies.

---

# 🔑 First Launch

MyGameList uses the **RAWG API** to search for games and retrieve game information.

When you launch the application for the first time, MyGameList will ask you for a **RAWG API key**.

### Getting your API key

1. Open the **[RAWG API page](https://rawg.io/apidocs)**.
2. Create a free RAWG account or log in to your existing account.
3. Follow the RAWG instructions to obtain your API key.
4. Copy the API key.
5. Return to MyGameList and enter the key when the application asks for it.

After the key is saved, you can start using the application.

> 🔐 **Never share your API key publicly or upload it to GitHub.**

---

# 💾 Your Library

Your personal library is stored **locally on your computer**.

The application uses a SQLite database to store information such as:

* Your games
* Game status
* Personal ratings
* Notes
* Favorites
* Played dates

Your library is not dependent on an online MyGameList account.

### ⚠️ Keep the application folder together

The application may create additional files and folders while you use it.

For this reason, keep the complete `MyGameList` folder together and do not delete or move individual files.

If you want to back up your library, keep a copy of your application data, especially:

```text
games.db
```

---

# 🛠️ Built With

| Technology  | Purpose                    |
| ----------- | -------------------------- |
| Python      | Backend                    |
| Flask       | Web application framework  |
| SQLite      | Local database             |
| HTML / CSS  | Interface                  |
| Jinja2      | HTML templates             |
| PyWebView   | Desktop application window |
| PyInstaller | Windows executable         |
| RAWG API    | Game data                  |

---

# 🧑‍💻 Running from Source

If you want to explore or modify the source code:

### Requirements

* Python 3.10+
* Git
* RAWG API key

### Clone the repository

```bash
git clone https://github.com/your-username/mygamelist.git
cd mygamelist
```

### Install dependencies

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Configure the API

Create a `.env` file:

```env
RAWG_API_KEY=your_key_here
```

Then initialize the database:

```bash
python database.py
```

Run the application:

```bash
python app.py
```

The development version will be available at:

```text
http://127.0.0.1:5000
```

---

# 🗺️ Roadmap

### Completed

* [x] RAWG API integration
* [x] Game search
* [x] Personal library
* [x] Status tracking
* [x] Personal ratings
* [x] Notes
* [x] Favorites
* [x] Played dates
* [x] Filtering & sorting
* [x] Turkish / English support
* [x] Custom UI
* [x] Error handling
* [x] Windows desktop version

### Planned

* [ ] User accounts
* [ ] Multi-user support
* [ ] Online/web version

---

# 📄 License

This is a personal project and currently has no specified open-source license.

---

# 🙏 Acknowledgments

Game data is provided by the **[RAWG Video Games Database API](https://rawg.io/apidocs)**.

MyGameList is an independent personal project and is not affiliated with RAWG.

---

**MyGameList — Keep track of the games you play. 🎮**
