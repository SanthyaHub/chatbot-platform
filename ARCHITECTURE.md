# How My App Works (Simple Design) 🛠️

## Big Picture
My app is like a secure clubhouse for chatbots. It has 4 main parts:
1. **Sign Up/Log In**: Checks email/password (hides real password with math trick).
2. **Make Project**: Saves your bot's "rules" (like "Be funny") in a list.
3. **Chat**: Looks up rules → Makes a fake reply (e.g., "Hi from funny bot!").
4. **Storage**: Uses a tiny file (SQLite) to remember users/projects.

## Step-by-Step Flow (Like a Map)
- You send message (e.g., "Sign up") → App checks → Saves in file.
- For chat: You say "Hi" → App grabs rules → Replies "Hi back!".
- Safe: Only logged-in kids can make/chat (uses secret code/token).

## Drawing (Text Version)

## Tools I Used
- Python + Flask: Makes the app run.
- JWT: Secret tickets for log-in.
- Mock AI: Fake replies (no real robot needed—saves money!).

It's simple but strong—like a Lego tower that doesn't fall. Easy to add real AI later!
