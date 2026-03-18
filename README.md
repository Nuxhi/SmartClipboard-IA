# SmartClipboard-IA
This project allows you to copy multiple items without overwriting the previous one. It improves productivity and removes the limitation of a single clipboard.

# 📋 SmartClipboard (WIP 🚧)

> ⚡ A smarter clipboard manager that lets you store multiple copied items without losing previous ones.

![status](https://img.shields.io/badge/status-in--progress-orange)
![python](https://img.shields.io/badge/python-3.x-blue)
![platform](https://img.shields.io/badge/platform-Windows-lightgrey)
![license](https://img.shields.io/badge/license-MIT-green)

---

## 🚧 Project Status

> ⚠️ **This project is still in development (Work In Progress).**  
> Many features will change, evolve, or be completely redesigned.

---

## 🧠 Concept

ClipboardSense enhances the default clipboard behavior by allowing you to:

- 📋 Store multiple copied elements
- 🔁 Control how they are pasted
- ⚡ Override default Ctrl+C / Ctrl+V behavior

👉 No more losing your previous copies.

---

## ✨ Current Features

- 📌 Multi-item clipboard history
- 🔁 Smart paste system:
  - Last copied element
  - First copied element
- ⌨️ Global shortcuts:
  - `Ctrl + C` → store items
  - `Ctrl + V` → custom paste
  - `Ctrl + Shift + V` → paste all
  - `Ctrl + Shift + C` → clear history
- 🖥️ System tray interface
- 🔄 Toggle ON/OFF system
- ⚙️ Clipboard mode selection

---

## 🏗️ Project Structure

main.py
app/
├── tray.py
├── clipboardmanager.py

### 🔹 `main.py`
- Handles global shortcuts
- Launches system tray thread  
- Manages app lifecycle :contentReference[oaicite:0]{index=0}

### 🔹 `clipboardmanager.py`
- Core clipboard logic
- Stores copied elements
- Handles paste behavior
- Simulates Ctrl+V when needed :contentReference[oaicite:1]{index=1}

### 🔹 `tray.py`
- System tray UI
- Toggle system ON/OFF
- Clipboard mode selection :contentReference[oaicite:2]{index=2}

---

## ⚙️ How It Works

1. You copy multiple elements → stored in a list
2. Default clipboard is overridden
3. When you paste:
   - The app decides what to paste
   - Simulates Ctrl+V
   - Maintains custom behavior

---

## 🔥 Why This Project?

The default clipboard is limited:
- ❌ Only one item stored
- ❌ No history
- ❌ No control

ClipboardSense solves this by:
- ✔ Keeping history
- ✔ Giving control
- ✔ Increasing productivity

---

## ⚠️ Current Limitations

- Uses `pyperclip` (text only)
- Some timing issues (`sleep` based)
- Limited clipboard format support
- No GUI (tray only)

---

## 🚀 Upcoming Improvements

### 🧠 Clipboard Engine Upgrade
- Replace `pyperclip` → **pywin32**
- Better performance
- Native Windows integration
- Support for:
  - Images 🖼️
  - Files 📁
  - Advanced formats

---

### 🤖 AI Integration (Major Feature)

A built-in AI assistant will allow:

- 📖 Get definition of selected text
- ✍️ Reformulate selected content
- 🧠 Context-aware explanations
- ⚡ Instant productivity boost

---

### 🖥️ UI Improvements
- Full graphical interface
- Clipboard history viewer
- Search & filter
- Favorites / pinned items

---

### ⚡ Performance
- Remove `time.sleep`
- Event-based clipboard detection
- Better keyboard handling

---

## 🛠️ Technologies

- Python
- pystray
- keyboard
- pyperclip (temporary)

---

## 🎯 Vision

Transform the clipboard into a **powerful productivity tool**:

> From a simple copy-paste → to an intelligent workflow system

---

## 📌 Roadmap

- [x] Basic clipboard manager
- [x] Tray integration
- [x] Multi-copy system
- [ ] AI integration
- [ ] pywin32 migration
- [ ] GUI interface ?????

---

## 🤝 Contribution

This project is evolving fast 🚀  
Feel free to:
- Open issues
- Suggest features
- Improve code

---

## 👤 Author

Developed by [Nuxhi](https://github.com/Nuxhi)

---

## ⭐ Support

If you like this project:
- ⭐ Star the repo

---

## ⚠️ Disclaimer

This project modifies default keyboard behavior.  
Use with caution depending on your system environment.

---
