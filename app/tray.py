from pystray import Menu, MenuItem as item
import pystray
import time

from . import clipboardmanager
from PIL import Image, ImageDraw

import main
import webbrowser


#Variables pour les options de collage

getLC = False  # Variable pour suivre l'état de "Coller le dernier element"
getFC = False  # Variable pour suivre l'état de "Coller le premier element"
getAC = False  # Variable pour suivre l'état de "Coller tout les elements"


# Variable pour suivre l'état du toggle
#Le toggle signifie que le programme est actif ou non, si le toggle est désactivé, les raccourcis clavier seront remplacé par ceux de l'app.
is_running = False
icon = None  # Variable globale pour le tray  


def create_default_icon():
    """
    Créer une icône par défaut si le fichier n'existe pas
    """
    
    img = Image.new("RGB", (64, 64), color=(40, 120, 200))
    draw = ImageDraw.Draw(img)
    draw.text((18, 18), "EN", fill="white")
    return img


def last_clipboard():
    
    '''
    Fonction pour coller le dernier élément du presse-papiers
     - change le style de copie pour copier le dernier élément
    '''

    clipboardmanager.change_copy_style("copy_last")
    print("Change copy style : copy_last")
    global getLC, getFC, getAC
    if getLC == False:
        getLC = True
        getFC = False
        getAC = False

    # Récupérer le dernier élément du presse-papiers
    return "Dernier élément du presse-papiers"

def first_clipboard():
    
    '''
    Fonction pour coller le premier élément du presse-papiers
     - change le style de copie pour copier le premier élément
    '''

    clipboardmanager.change_copy_style("copy_first")
    print("Change copy style : copy_first")
    global getLC, getFC, getAC
    if getFC == False:
        getFC = True
        getLC = False
        getAC = False

    # Récupérer le premier élément du presse-papiers
    return "Premier élément du presse-papiers"

def get_label(item):
    return "Etat : Désactivé" if not is_running else "Etat : Activé"

def toggle(icon, item):
    global is_running
    is_running = not is_running

    if is_running:
        print("Toggle activé")
    else:
        print("Toggle désactivé")

    icon.update_menu()

def close_tray(tray_icon, item):
    print("Fermeture du tray")
    global icon
    icon = None
    tray_icon.stop()  # Arrête le tray
    # Attendre que l'icône disparaisse avant de fermer complètement
    time.sleep(0.2)
    main.quit_app()  # Ferme l'app

### fonction principale du tray
def run_tray():
    global icon
    print("Lancement du tray")
    image = create_default_icon()     
    
    icon = pystray.Icon(
        "ID Learn English",    # ID de l'app 
        image,                 # Icon de l'app
        "Multi ClipBoard",       # Nom vue par l'utilisateur
        
        menu=pystray.Menu(
            item(get_label, toggle),  
            item("Paramètres", 
                            pystray.Menu(
                                item("Coller le dernier element", last_clipboard, checked=lambda _: getLC),
                                item("Coller le premier element", first_clipboard, checked=lambda _: getFC),
                )
            ),
            #item("Documentation :", lambda),
            item("A propos", lambda:webbrowser.open("https://github.com/Nuxhi")),
            item("Quit", close_tray)
            )
        
        )

    icon.run()

