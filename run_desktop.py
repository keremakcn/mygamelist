import threading
import webview
from app import app


def start_flask():
    """Flask sunucusunu arka planda, tarayıcı açmadan çalıştırır."""
    app.run(port=5000, debug=False, use_reloader=False)


if __name__ == "__main__":
    threading.Thread(target=start_flask, daemon=True).start()

    webview.create_window(
        "MyGameList",
        "http://127.0.0.1:5000",
        width=1100,
        height=750,
        min_size=(700, 500)
    )
    webview.start()