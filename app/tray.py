# Configuration du tray de l'application / génération icone
from pystray import Menu, MenuItem as item
import pystray
from PIL import Image, ImageDraw

# Utile pour le web / interface
import webbrowser
import threading
import uvicorn

# Utilisé pour fonctionner avec l'app
from . import clipboardmanager
# Import web.serveur sera fait localement pour éviter boucle circulaire
# Import main sera fait localement dans close_tray() pour éviter boucle circulaire

# Utile partout dans le code
import time


#Variables pour les options de collage

getLC = False  # Variable pour suivre l'état de "Coller le dernier element"
getFC = False  # Variable pour suivre l'état de "Coller le premier element"
getAC = False  # Variable pour suivre l'état de "Coller tout les elements"

# Variable pour suivre l'état du serveur :
serveur = None

# Variable pour suivre l'état du toggle :
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
    """Ferme l'application complètement"""
    from .. import main
    
    print("Fermeture du tray")
    global icon
    icon = None
    tray_icon.stop()  # Arrête le tray
    # Attendre que l'icône disparaisse avant de fermer complètement
    time.sleep(0.2)
    main.quit_app()  # Ferme l'app



############################
# --- --- ZONE WEB --- --- #
############################


def run_serveur():
    """Lancer l'interface web"""
    global server

    config = uvicorn.Config("app.web.serveur:app", host="127.0.0.1", port=6767, log_level="warning")
    serveur = uvicorn.Server(config)
    serveur.run()

def start_serveur():
    """Lancer l'interface web dans un thread séparé"""
    ui_thread = threading.Thread(target=run_serveur, daemon=True)
    ui_thread.start()
    webbrowser.open("http://127.0.0.1:6767/home")


def stop_server():
    global server
    if server:
        server.should_exit = True




###############################
## --- --- ZONE TRAY --- --- ##
###############################


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
            item("A propos", start_serveur)
            #item("Quit", close_tray)
            )
        
        )

    icon.run()

