# SchoolBot Chatbot

An AI-powered school FAQ chatbot built using Python, Flask, and ChatterBot.

## Setup Instructions

1. **Download/clone this project folder** to your computer.

2. **Open the folder in VS Code** (or your preferred editor).

3. **Open the terminal** in this folder.

4. (Optional but recommended) **Create a virtual environment:** type in: python -m venv venv

5. **Activate the virtual environment:**

- On Windows:
  ```
  venv\Scripts\activate
  ```
- On Mac/Linux:
  ```
  source venv/bin/activate
  ```

6. **Install all required libraries:**
pip install -r requirements.txt

7. **Download the English language model for spaCy** (first time only):
python -m spacy download en_core_web_sm


8. **Run the chatbot app:**
python app.py


9. **Open your browser and visit:**
http://localhost:5000


10. **Chat with your SchoolBot and lmk if there are any mistakes!**

---

## Files in This Project

- `app.py` – The main Flask app 
- `requirements.txt` – All necessary Python packages
- `README.md` – These instructions

---

## Troubleshooting

- If you get an error about spaCy or `en_core_web_sm` missing, run:
python -m spacy download en_core_web_sm

- If you see port or permission errors, make sure you have admin rights or try changing the port in `app.py`.

- If you have questions, text me privately or ask maam on the group.

---

