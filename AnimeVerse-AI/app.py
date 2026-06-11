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
# CHARACTER QUIZ
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

            # TEAM COMPARISON CENTERED
            st.markdown("## ⚔️ TEAM STATS COMPARISON")

            team_a = result["team_a_total"]
            team_b = result["team_b_total"]

            for stat in team_a.keys():
                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"🔵 {stat}")
                    st.progress(team_a[stat] / 100)

                with col2:
                    st.write(f"🔴 {stat}")
                    st.progress(team_b[stat] / 100)

            st.info(result["story"])


    # ---------------- 4v4 ----------------
    elif mode == "4v4 Battle":

        t1 = st.text_area("Team Alpha")
        t2 = st.text_area("Team Omega")

        if st.button("Battle") and t1 and t2:

            team_a = t1.split("\n")
            team_b = t2.split("\n")

            result = battle_4v4(team_a, team_b)

            st.success(f"🏆 Winner: {result['winner']}")

            st.markdown("## ⚔️ TEAM STATS COMPARISON")

            team_a = result["team_a_total"]
            team_b = result["team_b_total"]

            for stat in team_a.keys():
                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"🔵 {stat}")
                    st.progress(team_a[stat] / 100)

                with col2:
                    st.write(f"🔴 {stat}")
                    st.progress(team_b[stat] / 100)

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
# QUOTES
# =========================
with tab4:

    theme = st.selectbox("Theme", ["Motivational", "Friendship", "Success", "Sad", "Funny"])

    if st.button("Generate Quote"):
        st.success(generate_quote(theme))


# =========================
# QUIZ (CENTER RESULT + IMAGE OVERLAY)
# =========================

CHAR_IMAGES = {
    "goku": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/fcc8540c-16f2-442f-9a10-1b35f518cdd4/dflg7x2-6d37bf82-41e6-41d9-99ba-e4cf0ee6bb93.jpg",
    "naruto uzumaki": "https://preview.redd.it/explain-of-six-paths-sage-mode-and-six-paths-senjutsu-does-v0-5yluzjjtjny71.png",
    "luffy": "https://i.imgur.com/8Q9ZV.png",
    "itachi uchiha": "https://i.imgur.com/3QZQZ.png",
    "levi ackerman": "https://i.imgur.com/9XQxZ.png"
}

with tab5:

    q1 = st.radio("Motivation", ["Power", "Friendship", "Freedom", "Knowledge"])
    q2 = st.radio("Fight Style", ["Head on", "Strategic", "Support friends", "Adapt"])
    q3 = st.radio("Trait", ["Courage", "Intelligence", "Loyalty", "Calmness"])
    q4 = st.radio("Role", ["Leader", "Support", "Lone wolf", "Strategist"])
    q5 = st.radio("Weakness", ["Anger", "Trust issues", "Overconfidence", "Fear"])
    q6 = st.radio("Power Type", ["Physical strength", "Speed", "Magic/Skills", "Tactical mind"])
     
    if st.button("Result"):

    result = get_character_match(q1, q2, q3, q4, q5, q6).lower()
    img = CHAR_IMAGES.get(result, None)

    # FULL SCREEN CENTER CARD
    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown("""
        <style>
        .card {
            background: #0f172a;
            padding: 30px;
            border-radius: 20px;
            border: 2px solid #22c55e;
            text-align: center;
            box-shadow: 0 0 40px rgba(34,197,94,0.5);
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown("## 🎌 You are")
        st.markdown(f"# {result.title()}")

        # 🔥 THIS FIXES YOUR IMAGE ISSUE
        if img:
            st.image(img, use_container_width=True)
        else:
            st.warning("Image not found")

        st.markdown("</div>", unsafe_allow_html=True)
