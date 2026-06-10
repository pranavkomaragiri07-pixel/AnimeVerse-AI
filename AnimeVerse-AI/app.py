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
# SAFE FUNCTIONS
# =========================

def generate_quote(theme):
    quotes = {
        "Motivational": [
            ("Naruto Uzumaki", "I'm not gonna run away!"),
            ("All Might", "It's fine now! Because I am here!"),
        ],
        "Friendship": [
            ("Luffy", "I will never abandon my friends!"),
            ("Naruto", "Friends are my power!"),
        ],
        "Success": [
            ("Levi", "The only thing we can do is move forward."),
            ("Itachi", "Growth comes from sacrifice."),
        ],
        "Sad": [
            ("Pain", "Pain is the only way to understand peace."),
            ("Itachi", "Even heroes suffer."),
        ],
        "Funny": [
            ("Saitama", "Ok."),
            ("Goku", "I’m hungry again."),
        ]
    }

    char, quote = random.choice(quotes.get(theme, [("Anime", "Stay strong!")]))
    return f"{quote}\n\n— {char}"


def get_character_match(q1, q2, q3, q4, q5, q6):

    score = {
        "Naruto Uzumaki": 0,
        "Monkey D. Luffy": 0,
        "Gojo Satoru": 0,
        "Itachi Uchiha": 0,
        "Levi Ackerman": 0
    }

    answers = [q1, q2, q3, q4, q5, q6]

    for a in answers:

        if a in ["Friendship", "Support", "Loyalty"]:
            score["Naruto Uzumaki"] += 2
            score["Monkey D. Luffy"] += 1

        if a in ["Strategic", "Intelligence"]:
            score["Itachi Uchiha"] += 2
            score["Levi Ackerman"] += 2

        if a in ["Power", "Overconfidence"]:
            score["Gojo Satoru"] += 2

        if a in ["Freedom"]:
            score["Monkey D. Luffy"] += 2

    return max(score, key=score.get)


# =========================
# APP CONFIG
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
# HEADER
# =========================

st.title("🏆 AnimeVerse AI")
st.subheader("AI-Powered Anime Battle Simulator")

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
# 🔍 ANIME SEARCH
# =========================

with tab1:

    st.header("Search Anime")

    name = st.text_input("Enter anime name")

    if st.button("Search"):

        if name:

            url = f"https://api.jikan.moe/v4/anime?q={name}&limit=1"
            res = requests.get(url).json()

            if res["data"]:
                anime = res["data"][0];

                st.success(anime["title"])
                st.image(anime["images"]["jpg"]["image_url"])
                st.write("⭐", anime["score"])
                st.write("🎬 Episodes:", anime["episodes"])
                st.write("📖", anime["synopsis"])

# =========================
# ⚔️ BATTLE SYSTEM
# =========================

with tab3:

    mode = st.selectbox(
        "Select Mode",
        ["1v1 Battle", "2v2 Battle", "4v4 Battle", "Tournament Arc", "Survival Arena"]
    )

    # -----------------
    # 1v1
    # -----------------
    if mode == "1v1 Battle":

        a = st.text_input("Character A")
        b = st.text_input("Character B")

        if st.button("Start Battle") and a and b:

            result = battle_1v1(a, b)

            st.success(f"🏆 Winner: {result['winner']}")

            st.markdown("### ⚔️ Stats Comparison")

            fa = result["fighter_a"]["stats"]
            fb = result["fighter_b"]["stats"]

            for stat in fa:

                col1, col2 = st.columns(2)

                with col1:
                    st.write(a, stat, fa[stat])
                    st.progress(fa[stat] / 100)

                with col2:
                    st.write(b, stat, fb[stat])
                    st.progress(fb[stat] / 100)

            st.markdown("### 🏅 Category Winners")

            for k, v in result["category_winners"].items():
                st.write(f"{k} → {v}")

            st.markdown("### 📖 Story")
            st.write(result["story"])

    # -----------------
    # 2v2
    # -----------------
    elif mode == "2v2 Battle":

        a1 = st.text_input("A1")
        a2 = st.text_input("A2")
        b1 = st.text_input("B1")
        b2 = st.text_input("B2")

        if st.button("Fight") and all([a1, a2, b1, b2]):

            result = battle_2v2([a1, a2], [b1, b2])

            st.success(result["winner"])
            st.write(result["story"])

            st.markdown("### 🏅 Category Winners")
            for k, v in result["category_winners"].items():
                st.write(k, "→", v)

    # -----------------
    # 4v4
    # -----------------
    elif mode == "4v4 Battle":

        t1 = st.text_area("Team Alpha")
        t2 = st.text_area("Team Omega")

        if st.button("Battle") and t1 and t2:

            team_a = t1.split("\n")
            team_b = t2.split("\n")

            result = battle_4v4(team_a, team_b)

            st.success(result["winner"])
            st.write(result["story"])

            st.markdown("### 🏅 Category Winners")
            for k, v in result["category_winners"].items():
                st.write(k, "→", v)

    # -----------------
    # TOURNAMENT
    # -----------------
    elif mode == "Tournament Arc":

        fighters = st.text_area("Enter fighters")

        if st.button("Run") and fighters:

            result = run_tournament(fighters.split("\n"))

            st.success("👑 Champion: " + result["champion"])
            st.write(result["rounds"])
            st.write(result["story"])

    # -----------------
    # SURVIVAL
    # -----------------
    elif mode == "Survival Arena":

        hero = st.text_input("Hero")

        if st.button("Start") and hero:

            result = survival_mode(hero)

            st.success(result["character"])
            st.write("Score:", result["score"])
            st.write(result["rounds"])
            st.write(result["story"])

# =========================
# ✨ QUOTE
# =========================

with tab4:

    theme = st.selectbox("Theme", ["Motivational", "Friendship", "Success", "Sad", "Funny"])

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
