import threading
import keyboard
import app.tray
import app.clipboardmanager
import os
import time   

def quit_app():
    print("Fermeture de l'application")
    keyboard.unhook_all()  # Arrête tous les hotkeys
    time.sleep(0.2)  # Laisser le temps à l'icône de disparaître
    os._exit(0)


def main():
    print("Lancement de l'application")
    tread_tray = threading.Thread(target=app.tray.run_tray, daemon=True)
    tread_tray.start()


    keyboard.add_hotkey('ctrl+v', app.clipboardmanager.past, suppress=True)
    keyboard.add_hotkey('ctrl+c', app.clipboardmanager.copy, suppress=False)
    keyboard.add_hotkey('ctrl+shift+v', app.clipboardmanager.all_copy, suppress=False)

    keyboard.add_hotkey('ctrl+shift+c', app.clipboardmanager.lst_cpt_clear, suppress=False)
    # Garder le programme actif
    keyboard.wait()


if __name__ == "__main__":
    main()
