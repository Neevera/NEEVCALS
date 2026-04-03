# 🌐 Multi-Tool Web Hub & Smart AI Chatbot

Welcome to the **Multi-Tool Web Hub**! [cite_start]This project is a versatile web application built with the **Flask** framework[cite: 46]. It serves as a "digital Swiss Army Knife," featuring various utility tools—from financial calculators to unit converters—alongside an intelligent AI assistant.

---

## ✨ Features

* [cite_start]🤖 **Smart AI Chatbot (`chatbot.py`):** An interactive AI assistant powered by the `Llama-3.3-70b-versatile` model via the Groq API[cite: 46]. It is designed to provide clear, concise, and helpful responses to user inquiries.
* ⚖️ **BMI / Body Index Calculator (`bodyindex.py`):** Calculates the body mass index based on height and weight inputs, providing specific feedback on whether the user is within the ideal weight range.
* 🔢 **Number System Converter (`konv.py`):** A practical tool for converting numbers between Decimal, Binary, Octal, and Hexadecimal systems.
* 💰 **Income Tax Calculator (PPh 21) (`pph21.py`):** Calculates Indonesian income tax (PPh 21) based on monthly salary and tax-exempt income (PTKP) status, offering a detailed breakdown of tax layers.
* 🎂 **Age Calculator (`usia.py`):** Dynamically calculates your exact age based on your birth date relative to the current day.

---

## 📂 Project Architecture

This project uses a modular **Blueprint** architecture to keep the code organized and scalable:

* `index.py` ➔ **The Main Entry Point.** Initializes the Flask app and registers all functional Blueprints.
* **Blueprints (Core Logic):**
    * `chatbot.py`: Handles AI system instructions, session-based chat history, and API integration.
    * `bodyindex.py`: Contains the logic for height-weight ratio analysis.
    * `konv.py`: Manages mathematical conversions for different number bases.
    * `pph21.py`: Implements tax regulations and tiered tax rates.
    * `usia.py`: Uses the `datetime` module to calculate age accurately.
* [cite_start]`requirements.txt`: Lists all necessary Python packages such as Flask and Groq[cite: 46].

---

## 🚀 Installation & Setup

Follow these steps to run this hub on your local machine:

### 1. Install Dependencies
Open your terminal in the project directory and run:
```bash
pip install -r requirements.txt
