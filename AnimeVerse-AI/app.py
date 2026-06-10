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
# CLEAN WINNER UI (NO TOP GREEN BAR)
# =========================
def show_winner(name):
    st.markdown(f"""
        <div style="
            text-align:center;
            font-size:50px;
            font-weight:900;
            color:#ff3b3b;
            text-shadow:0 0 20px red;
            margin-top:-20px;
        ">
        🏆 WINNER!!<br>
        <span style="font-size:30px;color:white;">{name}</span>
        </div>
    """, unsafe_allow_html=True)


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
# ANIME SEARCH
# =========================
with tab1:
    st.header("🔍 Anime Search")

    anime_name = st.text_input("Enter Anime Name")

    if st.button("Search Anime"):
        r = requests.get(f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1").json()

        if r["data"]:
            anime = r["data"][0]
            st.image(anime["images"]["jpg"]["image_url"])
            st.success(anime["title"])


# =========================
# ⚔️ BATTLE SYSTEM (FIXED UI)
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
            winner = result["winner"]

            st.markdown("---")  # removes big gap

            show_winner(winner)

            # ================= STATS AS BARS =================
            st.markdown("## ⚔️ Stats Comparison")

            fa = result["fighter_a"]["stats"]
            fb = result["fighter_b"]["stats"]

            for stat in fa:
                col1, col2 = st.columns(2)

                with col1:
                    st.write(a, stat)
                    st.progress(fa[stat] / 100)

                with col2:
                    st.write(b, stat)
                    st.progress(fb[stat] / 100)

            # ================= CATEGORY WINNERS =================
            st.markdown("## 🏅 Category Winners")

            for k, v in result["category_winners"].items():

                if v == winner:
                    st.markdown(f"🔥 🏅 **{k} → {v} (WINNER BOOST)**")
                else:
                    st.write(f"🏅 {k} → {v}")

            st.write(result["story"])


    # ================= 2v2 =================
    elif mode == "2v2 Battle":

        a1 = st.text_input("Team A 1")
        a2 = st.text_input("Team A 2")
        b1 = st.text_input("Team B 1")
        b2 = st.text_input("Team B 2")

        if st.button("Start Battle"):

            result = battle_2v2([a1, a2], [b1, b2])
            winner = result["winner"]

            st.markdown("---")
            show_winner(winner)

            st.markdown("## 🏅 Category Winners")

            for k, v in result["category_winners"].items():
                if v == winner:
                    st.markdown(f"🔥 🏅 **{k} → {v}**")
                else:
                    st.write(f"🏅 {k} → {v}")

            st.write(result["story"])


    # ================= 4v4 =================
    elif mode == "4v4 Battle":

        t1 = st.text_area("Team Alpha")
        t2 = st.text_area("Team Omega")

        if st.button("Start Battle"):

            result = battle_4v4(t1.split("\n"), t2.split("\n"))
            winner = result["winner"]

            st.markdown("---")
            show_winner(winner)

            st.markdown("## 🏅 Category Winners")

            for k, v in result["category_winners"].items():
                if v == winner:
                    st.markdown(f"🔥 🏅 **{k} → {v}**")
                else:
                    st.write(f"🏅 {k} → {v}")

            st.write(result["story"])


    # ================= TOURNAMENT =================
    elif mode == "Tournament Arc":

        fighters = st.text_area("Enter fighters")

        if st.button("Start Tournament"):

            result = run_tournament(fighters.split("\n"))
            winner = result["champion"]

            st.markdown("---")
            show_winner(winner)

            st.markdown("## 🔥 Tournament Rounds")
            st.write(result["rounds"])

            st.write(result["story"])


# =========================
# QUOTES
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
