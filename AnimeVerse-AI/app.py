import streamlit as st
import random 
import requests

# =========================
# TEMP BACKEND FUNCTIONS
# =========================

def battle_1v1(a, b):
    winner = random.choice([a, b])
    return {
        "winner": winner,
        "battle_score": random.randint(80, 100),
        "difficulty": random.choice(["Easy", "Medium", "Hard"]),
        "win_probability": f"{random.randint(50,95)}%",
        "story": f"{a} and {b} fought an epic battle. {winner} emerged victorious."
    }

def battle_2v2(team_a, team_b):
    winner = random.choice(["Team A", "Team B"])
    return {
        "winner": winner,
        "story": f"{', '.join(team_a)} fought {', '.join(team_b)}. {winner} won."
    }

def battle_4v4(team_a, team_b):
    winner = random.choice(["Team Alpha", "Team Omega"])
    return {
        "winner": winner,
        "story": f"{winner} dominated the battlefield after a fierce 4v4 battle."
    }

def run_tournament(fighters):
    champion = random.choice(fighters)
    return {
        "champion": champion,
        "story": f"{champion} defeated all opponents and became the tournament champion."
    }

def survival_mode(hero):
    return {
        "result": f"{hero} survived the arena!",
        "score": random.randint(100, 1000)
    }

def generate_quote(theme):
    quotes = {
        "Motivational": [
            "Never give up until the very end.",
            "Power comes from perseverance.",
            "A true hero keeps moving forward."
        ],
        "Friendship": [
            "Friends are the family we choose.",
            "Together we are stronger.",
            "Trust is the strongest bond."
        ],
        "Success": [
            "Hard work surpasses talent.",
            "Every step counts toward victory.",
            "Success begins with determination."
        ],
        "Sad": [
            "Even pain helps us grow.",
            "Every scar tells a story.",
            "Darkness makes the stars shine brighter."
        ],
        "Funny": [
            "A hero needs snacks too!",
            "Training can wait, lunch cannot.",
            "Even legends forget their homework."
        ]
    }

    return random.choice(quotes[theme])

def get_character_match(q1, q2):

    if q1 == "Friendship":
        return "Naruto Uzumaki"
    elif q1 == "Freedom":
        return "Monkey D. Luffy"
    elif q1 == "Knowledge":
        return "Itachi Uchiha"
    elif q2 == "Strategic":
        return "Levi Ackerman"
    
    return "Gojo Satoru"

# =========================
# APP CONFIG
# =========================

st.set_page_config(
    page_title="AnimeVerse AI",
    page_icon="⚔️",
    layout="wide"
)

# =========================
# LOAD CSS
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
st.subheader("AI-Powered Anime Companion")

# =========================
# TABS (AI RECOMMENDER REMOVED)
# =========================

tab1, tab3, tab4, tab5 = st.tabs([
    "🔍 Anime Search",
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

        if anime_name:

            try:
                url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()

                    if data["data"]:
                        anime = data["data"][0]

                        st.success(f"Results for {anime['title']}")
                        st.image(anime["images"]["jpg"]["image_url"], width=300)

                        st.write(f"⭐ Rating: {anime['score']}")
                        st.write(f"🎬 Episodes: {anime['episodes']}")

                        genres = ", ".join(g["name"] for g in anime["genres"])
                        st.write(f"🎭 Genres: {genres}")

                        if anime["year"]:
                            st.write(f"📅 Release Year: {anime['year']}")

                        st.write(f"📖 Synopsis: {anime['synopsis']}")

                    else:
                        st.error("Anime not found.")
                else:
                    st.error("Failed to fetch anime data.")

            except Exception as e:
                st.error(f"Error: {e}")

        else:
            st.error("Please enter an anime name.")

# =========================
# TAB 2 - BATTLE SIMULATOR
# =========================

with tab3:

    st.header("⚔️ Anime Battle Simulator")

    mode = st.selectbox(
        "Select Mode",
        [
            "1v1 Battle",
            "2v2 Battle",
            "4v4 Battle",
            "Tournament Arc",
            "Survival Arena"
        ]
    )

    # =========================
    # ⚔️ 1v1 BATTLE (UPGRADED UI)
    # =========================
    if mode == "1v1 Battle":

        a = st.text_input("Character A")
        b = st.text_input("Character B")

        if st.button("Start Battle"):

            if a and b:

                result = battle_1v1(a, b)

                st.success(f"🏆 Winner: {result['winner']}")

                st.markdown("## ⚔️ Combat Analysis")

                # Fighters stats
                fa = result["fighter_a"]["stats"]
                fb = result["fighter_b"]["stats"]

                stats_keys = list(fa.keys())

                for stat in stats_keys:

                    col1, col2 = st.columns(2)

                    with col1:
                        st.write(f"🔥 {a} - {stat}")
                        st.progress(fa[stat] / 100)

                    with col2:
                        st.write(f"⚡ {b} - {stat}")
                        st.progress(fb[stat] / 100)

                # =========================
                # 🏅 CATEGORY WINNERS
                # =========================
                st.markdown("## 🏅 Category Winners")

                for k, v in result["category_winners"].items():
                    st.write(f"⚔️ **{k} → 🥇 {v}**")

                # =========================
                # 📖 STORY
                # =========================
                st.markdown("## 📖 Battle Story")
                st.write(result["story"])

            else:
                st.error("Enter both characters.")

    # =========================
    # 👥 2v2 BATTLE
    # =========================
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
                st.error("Fill all fields.")

    # =========================
    # ⚔️ 4v4 BATTLE
    # =========================
    elif mode == "4v4 Battle":

        t1 = st.text_area("Team Alpha (4 names)")
        t2 = st.text_area("Team Omega (4 names)")

        if st.button("Start 4v4 Battle"):

            if t1 and t2:

                team_a = t1.split("\n")
                team_b = t2.split("\n")

                result = battle_4v4(team_a, team_b)

                st.success(f"🏆 Winner: {result['winner']}")
                st.write(result["story"])

            else:
                st.error("Enter both teams.")

    # =========================
    # 🏆 TOURNAMENT
    # =========================
    elif mode == "Tournament Arc":

        fighters = st.text_area("Enter fighters (one per line)")

        if st.button("Start Tournament"):

            if fighters:

                result = run_tournament(fighters.split("\n"))

                st.success(f"👑 Champion: {result['champion']}")
                st.write(result["story"])

            else:
                st.error("Enter fighters.")

    # =========================
    # 🔥 SURVIVAL
    # =========================
    elif mode == "Survival Arena":

        hero = st.text_input("Select Hero")

        if st.button("Enter Arena"):

            if hero:

                result = survival_mode(hero)

                st.success(result["result"])
                st.write(f"⭐ Score: {result['score']}")

            else:
                st.error("Enter hero name.")

# =========================
# TAB 3 - QUOTE GENERATOR
# =========================

with tab4:

    st.header("✨ Anime Quote Generator")

    theme = st.selectbox(
        "Theme",
        ["Motivational", "Friendship", "Success", "Sad", "Funny"]
    )

    if st.button("Generate Quote"):
        quote = generate_quote(theme)
        st.success(quote)

# =========================
# TAB 4 - PERSONALITY QUIZ
# =========================

with tab5:

    st.header("🎭 Personality Quiz")

    q1 = st.radio("What motivates you?", ["Power", "Friendship", "Freedom", "Knowledge"])
    q2 = st.radio("How do you fight?", ["Head on", "Strategic", "Support friends", "Adapt"])

    if st.button("Reveal Result"):
        character = get_character_match(q1, q2)
        st.success(f"🎌 Your Anime Match: {character}")
