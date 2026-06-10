import streamlit as st
import requests
import random
import streamlit.components.v1 as components

# =========================
# BACKEND IMPORT
# =========================
from battle import (
    battle_1v1,
    battle_2v2,
    battle_4v4,
    run_tournament,
    survival_mode
)

# =========================
# CONFIG
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
# 🎆 FIREWORKS
# =========================
def show_fireworks():
    components.html("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
        for (let i = 0; i < 5; i++) {
            setTimeout(() => {
                confetti({
                    particleCount: 150,
                    spread: 100,
                    origin: { y: 0.6 }
                });
            }, i * 400);
        }
    </script>
    """, height=300)


# =========================
# 🏆 GLOW WINNER
# =========================
def show_winner_glow(name, title="WINNER!!"):
    components.html(f"""
    <style>
        .title {{
            text-align:center;
            font-size:55px;
            font-weight:900;
            color:white;
            animation: glow 1s infinite alternate;
        }}

        .name {{
            text-align:center;
            font-size:28px;
            color:#ff4b4b;
            font-weight:bold;
        }}

        @keyframes glow {{
            0% {{
                text-shadow: 0 0 10px red, 0 0 20px #ff4b4b;
            }}
            100% {{
                text-shadow: 0 0 40px red, 0 0 80px #ff6b6b;
            }}
        }}
    </style>

    <div class="title">{title}</div>
    <div class="name">{name}</div>
    """, height=220)


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
        r = requests.get(f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1").json()

        if r["data"]:
            anime = r["data"][0]
            st.success(anime["title"])
            st.image(anime["images"]["jpg"]["image_url"])


# =========================
# ⚔️ BATTLE SYSTEM
# =========================
with tab3:
    st.header("⚔️ Battle Simulator")

    mode = st.selectbox(
        "Select Mode",
        ["1v1 Battle", "2v2 Battle", "4v4 Battle", "Tournament Arc"]
    )

    # ================= 1v1 =================
    if mode == "1v1 Battle":
        a = st.text_input("Character A")
        b = st.text_input("Character B")

        if st.button("Start Battle"):
            result = battle_1v1(a, b)

            st.success(f"🏆 Winner: {result['winner']}")

            show_fireworks()
            show_winner_glow(result["winner"], "WINNER!!")

            # stats
            st.markdown("## ⚔️ Stats")
            fa = result["fighter_a"]["stats"]
            fb = result["fighter_b"]["stats"]

            for k in fa:
                col1, col2 = st.columns(2)
                with col1:
                    st.write(a, k, fa[k])
                with col2:
                    st.write(b, k, fb[k])

            # category
            st.markdown("## 🏅 Category Winners")
            for k, v in result["category_winners"].items():
                st.write(k, "→", v)

            st.write(result["story"])


    # ================= 2v2 =================
    elif mode == "2v2 Battle":

        a1 = st.text_input("Team A 1")
        a2 = st.text_input("Team A 2")
        b1 = st.text_input("Team B 1")
        b2 = st.text_input("Team B 2")

        if st.button("Start Battle"):
            result = battle_2v2([a1, a2], [b1, b2])

            st.success(f"🏆 Winner: {result['winner']}")

            show_fireworks()
            show_winner_glow(result["winner"], "WINNER!!")

            st.markdown("## 🏅 Category Winners")
            for k, v in result["category_winners"].items():
                st.write(k, "→", v)

            st.write(result["story"])


    # ================= 4v4 =================
    elif mode == "4v4 Battle":

        t1 = st.text_area("Team Alpha (4 names)")
        t2 = st.text_area("Team Omega (4 names)")

        if st.button("Start Battle"):
            result = battle_4v4(t1.split("\n"), t2.split("\n"))

            st.success(f"🏆 Winner: {result['winner']}")

            show_fireworks()
            show_winner_glow(result["winner"], "WINNER!!")

            st.markdown("## 🏅 Category Winners")
            for k, v in result["category_winners"].items():
                st.write(k, "→", v)

            st.write(result["story"])


    # ================= TOURNAMENT =================
    elif mode == "Tournament Arc":

        fighters = st.text_area("Enter fighters")

        if st.button("Start Tournament"):
            result = run_tournament(fighters.split("\n"))

            st.success(f"👑 Champion: {result['champion']}")

            show_fireworks()
            show_winner_glow(result["champion"], "CHAMPION!!")

            st.markdown("## 🔥 Rounds")
            st.write(result["rounds"])

            st.write(result["story"])


# =========================
# QUOTE
# =========================
with tab4:
    theme = st.selectbox("Theme", ["Motivational","Friendship","Success","Sad","Funny"])

    if st.button("Generate Quote"):
        st.success("Stay strong!")


# =========================
# QUIZ
# =========================
with tab5:
    q1 = st.radio("Motivation", ["Power","Friendship","Freedom","Knowledge"])
    q2 = st.radio("Fight Style", ["Head on","Strategic","Support friends","Adapt"])
    q3 = st.radio("Trait", ["Courage","Intelligence","Loyalty","Calmness"])
    q4 = st.radio("Role", ["Leader","Support","Lone wolf","Strategist"])
    q5 = st.radio("Weakness", ["Anger","Trust issues","Overconfidence","Fear"])
    q6 = st.radio("Power Type", ["Physical strength","Speed","Magic/Skills","Tactical mind"])

    if st.button("Reveal Result"):
        st.success("Your Anime Match: Saitama")
