HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SUDO_CHAT_ID = int(environ["SUDO_CHAT_ID"]) # Chat where the bot will play the music.
    SUDOERS = list(int(x) for x in environ.get("SUDOERS", "").split()) # Users which have special control over the bot.
    SESSION_STRING = environ["SESSION_STRING"] # Check Readme for session

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 1488120
    API_HASH = "9684f2fe66b111264c36cc3fa1e8e765"
    SUDO_CHAT_ID = -1001336384919
    SUDOERS = [660086073, 1344497552]

# don't make changes below this line
ARQ_API = "https://thearq.tech"
