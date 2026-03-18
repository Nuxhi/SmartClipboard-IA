import keyboard
import pyperclip
import time
import warnings

# Activer les DeprecationWarning
warnings.simplefilter("always", DeprecationWarning)

lst_cpt = []
lst_item_cpt = ""
cs = -1

bad_caractere_pattern = [" '\r\n' "]

'''
CopyStyle (Cs) information : 
-1 réplique le comportement noraml de windows, on collera donc les informations de la plus récente a la plus ancienne
0 colle les informations de la plus ancienne a la plus récente
'''

def change_copy_style(setting):
    global copy_Last, copy_all, cs
    if setting == "copy_last":
        cs = -1
    elif setting == "copy_first":
        cs = 0

def action_data(action, text=None):
    global lst_item_cpt
    '''
    Methode d'affichage des données d'action pour le debug
    action : 1 pour copy, 0 pour past
    '''
    warnings.warn("Cette fonction est dépréciée", DeprecationWarning, stacklevel=2)
    try:
        if action == 1:
            action = "Copier : "
        elif action == 0:
            action = "coller : "
        else:
            raise ValueError("Action invalide: doit être 0 ou 1")
    except ValueError as e:
        print(f"Erreur: {e}")
        return
    
    if not text:
        text = "aucun texte saisie"

    print(action, text)
    print("last item :", lst_item_cpt)
    print(f"lst_cpt {lst_cpt} len : {len(lst_cpt)}")


def copy():
    '''
    Enregistre le texte selectionner dans un tableau
    cela permet de stocker plusieusr éléments dans le presse-papiers
    '''
    global lst_item_cpt
    time.sleep(0.1)
    #Action avec le clipboard
    if pyperclip.paste() == bad_caractere_pattern:
        pass
    else:
        text = lst_item_cpt = pyperclip.paste() #pour affecté 2 varialbes en meme temps
        lst_cpt.append(text)

    #Affichage debug
    action_data(1, text)
    

def past():
    '''
    permet de coller un element du tableau afin de l'imposé la ou l'utilisateur le souhaite
    Cette fonction est appellé lors de l'appuie sur ctrl+v
    elle simule également un appluie ctrl+v car celui-ci a était bloquer dans le main.py afin déviter les conflits avec le clipboard originel de windows
    '''

    try:
        if len(lst_cpt) > 0:
            text = lst_cpt[cs]
            lst_cpt.pop(cs)
        elif len(lst_cpt) == 0:
            print("condition ex")
            text = lst_item_cpt
        else:
            print(f"Liste vide")
            action_data(0)
            return
    except IndexError:
        print(f"Liste vide")
        action_data(0)
        return
    
    action_data(0, text)
    pyperclip.copy(text)

    # Simuler le collage
    keyboard.send("ctrl+v")


def all_copy():
    '''
    Permet de vider le tableau complet d'un coup
    a la suite d'un ctrl+v+v
    '''
    time.sleep(0.1)
    for i in range(len(lst_cpt)):
        past()

def lst_cpt_clear():
    return lst_cpt.clear()
