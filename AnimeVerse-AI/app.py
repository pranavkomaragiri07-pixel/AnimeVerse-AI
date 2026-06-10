import streamlit as st
import requests
import random
import streamlit.components.v1 as components

# =========================
# IMPORT BACKEND
# =========================
from battle import (
    battle_1v1,
    battle_2v2,
    battle_4v4,
    run_tournament,
    survival_mode
)

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AnimeVerse AI",
    page_icon="⚔️",
    layout="wide"
)

# =========================
# CSS
# =========================
try:
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass


# =========================
# 🎆 FIREWORKS FUNCTION
# =========================
def show_fireworks():
    components.html("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
        function fire() {
            for (let i = 0; i < 5; i++) {
                setTimeout(() => {
                    confetti({
                        particleCount: 150,
                        spread: 100,
                        origin: { y: 0.6 }
                    });
                }, i * 400);
            }
        }
        fire();
    </script>
    """, height=300)


# =========================
# 🏆 WINNER GLOW
# =========================
def show_winner_glow(winner):
    components.html(f"""
    <style>
        .winner {{
            text-align:center;
            font-size:60px;
            font-weight:900;
            color:white;
            animation: glow 1s infinite alternate;
        }}

        .name {{
            text-align:center;
            font-size:30px;
            color:#ff4b4b;
            font-weight:bold;
        }}

        @keyframes glow {{
            0% {{
                text-shadow: 0 0 10px #ff0000, 0 0 20px #ff4b4b;
            }}
            100% {{
                text-shadow: 0 0 30px #ff0000, 0 0 60px #ff6b6b;
            }}
        }}
    </style>

    <div class="winner">🏆 WINNER!!</div>
    <div class="name">{winner}</div>
    """, height=220)


# =========================
# 🏆 CHAMPION GLOW (TOURNAMENT)
# =========================
def show_champion_glow(champion):
    components.html(f"""
    <style>
        .champion {{
            text-align:center;
            font-size:70px;
            font-weight:900;
            color:#fff;
            animation: glow 1s infinite alternate;
        }}

        .name {{
            text-align:center;
            font-size:30px;
            color:#ffd700;
            font-weight:bold;
        }}

        @keyframes glow {{
            0% {{
                text-shadow: 0 0 10px #ffd700, 0 0 20px #ff4b4b;
            }}
            100% {{
                text-shadow: 0 0 40px #ffd700, 0 0 80px #ff6b6b;
            }}
        }}
    </style>

    <div class="champion">🏆 CHAMPION !!</div>
    <div class="name">{champion}</div>
    """, height=260)


# =========================
# QUOTES
# =========================
def generate_quote(theme):
    quotes = {
        "Motivational": [("Naruto Uzumaki", "Believe it!")],
        "Friendship": [("Luffy", "I will become Pirate King.")],
        "Success": [("Itachi", "Knowledge is power.")],
        "Sad": [("Pain", "Know pain.")],
        "Funny": [("Saitama", "Ok.")]
    }
    return random.choice(quotes.get(theme, [("Anime", "Stay strong")]))


# =========================
# PERSONA MATCH
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

    for a in [q1, q2, q3, q4, q5, q6]:

        if a in ["Friendship", "Support", "Loyalty"]:
            score["Naruto Uzumaki"] += 2
            score["Monkey D. Luffy"] += 2

        if a in ["Freedom"]:
            score["Monkey D. Luffy"] += 3
            score["Eren Yeager"] += 2

        if a in ["Power", "Physical strength"]:
            score["Goku"] += 3
            score["Saitama"] += 2

        if a in ["Strategic", "Intelligence"]:
            score["Itachi Uchiha"] += 3
            score["Levi Ackerman"] += 3

        if a in ["Courage"]:
            score["Naruto Uzumaki"] += 3

        if a in ["Speed"]:
            score["Goku"] += 2

        if a in ["Leader"]:
            score["Naruto Uzumaki"] += 2
            score["Eren Yeager"] += 2

    return max(score, key=score.get)


# =========================
# UI
# =========================
st.title("🏆 AnimeVerse AI")
st.subheader("AI-Powered Anime Companion")

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
        url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"
        r = requests.get(url).json()

        if r["data"]:
            anime = r["data"][0]
            st.success(anime["title"])
            st.image(anime["images"]["jpg"]["image_url"])


# =========================
# ⚔️ BATTLE MODE (1v1)
# =========================
with tab3:
    st.header("⚔️ Battle Simulator")

    mode = st.selectbox("Mode", ["1v1 Battle", "Tournament Arc"])

    if mode == "1v1 Battle":

        a = st.text_input("Character A")
        b = st.text_input("Character B")

        if st.button("Start Battle"):
            result = battle_1v1(a, b)

            st.success(f"Winner: {result['winner']}")

            show_fireworks()
            show_winner_glow(result["winner"])


    # =========================
    # 🏆 TOURNAMENT MODE (UPDATED)
    # =========================
    elif mode == "Tournament Arc":

        fighters = st.text_area("Enter fighters (one per line)")

        if st.button("Start Tournament"):

            result = run_tournament(fighters.split("\n"))

            st.success(f"Champion: {result['champion']}")

            # 🎆 FIREWORKS
            show_fireworks()

            # 🏆 CHAMPION GLOW
            show_champion_glow(result["champion"])


# =========================
# QUOTE
# =========================
with tab4:
    theme = st.selectbox("Theme", ["Motivational","Friendship","Success","Sad","Funny"])

    if st.button("Generate"):
        st.success(generate_quote(theme))


# =========================
# QUIZ
# =========================
with tab5:
    q1 = st.radio("Motivation", ["Power","Friendship","Freedom","Knowledge"])
    q2 = st.radio("Fight Style", ["Head on","Strategic","Support friends","Adapt"])
    q3 = st.radio("Trait", ["Courage","Intelligence","Loyalty","Calmness"])
    q4 = st.radio("Role", ["Leader","Support","Lone wolf","Strategist"])
    q5 = st.radio("Weakness", ["Anger","Trust issues","Overconfidence","Fear"])
    q6 = st.radio("Power Type", ["Physical strength","Speed","Magic","Tactical"])

    if st.button("Result"):
        st.success(get_character_match(q1,q2,q3,q4,q5,q6))
