import streamlit as st
import requests
import random

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
# QUOTES
# =========================
def generate_quote(theme):
    quotes = {
        "Motivational": [
            ("Naruto Uzumaki", "Believe it! Never give up."),
            ("All Might", "I am here!"),
        ],
        "Friendship": [
            ("Luffy", "I will never abandon my friends!"),
            ("Naruto", "Friends are my power!"),
        ],
        "Success": [
            ("Itachi Uchiha", "Growth comes through sacrifice."),
            ("Levi Ackerman", "Move forward."),
        ],
        "Sad": [
            ("Pain", "Pain leads to understanding."),
            ("Itachi", "Even heroes suffer."),
        ],
        "Funny": [
            ("Saitama", "Ok."),
            ("Goku", "I’m hungry again."),
        ]
    }

    char, quote = random.choice(quotes.get(theme, [("Anime", "Stay strong!")]))
    return f"{quote}\n\n— {char}"


# =========================
# CHARACTER MATCH
# =========================
def get_character_match(q1, q2, q3, q4, q5, q6):

    score = {
        "Naruto Uzumaki": 0,
        "Monkey D. Luffy": 0,
        "Gojo Satoru": 0,
        "Itachi Uchiha": 0,
        "Levi Ackerman": 0,
        "Goku": 0,
        "Eren Yeager": 0,
        "Saitama": 0
    }

    answers = [q1, q2, q3, q4, q5, q6]

    for a in answers:
        if a in ["Friendship", "Support", "Loyalty"]:
            score["Naruto Uzumaki"] += 2
            score["Monkey D. Luffy"] += 2

        if a == "Freedom":
            score["Monkey D. Luffy"] += 3

        if a in ["Power", "Physical strength"]:
            score["Goku"] += 3

        if a in ["Strategic", "Intelligence"]:
            score["Itachi Uchiha"] += 3

        if a == "Courage":
            score["Naruto Uzumaki"] += 2
            score["Monkey D. Luffy"] += 3

    return max(score, key=score.get)


# =========================
# HEADER
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
# 🔍 ANIME SEARCH (FINAL FIX)
# =========================
with tab1:

    st.header("🔍 Anime Search")

    anime_name = st.text_input("Enter Anime Name")

    if st.button("Search Anime"):

        if anime_name:

            try:
                url = "https://api.jikan.moe/v4/anime"
                params = {
                    "q": anime_name,
                    "limit": 25,
                    "sfw": True
                }

                headers = {"User-Agent": "Mozilla/5.0"}

                res = requests.get(url, params=params, headers=headers, timeout=10).json()

                data = res.get("data", [])

                anime = None
                query = anime_name.lower().strip()

                # 🔥 STRONG MATCH LOGIC
                for item in data:
                    title = item.get("title", "").lower()

                    if (
                        query == title
                        or query in title
                        or title in query
                        or any(word in title for word in query.split())
                    ):
                        anime = item
                        break

                # fallback
                if not anime and data:
                    anime = data[0]

                if anime:
                    st.success(anime.get("title", "Unknown"))

                    st.image(anime["images"]["jpg"]["image_url"])

                    st.write("⭐ Rating:", anime.get("score", "N/A"))
                    st.write("🎬 Episodes:", anime.get("episodes", "N/A"))
                    st.write("📌 Status:", anime.get("status", "N/A"))
                    st.write("📖 Synopsis:", anime.get("synopsis", "N/A"))

                else:
                    st.error("No anime found.")

            except Exception as e:
                st.error(f"Error: {e}")

        else:
            st.warning("Please enter anime name")


# =========================
# ⚔️ BATTLE SYSTEM
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

        if st.button("Start Battle") and a and b:
            result = battle_1v1(a, b)
            st.success("🏆 Winner: " + result["winner"])


# =========================
# ✨ QUOTES
# =========================
with tab4:

    theme = st.selectbox(
        "Theme",
        ["Motivational", "Friendship", "Success", "Sad", "Funny"]
    )

    if st.button("Generate Quote"):
        st.success(generate_quote(theme))


# =========================
# 🎭 QUIZ
# =========================
with tab5:

    q1 = st.radio("Motivation", ["Power", "Friendship", "Freedom", "Knowledge"])
    q2 = st.radio("Fight Style", ["Head on", "Strategic", "Support friends", "Adapt"])
    q3 = st.radio("Trait", ["Courage", "Intelligence", "Loyalty", "Calmness"])
    q4 = st.radio("Role", ["Leader", "Support", "Lone wolf", "Strategist"])
    q5 = st.radio("Weakness", ["Anger", "Trust issues", "Overconfidence", "Fear"])
    q6 = st.radio("Power Type", ["Physical strength", "Speed", "Magic/Skills", "Tactical mind"])

    if st.button("Result"):
        result = get_character_match(q1, q2, q3, q4, q5, q6)
        st.success("🎌 You are: " + result)
