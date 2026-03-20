# 📋 SmartClipboard-IA (WIP 🚧)

> ⚡ Un gestionnaire de presse-papiers intelligent permettant de stocker plusieurs éléments copiés sans perdre les précédents.

![status](https://img.shields.io/badge/status-en%20cours-orange)
![python](https://img.shields.io/badge/python-3.x-blue)
![platform](https://img.shields.io/badge/platform-Windows-lightgrey)
![license](https://img.shields.io/badge/license-MIT-green)

---

## 🚧 État du projet

> ⚠️ **Ce projet est en cours de développement (Work In Progress).**  
> De nombreuses fonctionnalités vont évoluer, être améliorées ou complètement modifiées.

---

## 🧠 Concept

SmartClipboard-IA améliore le fonctionnement du presse-papiers classique en permettant de :

- Stocker plusieurs éléments copiés
- Contrôler la manière dont ils sont collés
- Remplacer le comportement par défaut de Ctrl+C / Ctrl+V
- Contient un AgentIA pour corriger / reformuler vos phrases / mot enregistrer

---

|   Commande       |  Fonctionalité     | disponibilité      | Etat actuel             | Debug uniquement       |
|---               |:-:    |:-:    |:-:    |--:    |
| CTRL + C         | Stocker les éléments       | DISPONIBLE | FINI                    |  ❌     |
| CTRL + V         | Collage d'un éléments      | DISPONIBLE | Mise a jours futur      |  ❌     |
| CTRL + SHIFT + V | Coller tous les éléments   | DISPONIBLE | Mise a jours futur      |  ❌     |
| CTRL + SHIFT + C | vider L'historique         | DISPONIBLE | FINI                    |  ✔️     |

## ✨ Fonctionnalités actuelles

- 📌 Historique de copie multi-éléments
- 🔁 Système de collage intelligent :
  - Dernier élément copié
  - Premier élément copié
- ⌨️ Raccourcis globaux :
  - `Ctrl + C` → stocker les éléments
  - `Ctrl + V` → collage personnalisé
  - `Ctrl + Shift + V` → coller tous les éléments (IN PROGRESS)
  - `Ctrl + Shift + C` → vider l’historique (DEBUG)
- 🖥️ Interface via icône système (tray - IN PROGRESS)
- 🔄 Activation / désactivation du système (FUTUR)
- ⚙️ Choix du mode de collage (DISPONIBLE)

---

## 🏗️ Structure du projet

main.py
app/
├── tray.py
├── clipboardmanager.py

### 🔹 `main.py`

- Gère les raccourcis clavier globaux
- Lance le thread du tray
- Gère le cycle de vie de l’application :contentReference[oaicite:0]{index=0}

### 🔹 `clipboardmanager.py`

- Logique principale du presse-papiers
- Stockage des éléments copiés
- Gestion du collage
- Simulation du Ctrl+V :contentReference[oaicite:1]{index=1}

### 🔹 `tray.py`

- Interface système (tray)
- Activation / désactivation
- Sélection du mode de collage :contentReference[oaicite:2]{index=2}

---

## ⚙️ Fonctionnement

1. Vous copiez plusieurs éléments → ils sont stockés dans une liste
2. Le presse-papiers par défaut est intercepté
3. Lors du collage :
   - Le programme choisit quoi coller
   - Simule un Ctrl+V
   - Applique le comportement choisi

---

## 🔥 Pourquoi ce projet ?

Le presse-papiers classique est limité :

- ❌ Un seul élément stocké
- ❌ Pas d’historique
- ❌ Aucun contrôle
---

## ⚠️ Limitations actuelles

- Utilise `pyperclip` (texte uniquement)
- Gestion basée sur des délais (`sleep`)
- Pas de support des images/fichiers
- Interface limitée au tray

---

## 🚀 Améliorations prévues

### 🧠 Amélioration du moteur clipboard

- Passage de `pyperclip` → **pywin32**
- Meilleure performance
- Intégration native Windows
- Support :
  - Images 🖼️
  - Fichiers 📁
  - Formats avancés
 
- Intégration d'agent IA local ou disponible sur le cloud
  - Correction des fautes
  - Reformulation des phrases

- Interface web
  - Géré facilement le comportement de vos agent grace a une interface web
  - Géré facilement les paramètres de l'app avec une interface web moderne

---

### 🤖 Intégration d’un agent IA (feature majeure)

Un assistant IA sera intégré pour :

- 📖 Afficher la définition d’un texte sélectionné
- ✍️ Reformuler un texte sélectionné
- 🧠 Fournir des explications contextuelles
- ⚡ Améliorer la productivité

---

### ⚡ Performance

- Suppression des `time.sleep`
- Détection d’événements système
- Meilleure gestion clavier
- Précharger les models afin que la premier utilisation sois rapide

---

## 🛠️ Technologies utilisées

- Python
- pystray
- keyboard
- pyperclip _(temporaire)_
- Ollama
- MISTRAL

---

## 🎯 Vision

Transformer le presse-papiers en un **outil de productivité avancé** :

> D’un simple copier-coller → à un système intelligent et puissant

---

## 📌 Roadmap

- [x] Gestion multi-copie
- [x] Intégration tray
- [x] Système de collage
- [x] Intégration IA (En vrai pas encore, y'a 80% du code ajouté la)
- [ ] Migration vers pywin32
- [ ] Interface graphique ????
- [ ] Support multiplateforme

---

## ⭐ Support

Si le projet te plaît :

- ⭐ Star le repo
- 💡 Propose des idées

---

## ⚠️ Avertissement

Ce programme modifie le comportement des raccourcis clavier système.  
À utiliser avec précaution selon votre environnement.

---
