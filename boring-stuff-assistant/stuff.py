"""
Boring Stuff Script

"""
import pystray
import threading
import logging
from PIL import Image
from time import time, sleep

NAME = "Boring Stuff Assistant"
REFRESH_RATE = 3
ICON_SIZE = (64, 64)
ICON_COLOR = (255, 255, 0)

running = True
trayicon = None


def quit():
    """Quit application"""
    logging.info("Quitting.")
    trayicon.stop()
    global running
    running = False


def trayicon_init():
    """Initialize trayicon"""
    try:
        image = Image.open("res/icon.png")
    except:
        image = Image.new('RGB', ICON_SIZE, ICON_COLOR)
        logging.warning("Icon file not found.")

    menu = pystray.Menu(
        pystray.MenuItem("Exit", quit)
    )

    global trayicon
    trayicon = pystray.Icon(NAME, icon=image, menu=menu,
                            title=NAME)
    trayicon.run()


def notify(text, ok=True):
    if ok:
        logging.info(text)
        trayicon.notify(text, title=NAME)
    else:
        logging.critical(text)
        trayicon.notify(text, title=NAME + " Error")


def loop():
    """Desktop scanning loop"""
    sleep(2)  # Wait for trayicon initialization

    while running:
        notify("AAa...")
        sleep(REFRESH_RATE)


def main():
    try:
        logging.basicConfig(filename="boring-stuff.log", level=logging.INFO,
                            format="%(asctime)s %(levelname)s: %(message)s")
        logging.info(50 * "-")
        logging.info("Starting.")

        watcher = threading.Thread(target=loop)
        watcher.start()

        trayicon_init()

        watcher.join()
    except Exception as e:
        notify("Unexpected critical error occured.", False)
        logging.exception(e)


if __name__ == "__main__":
    main()
