# My Chatbot Platform! 🤖

Hi! This is my school assignment: A simple app where you sign up, make a chatbot project, and chat with it (fake AI for fun).

## What It Does
- Sign up and log in (safe passwords).
- Create a project with special instructions for the bot.
- Chat: Send a message and get a reply (uses your instructions).

## How to Run It (Easy Steps)
1. Download my code: Go to [GitHub link] and click green "Code" → "Download ZIP".
2. Unzip to a folder (e.g., Desktop/chatbot).
3. Open in VSCode: File → Open Folder → Pick the folder.
4. Open Terminal (bottom): Type `pip install flask flask-jwt-extended flask-cors python-dotenv` → Enter (installs stuff).
5. Type `python app.py` → Enter. See "Running on http://127.0.0.1:5000"? It's on!
6. Test: Use Thunder Client (VSCode extension—install if needed). 
   - POST /register: {"email": "kid@test.com", "password": "123"}
   - POST /login: Same → Get token.
   - POST /projects (add token header): {"name": "Fun Bot", "prompts": "Be silly!"}
   - POST /chat/1 (add token): {"message": "Hi!"} → Get reply.

## Try the Live Demo
Go to [Replit link from Step 4]—no install needed! Test the same way.

Made by [Your Name] for [Class/Teacher]. Fun project! 😄
