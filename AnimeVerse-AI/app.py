import streamlit as st
import os

# =========================
# BACKEND IMPORTS
# =========================
from battle import battle_1v1, battle_2v2, battle_4v4, run_tournament, survival_mode
from quote_generator import generate_quote
from personality_quiz import get_character_match

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AnimeVerse AI",
    page_icon="⚔️",
    layout="wide"
)

# =========================
# SAFE CSS LOADER (FIXED ERROR)
# =========================
css_path = os.path.join(os.path.dirname(__file__), "styles.css")

if os.path.exists(css_path):
    with open(css_path, "r") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
else:
    st.warning("styles.css not found - UI styling disabled")

# =========================
# HEADER
# =========================
st.title("🏆 AnimeVerse AI")
st.subheader("AI-Powered Anime Companion")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔍 Anime Search",
    "🎌 AI Recommender",
    "⚔️ Battle Simulator",
    "✨ Quote Generator",
    "🎭 Personality Quiz"
])

# =========================
# TAB 1 - ANIME SEARCH
# =========================
with tab1:
    st.header("🔍 Anime Search")

    anime_name = st.text_input("Enter Anime Name")

    if st.button("Search Anime"):
        st.info("Backend API integration pending")

    st.subheader("Anime Details")
    st.write("🖼️ Poster: Backend Output")
    st.write("⭐ Rating: Backend Output")
    st.write("🎬 Episodes: Backend Output")
    st.write("🎭 Genres: Backend Output")
    st.write("📅 Release Date: Backend Output")
    st.write("📖 Synopsis: Backend Output")

# =========================
# TAB 2 - RECOMMENDER
# =========================
with tab2:
    st.header("🎌 AI Anime Recommender")

    anime_input = st.text_input("Enter anime you enjoyed")

    if st.button("Get Recommendations"):
        st.info("Backend integration pending")

    st.subheader("Recommendations")
    st.write("🎌 Recommendation 1")
    st.write("🎌 Recommendation 2")
    st.write("🎌 Recommendation 3")

# =========================
# TAB 3 - BATTLE SIMULATOR
# =========================
with tab3:
    st.header("⚔️ Anime Battle Simulator")

    mode = st.selectbox(
        "Select Mode",
        ["1v1 Battle", "2v2 Battle", "4v4 Battle", "Tournament Arc", "Survival Arena"]
    )

    if mode == "1v1 Battle":
        a = st.text_input("Character A")
        b = st.text_input("Character B")

        if st.button("Start Battle"):
            if a and b:
                result = battle_1v1(a, b)
                st.success(f"🏆 Winner: {result['winner']}")
                st.write(result["story"])
            else:
                st.error("Enter both characters")

    elif mode == "2v2 Battle":
        a1 = st.text_input("Team A Fighter 1")
        a2 = st.text_input("Team A Fighter 2")
        b1 = st.text_input("Team B Fighter 1")
        b2 = st.text_input("Team B Fighter 2")

        if st.button("Start Team Battle"):
            if all([a1, a2, b1, b2]):
                result = battle_2v2([a1, a2], [b1, b2])
                st.success(f"🏆 Winner: {result['winner']}")
                st.write(result["story"])
            else:
                st.error("Fill all fields")

    elif mode == "4v4 Battle":
        t1 = st.text_area("Team Alpha")
        t2 = st.text_area("Team Omega")

        if st.button("Start 4v4 Battle"):
            if t1 and t2:
                result = battle_4v4(t1.split("\n"), t2.split("\n"))
                st.success(f"🏆 Winner: {result['winner']}")
                st.write(result["story"])
            else:
                st.error("Enter teams")

    elif mode == "Tournament Arc":
        fighters = st.text_area("Enter Fighters (one per line)")

        if st.button("Start Tournament"):
            if fighters:
                result = run_tournament(fighters.split("\n"))
                st.success(f"👑 Champion: {result['champion']}")
                st.write(result["story"])
            else:
                st.error("Enter fighters")

    elif mode == "Survival Arena":
        hero = st.text_input("Select Hero")

        if st.button("Enter Arena"):
            if hero:
                result = survival_mode(hero)
                st.success(result["result"])
                st.write(f"⭐ Score: {result['score']}")
            else:
                st.error("Enter hero name")

# =========================
# TAB 4 - QUOTE GENERATOR
# =========================
with tab4:
    st.header("✨ Anime Quote Generator")

    mode = st.radio("Mode", ["Real Quote", "AI Quote"])
    theme = st.selectbox("Theme", ["Motivational", "Friendship", "Success", "Sad", "Funny"])

    if st.button("Generate Quote"):
        st.info("Backend pending integration")

# =========================
# TAB 5 - PERSONALITY QUIZ
# =========================
with tab5:
    st.header("🎭 Personality Quiz")

    q1 = st.radio("What motivates you?", ["Power", "Friendship", "Freedom", "Knowledge"])
    q2 = st.radio("How do you fight?", ["Head on", "Strategic", "Support friends", "Adapt"])

    if st.button("Reveal Result"):
        st.info("Backend pending integration")
