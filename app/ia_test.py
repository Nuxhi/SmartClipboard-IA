
# Tableau de test avec toutes les phrases
from ia import cloud_generation, local_generation
import time


start_time = time.time()
phrases_test = [
    # évidentes
    "j'ai oublier de faire mes devoir",
    "il sont parti sans prévenir",
    "je c'est pas ou il est",
    "tu fait quoi demain",
    "on n'a manger tard hier",
    "sa ne marche pas comme prévu",
    "j'ai pris c'est document",
    "il a terminer sont travail",
    
    
    #  classiques
    "j'ai essayer de comprendre mais j'y arrive pas",
    "elle a décider de partir plus tôt",
    "ils ont commencer sans nous",
    "tu peux me dire ou est le problème",
    "il faut que je fasse attention a sa",
    "je me suis rendu compte que j'avais tord",
    "il a fallut attendre longtemps",
    "je les ai vue hier",
    
    #  d'accord
    "les enfants a jouer dans le jardin",
    "les fleurs que j'ai cueilli sont jolie",
    "elle est partie sans prévenir ses amis",
    "ils sont arriver en retard a la réunion",
    "les choses que j'ai dit était vrai",
    "il les a pris sans demander",
    
    #  subtiles
    "il faut que tu prenne ton temps",
    "je les ai laisser faire",
    "elle c'est rendu compte de son erreur",
    "les données que j'ai collecté sont fiable",
    "il a su répondre a toute les questions",
    "je n'ai rien vue de particulier",
    "ils ont du partir plus tôt",
    
    # Phrases naturelles (type utilisateur)
    "salut j'ai un probleme avec mon code sa marche pas",
    "est ce que tu peux m'aider a comprendre se bug",
    "j'ai essayer plusieurs solution mais rien ne fonctionne",
    "si ta une idée je suis preneur",
    "merci pour ton aide sa m'aiderais beaucoup",
    
    # Texte un peu plus long
    "bonjour j'ai un petit soucis avec mon programme il fonctionne pas comme prévu et je comprend pas pourquoi",
    "j'ai essayer de debug mais j'arrive pas a trouver d'ou viens le probleme",
    "j'ai verifier plusieurs fois le code mais il y a toujours une erreur qui apparait",

    # Cas piégeux
    "il ce sont parler longtemps",
    "elle c'est tromper de réponse",
    "je c'est qu'il va venir",
    "on c'est vu hier soir",
    "il a pris sa veste et c'est chaussures",
    
    
    #Réaliste
    "j'ai pas trop compris pourquoi sa fonctionne pas alors que hier sa marcher tres bien",
    "si quelqu'un a une idée de se qui cloche je suis preneur",
    "j'ai essayer plein de truc mais rien n'a marcher"]

# Boucle pour corriger chaque phrase
for i, phrase in enumerate(phrases_test, 1):
    print(f"\n{'='*60}")
    print(f"Phrase {i}/{len(phrases_test)}")
    print(f"{'='*60}")
    local_generation(phrase)
    print()
    with open("corrections.txt", "a", encoding="utf-8") as f:
        f.write(f"Phrase {i} : {phrase}\n")
        f.write(f"Correction : {local_generation(phrase)}\n")
        f.write(f"{'-'*60}\n")

end_time = time.time()
print(f"\nTime taken for all corrections: {end_time - start_time} seconds")