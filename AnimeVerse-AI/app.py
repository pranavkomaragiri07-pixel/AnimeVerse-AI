import streamlit as st
import requests
import random

# =========================
# IMPORT REAL BACKEND
# =========================
from battle import (
    battle_1v1,
    battle_2v2,
    battle_4v4,
    run_tournament,
    survival_mode
)

# =========================
# PAGE CONFIG (MUST BE FIRST)
# =========================
st.set_page_config(
    page_title="AnimeVerse AI",
    page_icon="⚔️",
    layout="wide"
)

# =========================
# CSS LOADER (KEEP HERE)
# =========================
try:
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

# =========================
# QUOTE GENERATOR
# =========================
def generate_quote(theme):
    quotes = {
        "Motivational": [
            ("Naruto Uzumaki", "I'm not gonna run away..."),
            ("Rock Lee", "Hard work beats talent."),
            ("All Might", "Because I am here!")
        ],
        "Friendship": [
            ("Luffy", "I will become Pirate King."),
            ("Naruto Uzumaki", "I won't let my friends die."),
        ],
        "Success": [
            ("Itachi Uchiha", "Reality is harsh."),
            ("Light Yagami", "I am justice."),
        ],
        "Sad": [
            ("Pain", "Feel pain."),
            ("Itachi", "Forgive me."),
        ],
        "Funny": [
            ("Saitama", "Ok."),
            ("Goku", "I’m hungry."),
        ]
    }
    return random.choice(quotes.get(theme, [("Anime", "Stay strong")]))


# =========================
# PERSONA FIXED (IMPORTANT)
# =========================
def get_character_match(q1, q2, q3, q4, q5, q6):

    score = {
        "Naruto Uzumaki": 0,
        "Monkey D. Luffy": 0,
        "Itachi Uchiha": 0,
        "Levi Ackerman": 0,
        "Gojo Satoru": 0,
        "Goku": 0,
        "Eren Yeager": 0,
        "Saitama": 0
    }

    answers = [q1, q2, q3, q4, q5, q6]

    for a in answers:

        if a in ["Friendship", "Support", "Loyalty"]:
            score["Naruto Uzumaki"] += 2
            score["Monkey D. Luffy"] += 2
            score["Itachi Uchiha"] += 2
            score["Saitama"] += 1

        if a in ["Freedom"]:
            score["Monkey D. Luffy"] += 3
            score["Eren Yeager"] += 2

        if a in ["Power", "Physical strength"]:
            score["Goku"] += 3
            score["Saitama"] += 2
            score["Gojo Satoru"] += 2
            score["Naruto Uzumaki"] += 1
            score["Itachi Uchiha"] += 1   # FIXED

        if a in ["Strategic", "Intelligence", "Tactical mind"]:
            score["Itachi Uchiha"] += 3
            score["Levi Ackerman"] += 3

        if a in ["Courage"]:
            score["Naruto Uzumaki"] += 2
            score["Monkey D. Luffy"] += 3
            score["Goku"] += 2

        if a in ["Anger", "Overconfidence"]:
            score["Eren Yeager"] += 3

        if a in ["Calmness"]:
            score["Itachi Uchiha"] += 2
            score["Gojo Satoru"] += 2

        if a in ["Speed"]:
            score["Goku"] += 2
            score["Naruto Uzumaki"] += 1
            score["Monkey D. Luffy"] += 1

        if a in ["Leader"]:
            score["Naruto Uzumaki"] += 2
            score["Eren Yeager"] += 2
            score["Monkey D. Luffy"] += 2

        if a in ["Adapt"]:
            score["Levi Ackerman"] += 2
            score["Goku"] += 2
            score["Itachi Uchiha"] += 3   # FIXED KEY
            score["Saitama"] += 1

    return max(score, key=score.get)


# =========================
# HEADER
# =========================
st.title("🏆 AnimeVerse AI")
st.subheader("AI-Powered Anime Companion")

# =========================
# TABS
# =========================
tab1, tab3, tab4, tab5 = st.tabs([
    "🔍 Anime Search",
    "⚔️ Battle Simulator",
    "✨ Quote Generator",
    "🎭 Personality Quiz"
])

# =========================
# ANIME SEARCH
# =========================
with tab1:
    st.header("🔍 Anime Search")

    anime_name = st.text_input("Enter Anime Name")

    if st.button("Search Anime"):
        if anime_name:
            url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                if data["data"]:
                    anime = data["data"][0]

                    st.success(f"Results for {anime['title']}")
                    st.image(anime["images"]["jpg"]["image_url"], width=300)

                    st.write(f"⭐ Rating: {anime['score']}")
                    st.write(f"🎬 Episodes: {anime['episodes']}")

                    genres = ", ".join(g["name"] for g in anime["genres"])
                    st.write(f"🎭 Genres: {genres}")

                    if anime["year"]:
                        st.write(f"📅 Release Year: {anime['year']}")

                    st.write(f"📖 Synopsis: {anime['synopsis']}")

# =========================
# BATTLE (UNCHANGED)
# =========================
with tab3:
    st.header("⚔️ Battle Simulator")

    mode = st.selectbox(
        "Select Mode",
        ["1v1 Battle", "2v2 Battle", "4v4 Battle", "Tournament Arc", "Survival Arena"]
    )

    if mode == "1v1 Battle":
        a = st.text_input("Character A")
        b = st.text_input("Character B")

        if st.button("Start Battle"):
            result = battle_1v1(a, b)
            st.success(result["winner"])

# =========================
# QUOTES
# =========================
with tab4:
    st.header("✨ Quote Generator")

    theme = st.selectbox("Theme", ["Motivational","Friendship","Success","Sad","Funny"])

    if st.button("Generate Quote"):
        st.success(generate_quote(theme))

# =========================
# QUIZ FIXED
# =========================
with tab5:
    st.header("🎭 Personality Quiz")

    q1 = st.radio("Motivation", ["Power","Friendship","Freedom","Knowledge"])
    q2 = st.radio("Fight Style", ["Head on","Strategic","Support friends","Adapt"])
    q3 = st.radio("Trait", ["Courage","Intelligence","Loyalty","Calmness"])
    q4 = st.radio("Role", ["Leader","Support","Lone wolf","Strategist"])
    q5 = st.radio("Weakness", ["Anger","Trust issues","Overconfidence","Fear"])
    q6 = st.radio("Power Type", ["Physical strength","Speed","Magic/Skills","Tactical mind"])

    if st.button("Reveal Result"):
        character = get_character_match(q1,q2,q3,q4,q5,q6)
        st.success(character)
