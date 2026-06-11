import streamlit as st
import requests
import random

from battle import (
    battle_1v1,
    battle_2v2,
    battle_4v4,
    run_tournament,
    survival_mode
)

# =========================
# QUOTES
# =========================
def generate_quote(theme):

    quotes = {
        "Motivational": [
            ("Naruto Uzumaki", "Hard work is worthless for those that don't believe in themselves."),
            ("Rock Lee", "A dropout will beat a genius through hard work."),
            ("All Might", "You too can become a hero if you push forward!"),
        ],

        "Friendship": [
            ("Naruto Uzumaki", "Failing doesn’t give you a reason to give up."),
            ("Luffy", "I don’t care if I die fighting for my friends."),
        ],

        "Success": [
            ("Itachi Uchiha", "People live bound by what they accept as correct."),
            ("Levi Ackerman", "Regret comes from hesitation."),
        ],

        "Sad": [
            ("Pain", "Feel pain, accept pain, know pain."),
            ("Itachi Uchiha", "Even the strongest carry suffering."),
        ],

        "Funny": [
            ("Saitama", "Ok."),
            ("Goku", "Training? I prefer eating."),
        ]
    }

    char, quote = random.choice(quotes.get(theme, [("Anime", "Stay strong!")]))
    return f"{quote}\n\n— {char}"


# =========================
# PERSONA QUIZ
# =========================
def get_character_match(q1, q2, q3, q4, q5, q6):

    score = {
        "Naruto Uzumaki": 0,
        "Monkey D. Luffy": 0,
        "Goku": 0,
        "Itachi Uchiha": 0,
        "Levi Ackerman": 0,
    }

    for a in [q1, q2, q3, q4, q5, q6]:

        if a in ["Friendship", "Support", "Loyalty"]:
            score["Naruto Uzumaki"] += 2
            score["Monkey D. Luffy"] += 2

        if a in ["Freedom"]:
            score["Monkey D. Luffy"] += 3

        if a in ["Power", "Physical strength"]:
            score["Goku"] += 3

        if a in ["Strategic", "Intelligence"]:
            score["Itachi Uchiha"] += 3
            score["Levi Ackerman"] += 2

        if a in ["Courage"]:
            score["Naruto Uzumaki"] += 2

    return max(score, key=score.get)


# =========================
# CONFIG
# =========================
st.set_page_config(page_title="AnimeVerse AI", page_icon="⚔️", layout="wide")

st.title("🏆 AnimeVerse AI")
st.subheader("AI Anime Battle System")


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

    st.header("Search Anime")

    name = st.text_input("Enter anime name")

    if st.button("Search") and name:

        try:
            url = f"https://api.jikan.moe/v4/anime?q={name}&limit=1"
            res = requests.get(url).json()
            data = res.get("data", [])

            if data:
                anime = data[0]

                st.success(anime["title"])
                st.image(anime["images"]["jpg"]["image_url"])

                st.write("⭐ Rating:", anime.get("score"))
                st.write("🎬 Episodes:", anime.get("episodes"))
                st.write("📖 Synopsis:", anime.get("synopsis"))

            else:
                st.error("No anime found")

        except:
            st.error("API error")


# =========================
# BATTLE SYSTEM
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

            st.markdown("## ⚔️ VS BATTLE")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"### 🔵 {a}")
                for k, v in fa.items():
                    st.write(k)
                    st.progress(v / 100)

            with col2:
                st.markdown(f"### 🔴 {b}")
                for k, v in fb.items():
                    st.write(k)
                    st.progress(v / 100)

            st.markdown("## 🏅 Category Winners")

            a_win = 0
            b_win = 0

            for k, v in result["category_winners"].items():
                if v == a:
                    a_win += 1
                else:
                    b_win += 1

                st.write(f"{k} → 🏅 {v}")

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

            st.success(f"🏆 Winner: {result['winner']}")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("## 🔵 Team A")
                for f in result["team_a_stats"]:
                    st.write(f["name"])
                    for k, v in f["stats"].items():
                        st.write(k)
                        st.progress(v / 100)

            with col2:
                st.markdown("## 🔴 Team B")
                for f in result["team_b_stats"]:
                    st.write(f["name"])
                    for k, v in f["stats"].items():
                        st.write(k)
                        st.progress(v / 100)
            
            st.markdown("## ⚔️ TEAM STATS COMPARISON")

            team_a = result["team_a_total"]
            team_b = result["team_b_total"]
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 🔵 Team A")
            with col2:
                st.markdown("### 🔴 Team B")
            for stat in team_a.keys():
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"{stat}")
                    st.progress(team_a[stat] / 100)
                with col2:
                    st.write(f"{stat}")
                    st.progress(team_b[stat] / 100)


    # ---------------- 4v4 ----------------
    elif mode == "4v4 Battle":

        t1 = st.text_area("Team Alpha")
        t2 = st.text_area("Team Omega")

        if st.button("Battle") and t1 and t2:

            team_a = t1.split("\n")
            team_b = t2.split("\n")

            result = battle_4v4(team_a, team_b)

            st.success(f"🏆 Winner: {result['winner']}")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("## 🔵 Team Alpha")
                for f in result["team_a_stats"]:
                    st.write(f["name"])
                    for k, v in f["stats"].items():
                        st.write(k)
                        st.progress(v / 100)

            with col2:
                st.markdown("## 🔴 Team Omega")
                for f in result["team_b_stats"]:
                    st.write(f["name"])
                    for k, v in f["stats"].items():
                        st.write(k)
                        st.progress(v / 100)

            st.markdown("## ⚔️ TEAM STATS COMPARISON")

            team_a = result["team_a_total"]
            team_b = result["team_b_total"]
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 🔵 Team A")
            with col2:
                st.markdown("### 🔴 Team B")
            for stat in team_a.keys():
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"{stat}")
                    st.progress(team_a[stat] / 100)
                with col2:
                    st.write(f"{stat}")
                    st.progress(team_b[stat] / 100)


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
# QUOTES
# =========================
with tab4:

    theme = st.selectbox("Theme", ["Motivational", "Friendship", "Success", "Sad", "Funny"])

    if st.button("Generate Quote"):
        st.success(generate_quote(theme))


# =========================
# QUIZ
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
