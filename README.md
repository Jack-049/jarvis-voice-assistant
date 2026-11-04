# jarvis-voice-assistant
# 🤖 JARVIS - Voice & Text Virtual Assistant for Windows

**JARVIS** is a modular Python-based virtual assistant designed to automate daily tasks on Windows through voice or text commands.

The project was built to deliver a smooth and responsive voice-control interface capable of handling system utilities, fetching information, and integrating with external APIs.

---

## Key Features

### Voice & Hybrid Control (Wake Word)
- **Wake Word Integration:** Operates in passive listening mode, activating only when the keyword *"JARVIS"* is spoken.
- **Hybrid Input:** Supports both voice input (via microphone) and direct text input from the keyboard.
- **Voice Feedback (TTS):** Delivers immediate audio responses using Windows' native speech synthesis engine.

### Information & Web Services
- **Real-Time Weather:** Integrated with the **OpenWeatherMap API** to fetch temperature and weather conditions for any city.
- **Encylopedic Search:** Integrated with the **Wikipedia API** to summarize facts about people, places, or concepts.

### Hardware & System Control
- **Audio Control:** Adjusts system volume and toggles mute in real time.
- **Hardware Monitoring:** Checks battery percentage/charging status and CPU usage.
- **Utilities:** Takes instant full-screen screenshots saved directly to the Desktop.

### Application & Directory Automation
- **App Launcher:** Quickly launches Windows built-in software (Calculator, Notepad, Paint, File Explorer).
- **Microsoft Office Suite:** Opens Word, Excel, and PowerPoint via custom shortcuts.
- **Web & Directory Navigation:** Launches major websites (Google, YouTube, Amazon) and navigates local folders (Downloads, Documents, Desktop, and custom paths).

---

## 🛠️ Technologies Used

- **Language:** Python 3.12+
- **Speech Recognition:** `SpeechRecognition` (Google Speech API)
- **Text-to-Speech:** `pyttsx3` (Offline TTS via SAPI5 on Windows)
- **Automation & Hardware:** `pyautogui`, `psutil`
- **Web APIs:** `requests` (OpenWeatherMap API), `wikipedia-api`
- **Environment:** Virtualenv (`venv`), Windows Batch Scripts (`.bat`)

---

## 🚀 Installation & Setup

### 1. Prerequisites
Ensure you have Python installed and a free API key from [OpenWeatherMap](https://openweathermap.org/).

### 2. Clone the Repository
```bash
git clone [https://github.com/your-username/JARVIS.git](https://github.com/your-username/JARVIS.git)
cd JARVIS
