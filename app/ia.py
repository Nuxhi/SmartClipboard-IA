from dotenv import load_dotenv
import os

import ollama

#cloud
from ollama import Client

#local
from ollama import chat
from ollama import ChatResponse

import time
import ia_prompt

load_dotenv()

use_cloud = False
choose_model = ["mistral", "mistral:latest"] 
PROMPT = ia_prompt.system_prompt()

def init_ollama():
    models_lst = []

    print("PHASE 1/3")
    try:
        models = ollama.list()
        for m in models.models:
            models_lst.append(m.model)
    except Exception as e:
        print("erreur lors de la vérification des models")
    
    print("PHASE 2/3")
    if not any(model in models_lst for model in choose_model): #EXPRESSION génératrice, je découvre ça ce soir, j'avais une erreur car je voulais check une liste...
        try:
            print("tentative d'installation du model : ", choose_model)
            ollama.pull(choose_model)
        except ollama.ResponseError as e:
            print("Erreur lors de l'installation : \nmodèle inexistant\nerreur serveur\nrequête invalide : \n erreur : ",e)
        except ollama.RequestError as e:
            print("Erreur lors de l'installation : \nOllama pas lancé ?\nProbleme de réseau\n api innacessible \n erreur : ",e)
        except Exception as e:
            print("Erreur lors de l'installation du model \n erreur : ",e)
        
        print("le model viens d'etre etre installé")
    else:
        print("model déjà installé")
    
    print("PHASE 3/3")



def cloud_generation(phrase):
    '''
    Correction orthographique et grammaticale par IA (gpt-oss:120b).
    Permet de corriger l’orthographe d’un mot ou d’une phrase rédigée par l’utilisateur.
    Cette méthode requiert une clé API Ollama.
    Elle est utilisée si use_cloud est défini sur True.
    '''
    start_time = time.time()
    client = Client(
        host='https://ollama.com',
        headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY')}
    )

    messages=[
        {
            'role': 'system',
            'content':f'{PROMPT}'
        },
        {
            'role': 'user',
            'content': f'Tu peux corriger les fautes d\'orthographe et de grammaire dans cette phrase ou le mot suivant : {phrase}'
        }
    ]

    for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
        print(part.message.content, end='', flush=True)
    
    end_time = time.time()
    print(f"\nTime taken: {end_time - start_time} seconds")



def local_generation(phrase):
    '''
    Methode d'utilisation de l'ia choisis par l'utilsiateur (mistral par défaut)
    afin qu'elle corrige l'ortropgrahe du mot ou de la phrase rédigé par l'utilisateur.
    cette methode fonctionne grace a la puissance GPU du pc de l'utilisateur (généralement plus rapide que le cloud mais demande des perfs)
    elle est utilisé si use_cloud est sur False
    '''
    print(choose_model[0])
    start_time = time.time()
    response: ChatResponse = chat(
        model=choose_model[0],
        messages=[
            {
                'role': 'system',
                'content':f'{PROMPT}'
            },
            {
                'role': 'user',
                'content': phrase
            }
        ]
    )

    print(response['message']['content'])
    end_time = time.time()
    print(f"\nTime taken: {end_time - start_time} seconds")


init_ollama()
#cloud_generation("Je suis aller au marché hier et j'ai acheter des pommes.")
local_generation("Je suis aller au marché hier et j'ai acheter des pommes.")