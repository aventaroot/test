import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Botunuzu çalıştıran ana dosyanızın adını buraya yazın
MAIN_SCRIPT_PATH = "bot.py"

class RestartHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print("Detected changes. Restarting bot...")
            restart_bot()

def restart_bot():
    global bot_process
    try:
        bot_process.terminate()
    except:
        pass

    bot_process = subprocess.Popen(["python", MAIN_SCRIPT_PATH])

if __name__ == "__main__":
    event_handler = RestartHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    bot_process = subprocess.Popen(["python", MAIN_SCRIPT_PATH])

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
