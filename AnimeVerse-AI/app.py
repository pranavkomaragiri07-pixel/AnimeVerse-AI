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
# CSS LOADER
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

    # =========================
    #  MOTIVATIONAL
    # =========================
    "🔥Motivational": [
        ("Naruto Uzumaki", "I'm not gonna run away, I never go back on my word. That's my ninja way!"),
        ("Rock Lee", "A dropout will beat a genius through hard work."),
        ("All Might", "Now it's your turn. Go beyond your limits! Plus Ultra!"),
        ("Asta", "No matter how hard I fall, I will rise again!"),
    ],

    # =========================
    # 🤝 FRIENDSHIP
    # =========================
    "🤝Friendship": [
        ("Monkey D. Luffy", "I don’t care if I die protecting my friends."),
        ("Naruto Uzumaki", "I will never let my friends die."),
        ("Natsu Dragneel", "We’re not alone when we have friends."),
        ("Eren Yeager", "If we die, we die together."),
    ],

    # =========================
    # 🏆 SUCCESS / AMBITION
    # =========================
    "🏆Success": [
        ("Itachi Uchiha", "People live bound by what they accept as correct."),
        ("Light Yagami", "I am justice. I will become the god of a new world."),
        ("Levi Ackerman", "The only thing we can do is move forward."),
        ("Madara Uchiha", "Wake up to reality. Nothing goes as planned."),
    ],

    # =========================
    # 😢 SAD / EMOTIONAL
    # =========================
    "😢Sad": [
        ("Nagato (Pain)", "Those who do not understand pain can never understand true peace."),
        ("Itachi Uchiha", "Forgive me, Sasuke... this is the last time."),
        ("Griffith", "Dreams… are something you sacrifice everything for."),
        ("Rengoku", "Set your heart ablaze, even in suffering."),
    ],

    # =========================
    # 😂 FUNNY / LIGHT
    # =========================
    "😂Funny": [
        ("Saitama", "Ok."),
        ("Goku", "I'm hungry again... is there food?"),
        ("Kakashi", "Sorry I'm late... I got lost on the path of life."),
        ("Zenitsu", "I don’t want to die yet!!"),
    ]
}
    return random.choice(quotes.get(theme, [("Anime", "Stay strong")]))


# =========================
# CHARACTER MATCH
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

        if a == "Freedom":
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

        if a == "Courage":
            score["Naruto Uzumaki"] += 2
            score["Monkey D. Luffy"] += 3
            score["Goku"] += 2

        if a in ["Anger", "Overconfidence"]:
            score["Eren Yeager"] += 3

        if a == "Calmness":
            score["Itachi Uchiha"] += 2
            score["Gojo Satoru"] += 2

        if a == "Speed":
            score["Goku"] += 2
            score["Naruto Uzumaki"] += 1
            score["Monkey D. Luffy"] += 1

        if a == "Leader":
            score["Naruto Uzumaki"] += 2
            score["Eren Yeager"] += 2
            score["Monkey D. Luffy"] += 2

        if a == "Adapt":
            score["Levi Ackerman"] += 2
            score["Goku"] += 2
            score["Itachi Uchiha"] += 3
            score["Saitama"] += 1

    return max(score, key=score.get)


# =========================
# UI HEADER
# =========================
st.title("🏆 AnimeVerse AI")
st.subheader("AI-Powered Anime Companion")

# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
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

                    st.write(f"⭐ Rating: {anime.get('score')}")
                    st.write(f"🎬 Episodes: {anime.get('episodes')}")
                    st.write(f"📌 Status: {anime.get('status')}")

                    genres = ", ".join(g["name"] for g in anime["genres"])
                    st.write(f"🎭 Genres: {genres}")

                    st.write(f"📖 Synopsis: {anime.get('synopsis')}")


# =========================
# BATTLE
# =========================
with tab2:
    st.header("⚔️ Battle Simulator")

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

                st.markdown("## 🏆 WINNER!!")
                st.success(result["winner"])

                st.markdown("### 📖 Story")
                st.write(result["story"])

                st.markdown("### ⚔️ Category Winners 🏅")
                for k, v in result["category_winners"].items():
                    st.write(f"🏅 {k} → {v}")


# =========================
# QUOTE
# =========================
with tab3:
    st.header("✨ Quote Generator")

    theme = st.selectbox("Theme", ["Motivational","Friendship","Success","Sad","Funny"])

    if st.button("Generate Quote"):
        st.success(generate_quote(theme))


# =========================
# QUIZ
# =========================
with tab4:
    st.header("🎭 Personality Quiz")

    q1 = st.radio("Motivation", ["Power","Friendship","Freedom","Knowledge"])
    q2 = st.radio("Fight Style", ["Head on","Strategic","Support friends","Adapt"])
    q3 = st.radio("Trait", ["Courage","Intelligence","Loyalty","Calmness"])
    q4 = st.radio("Role", ["Leader","Support","Lone wolf","Strategist"])
    q5 = st.radio("Weakness", ["Anger","Trust issues","Overconfidence","Fear"])
    q6 = st.radio("Power Type", ["Physical strength","Speed","Magic/Skills","Tactical mind"])

    if st.button("Reveal Result"):
        character = get_character_match(q1,q2,q3,q4,q5,q6)
        st.markdown("## 🎌 Your Anime Match")
        st.success(character)
