import streamlit as st
import requests
import random
import streamlit.components.v1 as components

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
# FIREWORKS
# =========================
def firework():
    components.html("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
        let count = 5;
        let interval = setInterval(() => {
            confetti({
                particleCount: 120,
                spread: 100,
                origin: { y: 0.6 }
            });
            count--;
            if(count <= 0) clearInterval(interval);
        }, 500);
    </script>
    """, height=0)


# =========================
# WINNER UI (GLOW + FIREWORKS)
# =========================
def show_winner(name):
    st.markdown(f"""
    <div style="
        text-align:center;
        font-size:65px;
        font-weight:900;
        color:#ff2e2e;
        text-shadow:0px 0px 25px red, 0px 0px 60px darkred;
        margin-top:0px;
    ">
    🏆 WINNER!!
    </div>

    <div style="
        text-align:center;
        font-size:32px;
        color:white;
        font-weight:700;
        margin-top:-10px;
    ">
    {name}
    </div>
    """, unsafe_allow_html=True)

    firework()


# =========================
# QUOTES
# =========================
def generate_quote(theme):
    quotes = {
        "Motivational": [("Naruto","Never give up"),("Rock Lee","Hard work wins")],
        "Friendship": [("Luffy","I trust my crew")],
        "Success": [("Itachi","Sacrifice is power")],
        "Sad": [("Pain","Understand pain")],
        "Funny": [("Saitama","Ok.")]
    }
    return random.choice(quotes.get(theme, [("Anime","Stay strong")]))


# =========================
# PERSONA
# =========================
def get_character_match(q1,q2,q3,q4,q5,q6):

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

    for a in [q1,q2,q3,q4,q5,q6]:

        if a in ["Friendship","Support","Loyalty"]:
            score["Naruto Uzumaki"] += 2
            score["Luffy"] += 2
            score["Itachi Uchiha"] += 2

        if a == "Power":
            score["Goku"] += 3
            score["Saitama"] += 2

        if a == "Freedom":
            score["Luffy"] += 3
            score["Eren Yeager"] += 2

    return max(score, key=score.get)


# =========================
# HEADER
# =========================
st.title("🏆 AnimeVerse AI")
st.subheader("AI-Powered Anime Companion")

tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Anime Search",
    "⚔️ Battle",
    "✨ Quotes",
    "🎭 Quiz"
])


# =========================
# ANIME SEARCH (FIXED UI)
# =========================
with tab1:

    anime_name = st.text_input("Enter Anime Name")

    if st.button("Search"):

        r = requests.get(f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1").json()

        if r["data"]:

            a = r["data"][0]

            st.image(a["images"]["jpg"]["image_url"])

            st.markdown(f"## {a['title']}")

            col1,col2,col3 = st.columns(3)

            with col1:
                st.metric("⭐ Rating", a.get("score", "N/A"))
            with col2:
                st.metric("🎬 Episodes", a.get("episodes", "N/A"))
            with col3:
                st.metric("📅 Year", a.get("year", "N/A"))

            st.write("🎭 Genres:", ", ".join([g["name"] for g in a["genres"]]))

            st.write("📖", a["synopsis"])


# =========================
# BATTLE SYSTEM
# =========================
with tab2:

    mode = st.selectbox("Mode", ["1v1","2v2","4v4","Tournament"])

    # ---------- 1v1 ----------
    if mode == "1v1":

        a = st.text_input("A")
        b = st.text_input("B")

        if st.button("Fight"):

            result = battle_1v1(a,b)
            winner = result["winner"]

            show_winner(winner)

            st.markdown("## ⚔️ Stats")

            for stat in result["fighter_a"]["stats"]:
                col1,col2 = st.columns(2)

                with col1:
                    st.write(a)
                    st.progress(result["fighter_a"]["stats"][stat]/100)

                with col2:
                    st.write(b)
                    st.progress(result["fighter_b"]["stats"][stat]/100)

            st.markdown("## 🏅 Category Winners")

            for k,v in result["category_winners"].items():
                if v == winner:
                    st.markdown(f"🔥 🏅 **{k} → {v}**")
                else:
                    st.write(f"🏅 {k} → {v}")

            st.write(result["story"])


    # ---------- 2v2 ----------
    if mode == "2v2":

        a1 = st.text_input("A1")
        a2 = st.text_input("A2")
        b1 = st.text_input("B1")
        b2 = st.text_input("B2")

        if st.button("Fight"):

            result = battle_2v2([a1,a2],[b1,b2])

            show_winner(result["winner"])

            st.write(result["story"])


    # ---------- 4v4 ----------
    if mode == "4v4":

        t1 = st.text_area("Team A")
        t2 = st.text_area("Team B")

        if st.button("Fight"):

            result = battle_4v4(t1.split("\n"), t2.split("\n"))

            show_winner(result["winner"])

            st.write(result["story"])


    # ---------- TOURNAMENT ----------
    if mode == "Tournament":

        fighters = st.text_area("Fighters")

        if st.button("Start"):

            result = run_tournament(fighters.split("\n"))

            show_winner(result["champion"])

            st.write(result["rounds"])
            st.write(result["story"])


# =========================
# QUOTES
# =========================
with tab3:

    theme = st.selectbox("Theme", ["Motivational","Friendship","Success","Sad","Funny"])

    if st.button("Generate"):
        st.success(generate_quote(theme))


# =========================
# QUIZ
# =========================
with tab4:

    q1 = st.radio("Motivation", ["Power","Friendship","Freedom","Knowledge"])
    q2 = st.radio("Fight Style", ["Head on","Strategic","Support friends","Adapt"])
    q3 = st.radio("Trait", ["Courage","Intelligence","Loyalty","Calmness"])
    q4 = st.radio("Role", ["Leader","Support","Lone wolf","Strategist"])
    q5 = st.radio("Weakness", ["Anger","Trust issues","Overconfidence","Fear"])
    q6 = st.radio("Power Type", ["Physical strength","Speed","Magic/Skills","Tactical mind"])

    if st.button("Result"):
        st.success(get_character_match(q1,q2,q3,q4,q5,q6))
