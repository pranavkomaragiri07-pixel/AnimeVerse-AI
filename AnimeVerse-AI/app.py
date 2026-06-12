import os
import streamlit as st
import requests
import random
def local_ai_predict(team_a, team_b):
    a_score = sum(len(str(x)) for x in team_a)
    b_score = sum(len(str(x)) for x in team_b)

    if a_score > b_score:
        return "Team A has better synergy and control."
    elif b_score > a_score:
        return "Team B has stronger coordination and power."
    else:
        return "Both teams are evenly matched."

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
def local_ai_predict(team_a, team_b):
    a_score = sum(len(str(x)) for x in team_a)
    b_score = sum(len(str(x)) for x in team_b)

    if a_score > b_score:
        return "Team A has better synergy and control."
    elif b_score > a_score:
        return "Team B has stronger coordination and power."
    else:
        return "Both teams are evenly matched."
        
st.set_page_config(
    page_title="AnimeVerse AI",
    page_icon="⚔️",
    layout="wide"
)
st.markdown("""
<style>

/* FULL PAGE CENTER FIX */
[data-testid="stAppViewContainer"] {
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* CENTER MAIN CONTENT */
.main {
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* RESULT CARD CENTER FIX */
div.stSuccess {
    display: flex;
    justify-content: center;
}

/* IMAGE CENTER FIX */
img {
    display: block;
    margin-left: auto;
    margin-right: auto;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.title("🏆 AnimeVerse AI")
st.subheader("AI-Powered Anime Battle Simulator")
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔍 Anime Search",
    "🤖 AI Anime Recommender",
    "⚔️ Battle Simulator",
    "✨ Quote Generator",
    "🎭 Personality Quiz"
])
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

                st.success(anime["title"])
                st.image(anime["images"]["jpg"]["image_url"])   # ✅ THIS IS CORRECT PLACE
                st.write("⭐ Rating:", anime.get("score"))
                st.write("🎬 Episodes:", anime.get("episodes"))
                st.write("📖 Synopsis:", anime.get("synopsis"))
            else:
                st.error("No anime found.")

        except:
            st.error("Failed to fetch anime data.")


with tab2:

    st.title("🤖 AI Anime Recommender System")

    # =========================
    # SESSION STATE INIT
    # =========================
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "step" not in st.session_state:
        st.session_state.step = "chat"

    if "genre" not in st.session_state:
        st.session_state.genre = None

    if "anime_list" not in st.session_state:
        st.session_state.anime_list = []

    if "page" not in st.session_state:
        st.session_state.page = 1

    if "selected_anime" not in st.session_state:
        st.session_state.selected_anime = None

    # =========================
    # AI BRAIN
    # =========================
    def ai_response(msg):

        msg = msg.lower()

        if "hello" in msg or "hi" in msg:
            return "👋 Hello! Say 'genre' and I will suggest anime categories."

        if "genre" in msg:
            st.session_state.step = "genre_input"
            return "🎯 Choose a genre: Action, Adventure, Comedy, Drama, Fantasy, Horror, Romance, Sci-Fi"

        return "🤖 I can help! Try saying 'genre' or 'suggest anime'"

    # =========================
    # CHAT DISPLAY
    # =========================
    for role, text in st.session_state.messages:
        if role == "user":
            st.markdown(f"🧑 You: {text}")
        else:
            st.markdown(f"🤖 AI: {text}")

    # =========================
    # CHAT INPUT (ALWAYS ACTIVE)
    # =========================
    user_input = st.text_input("Talk to AI", key="chat_input")

    if st.button("Send") and user_input:

        st.session_state.messages.append(("user", user_input))
        reply = ai_response(user_input)
        st.session_state.messages.append(("ai", reply))
        st.rerun()

    # =========================
    # GENRE MAP
    # =========================
    GENRES = {
        "action": 1,
        "adventure": 2,
        "comedy": 4,
        "drama": 8,
        "fantasy": 10,
        "horror": 14,
        "romance": 22,
        "sci-fi": 24
    }

    # =========================
    # GENRE INPUT BAR (DYNAMIC)
    # =========================
    if st.session_state.step == "genre_input":

        genre = st.text_input("Enter Genre (Action, Romance, Fantasy...)")

        if st.button("Load Anime") and genre:

            gid = GENRES.get(genre.lower())

            if not gid:
                st.error("Invalid genre")
            else:

                all_anime = []
                seen = set()

                # 100 anime (4 pages × 25)
                for page in range(1, 5):

                    url = f"https://api.jikan.moe/v4/anime?genres={gid}&limit=25&page={page}"
                    res = requests.get(url).json()

                    for a in res.get("data", []):
                        if a["mal_id"] not in seen:
                            seen.add(a["mal_id"])
                            all_anime.append(a)

                st.session_state.anime_list = all_anime
                st.session_state.step = "show_anime"
                st.session_state.page = 1
                st.rerun()

    # =========================
    # SHOW ANIME GRID (PAGINATION)
    # =========================
    if st.session_state.step == "show_anime":

        per_page = 25
        start = (st.session_state.page - 1) * per_page
        end = start + per_page

        page_data = st.session_state.anime_list[start:end]

        st.markdown("## 📺 Anime List")

        cols = st.columns(5)

        for i, anime in enumerate(page_data):

            with cols[i % 5]:

                st.image(anime["images"]["jpg"]["image_url"], width=150)

                if st.button(anime["title"], key=anime["mal_id"]):
                    st.session_state.selected_anime = anime
                    st.session_state.step = "details"
                    st.rerun()

        #pagination
        TOTAL_PAGES = 4
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.session_state.page > 1:
                if st.button("⬅ Prev"):
                    st.session_state.page -= 1
                    st.rerun()
        with c2:
            st.markdown(f"📄 Page {st.session_state.page} / {TOTAL_PAGES}")
        with c3:
            if st.session_state.page < TOTAL_PAGES:
                if st.button("Next ➡"):
                    st.session_state.page += 1
                    st.rerun()
    # =========================
    # ANIME DETAILS PAGE
    # =========================
    if st.session_state.step == "details":

        a = st.session_state.selected_anime

        st.markdown("## 🎬 Anime Details")

        st.image(a["images"]["jpg"]["image_url"], width=250)

        st.write("⭐ Score:", a.get("score"))
        st.write("🎬 Episodes:", a.get("episodes"))
        st.write("📖 Synopsis:", a.get("synopsis"))

        if st.button("⬅ Back"):
            st.session_state.step = "show_anime"
            st.rerun()
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
            st.markdown("## 🤖 AI ANALYSIS")
            if st.button("Predict with AI"):
                st.info(ai_analyze_battle(a, b))

    # ================= 2v2 =================
    elif mode == "2v2 Battle":
        a1 = st.text_input("Player-1")
        a2 = st.text_input("Player-2")
        b1 = st.text_input("Player-3")
        b2 = st.text_input("Player-4")
        if st.button("Fight") and all([a1, a2, b1, b2]):
            result = battle_2v2([a1, a2], [b1, b2])
            st.success(f"🏆 Winner: {result['winner']}")
            team_a = result["team_a_total"]
            team_b = result["team_b_total"]
            st.markdown("## ⚔️ TEAM STATS COMPARISON")
            colA, colVS, colB = st.columns([4, 1, 4])
            with colA:
                st.markdown("### 🔵 TEAM A")
            with colVS:
                st.markdown("### VS")
            with colB:
                st.markdown("### 🔴 TEAM B")
            for stat in team_a.keys():
                colA, colVS, colB = st.columns([4, 1, 4])
                with colA:
                    st.write(stat)
                    st.progress(team_a[stat] / 100)
                with colB:
                    st.write(stat)
                    st.progress(team_b[stat] / 100)
            st.markdown("## 🏅 Category Winners")
            for k, v in result["category_winners"].items():
                st.write(f"🏅 {k} → {v}")
            st.markdown("## 📖 Story")
            st.info(result["story"])
            st.markdown("## 🤖 AI Analysis")
            st.success(local_ai_predict([a1, a2], [b1, b2]))
       
    # ---------------- 4v4 ----------------
    elif mode == "4v4 Battle":
        t1 = st.text_area("Phantum Troupe")
        t2 = st.text_area("Oración Seis")
        if st.button("Battle") and t1 and t2:
            team_a_list = t1.split("\n")
            team_b_list = t2.split("\n")
            result = battle_4v4(team_a_list, team_b_list)
            st.success(f"🏆 Winner: {result['winner']}")
            team_a = result["team_a_total"]
            team_b = result["team_b_total"]
            st.markdown("## ⚔️ TEAM STATS COMPARISON")
            colA, colVS, colB = st.columns([4, 1, 4])
            with colA:
                st.markdown("### 🔵 TEAM A TOTAL STATS")
            with colB:
                st.markdown("### 🔴 TEAM B TOTAL STATS")
            for stat in team_a.keys():
                colA, colVS, colB = st.columns([4, 1, 4])
                with colA:
                    st.write(stat)
                    st.progress(team_a[stat] / 100)
                with colB:
                    st.write(stat)
                    st.progress(team_b[stat] / 100)
            st.markdown("## 🏅 Category Winners")
            for k, v in result["category_winners"].items():
                st.write(f"🏅 {k} → {v}")
            st.markdown("## 📖 Story")
            st.info(result["story"])
            st.markdown("## 🤖 AI Analysis")
            st.success(local_ai_predict(team_a_list, team_b_list))
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
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.markdown("## 🎌 You are")
                st.success(result["character"])
                char_key = result["character"].lower()
                st.image(CHAR_IMAGES.get(char_key, "https://i.imgur.com/default.png"),use_container_width=True)
            st.markdown("## ⭐ Score")
            st.write(result["score"])
            st.markdown("## 📖 Story")
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
