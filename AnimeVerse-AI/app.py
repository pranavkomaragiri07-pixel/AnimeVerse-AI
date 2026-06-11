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
# SAFE QUOTE FUNCTION (FIXED)
# =========================
def generate_quote(theme):

    quotes = {
        "Motivational": [
            ("Naruto Uzumaki", "Hard work is worthless for those that don't believe in themselves."),
            ("Rock Lee", "A dropout will beat a genius through hard work."),
            ("All Might", "You too can become a hero if you push forward!"),
            ("Izuku Midoriya", "If you want to win, work harder than anyone else."),
        ],

        "Friendship": [
            ("Naruto Uzumaki", "Failing doesn’t give you a reason to give up."),
            ("Luffy", "I don’t care if I die fighting for my friends."),
            ("Natsu Dragneel", "We fight together, no matter what."),
        ],

        "Success": [
            ("Itachi Uchiha", "People live their lives bound by what they accept as correct."),
            ("Levi Ackerman", "The only thing we are allowed to do is believe that we won't regret the choice we made."),
            ("Tanjiro Kamado", "No matter how many times it breaks your heart, stand up."),
        ],

        "Sad": [
            ("Pain", "Feel pain, accept pain, know pain."),
            ("Itachi Uchiha", "Even the strongest of us carry suffering."),
            ("Griffith", "Dreams aren’t meant to be easy."),
        ],

        "Funny": [
            ("Saitama", "Ok."),
            ("Goku", "Training? I prefer eating first."),
            ("Kazuma", "I just want a normal life… why is this so hard?"),
        ]
    }

    char, quote = random.choice(quotes.get(theme, [("Anime", "Stay strong!")]))
    return f"{quote}\n\n— {char}"


# =========================
# PERSONA MATCH (UNCHANGED LOGIC)
# =========================
def get_character_match(q1, q2, q3, q4, q5, q6):

    score = {
        "Naruto Uzumaki": 0,
        "Monkey D. Luffy": 0,
        "Goku": 0,
        "Gojo Satoru": 0,
        "Itachi Uchiha": 0,
        "Levi Ackerman": 0,
        "Eren Yeager": 0,
        "Saitama": 0
    }
    for a in [q1, q2, q3, q4, q5, q6]:

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
            score["Itachi Uchiha"] += 1

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
            score["Itachi Uchiha"] += 3
            score["Saitama"] += 1

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
# 🔍 ANIME SEARCH (FIXED SAFE)
# =========================
with tab1:

    st.header("Search Anime")
    name = st.text_input("Enter anime name")

    if st.button("Search") and name:

        url = f"https://api.jikan.moe/v4/anime?q={name}&limit=1"

        try:
            res = requests.get(url).json()
            data = res.get("data", [])

            if data:
                anime = data[0]

                st.success(anime.get("title", "No title"))
                st.image(anime["images"]["jpg"]["image_url"])
                st.write("⭐ Rating:", anime.get("score", "N/A"))
                st.write("🎬 Episodes:", anime.get("episodes", "N/A"))
                st.write("📖 Synopsis:", anime.get("synopsis", "N/A"))
            else:
                st.error("No anime found.")

        except:
            st.error("Failed to fetch anime data.")

# =========================
# ⚔️ BATTLE SYSTEM (FIXED UI)
# =========================
with tab3:

    mode = st.selectbox(
        "Select Mode",
        ["1v1 Battle", "2v2 Battle", "4v4 Battle", "Tournament Arc", "Survival Arena"]
    )

    # ---------------- 1v1 ----------------
    if mode == "1v1 Battle":

        a = st.text_input("Character A")
        b = st.text_input("Character B")

        if st.button("Start Battle") and a and b:

            result = battle_1v1(a, b)

            st.success(f"🏆 Winner: {result['winner']}")

            fa = result["fighter_a"]["stats"]
            fb = result["fighter_b"]["stats"]

            st.markdown("## ⚔️ BATTLE STATS")

            col1, col2 = st.columns(2)

            # LEFT = A
            with col1:
                st.markdown(f"### 🔵 {a}")
                for k, v in fa.items():
                    st.write(k)
                    st.progress(v / 100)

            # RIGHT = B
            with col2:
                st.markdown(f"### 🔴 {b}")
                for k, v in fb.items():
                    st.write(k)
                    st.progress(v / 100)

            st.markdown("## 🏅 CATEGORY WINNERS")

            a_win = 0
            b_win = 0

            for k, v in result["category_winners"].items():
                if v == a:
                    a_win += 1
                    st.write(f"⚡ {k} → 🥇 {a}")
                else:
                    b_win += 1
                    st.write(f"⚡ {k} → 🥇 {b}")

            final = a if a_win > b_win else b

            st.success(f"🔥 FINAL WINNER: {final}")
            st.info(result["story"])

    # ---------------- 2v2 ----------------
    elif mode == "2v2 Battle":

        a1 = st.text_input("A1")
        a2 = st.text_input("A2")
        b1 = st.text_input("B1")
        b2 = st.text_input("B2")

        if st.button("Fight") and all([a1, a2, b1, b2]):

            result = battle_2v2([a1, a2], [b1, b2])

            st.success(result["winner"])
            st.info(result["story"])

    # ---------------- 4v4 ----------------
    elif mode == "4v4 Battle":

        t1 = st.text_area("Team Alpha")
        t2 = st.text_area("Team Omega")

        if st.button("Battle") and t1 and t2:

            result = battle_4v4(t1.split("\n"), t2.split("\n"))

            st.success(result["winner"])
            st.info(result["story"])

    # ---------------- TOURNAMENT ----------------
    elif mode == "Tournament Arc":

        fighters = st.text_area("Enter fighters")

        if st.button("Run") and fighters:

            result = run_tournament(fighters.split("\n"))

            st.success("👑 " + result["champion"])
            st.info(result["story"])

    # ---------------- SURVIVAL ----------------
    elif mode == "Survival Arena":

        hero = st.text_input("Hero")

        if st.button("Start") and hero:

            result = survival_mode(hero)

            st.success(result["character"])
            st.write("⭐ Score:", result["score"])
            st.info(result["story"])

# =========================
# ✨ QUOTES
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
