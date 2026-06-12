import os
import streamlit as st
import requests
import random

TEXT = {
    "English": {
        "title": "🏆 AnimeVerse AI",
        "chat" : "Type message",
        "chat_hi": "👋 Hello! How can I help you?",
        "chat_genre": "🎯 Tell me a genre like Action, Romance, Fantasy",
        "chat_default": "🤖 I understand you. Ask about anime!",

        "search": "Search Anime",
        "enter": "Enter anime name",
        "send": "Send",
        "genre": "Choose Genre",
        "load": "Get Anime List",

        "rating": "⭐ Rating",
        "episodes": "🎬 Episodes",
        "synopsis": "📖 Synopsis",

        "start_battle": "Start Battle",
        "generate_quote": "Generate Quote",
        "result_btn": "Result",
        "next": "Next",
        "prev": "Previous",

        # QUIZ LABELS
        "motivation": "Motivation",
        "fight_style": "Fight Style",
        "trait": "Trait",
        "role": "Role",
        "weakness": "Weakness",
        "power_type": "Power Type",

        # OPTIONS
        "options_power": "Power",
        "options_friendship": "Friendship",
        "options_freedom": "Freedom",
        "options_knowledge": "Knowledge",

        "style_headon": "Head on",
"style_strategic": "Strategic",
"style_support": "Support friends",
"style_adapt": "Adapt",

"trait_courage": "Courage",
"trait_intelligence": "Intelligence",
"trait_loyalty": "Loyalty",
"trait_calmness": "Calmness",

"role_leader": "Leader",
"role_support": "Support",
"role_lonely": "Lone wolf",
"role_strategist": "Strategist",

"weak_anger": "Anger",
"weak_trust": "Trust issues",
"weak_overconfidence": "Overconfidence",
"weak_fear": "Fear",

"power_physical": "Physical strength",
"power_speed": "Speed",
"power_magic": "Magic/Skills",
"power_tactical": "Tactical mind",
        
        "back": "Back",
        "result_text": "You are:",
    },

    "Hindi": {
        "title": "🏆 एनीमे वर्स AI",
        "chat": "संदेश लिखें",
        "chat_hi": "👋 नमस्ते! मैं आपकी कैसे मदद कर सकता हूँ?",
        "chat_genre": "🎯 मुझे कोई genre बताइए",
        "chat_default": "🤖 मैं समझ गया!",

        "search": "एनीमे खोजें",
        "enter": "एनीमे नाम दर्ज करें",
        "send": "भेजें",
        "genre": "शैली चुनें",
        "load": "एनीमे दिखाएं",

        "rating": "⭐ रेटिंग",
        "episodes": "🎬 एपिसोड",
        "synopsis": "📖 कहानी",

        "start_battle": "युद्ध शुरू करें",
        "generate_quote": "उद्धरण बनाएं",
        "result_btn": "परिणाम",
        "next": "अगला",
        "prev": "पिछला",

        "motivation": "प्रेरणा",
        "fight_style": "लड़ाई शैली",
        "trait": "गुण",
        "role": "भूमिका",
        "weakness": "कमजोरी",
        "power_type": "शक्ति प्रकार",

        "options_power": "शक्ति",
        "options_friendship": "मित्रता",
        "options_freedom": "स्वतंत्रता",
        "options_knowledge": "ज्ञान",

        "style_headon": "सीधा हमला",
"style_strategic": "रणनीतिक",
"style_support": "साथियों का समर्थन",
"style_adapt": "अनुकूलन",

"trait_courage": "साहस",
"trait_intelligence": "बुद्धिमत्ता",
"trait_loyalty": "वफादारी",
"trait_calmness": "शांति",

"role_leader": "नेता",
"role_support": "सहायक",
"role_lonely": "अकेला",
"role_strategist": "रणनीतिकार",

"weak_anger": "गुस्सा",
"weak_trust": "भरोसे की समस्या",
"weak_overconfidence": "अतिआत्मविश्वास",
"weak_fear": "डर",

"power_physical": "शारीरिक शक्ति",
"power_speed": "गति",
"power_magic": "जादू/कौशल",
"power_tactical": "रणनीति",

        "back": "पीछे",
        "result_text": "आप हैं:",
    },

    "Telugu": {
        "title": "🏆 అనిమే వర్స్ AI",
        "chat": "సందేశం టైప్ చేయండి",
        "chat_hi": "👋 హలో! నేను ఎలా సహాయం చేయగలను?",
        "chat_genre": "🎯 జానర్ చెప్పండి",
        "chat_default": "🤖 నేను అర్థం చేసుకున్నాను!",

        "search": "అనిమే వెతకండి",
        "enter": "అనిమే పేరు నమోదు చేయండి",
        "send": "పంపండి",
        "genre": "జానర్ ఎంచుకోండి",
        "load": "అనిమే చూపించు",

        "rating": "⭐ రేటింగ్",
        "episodes": "🎬 ఎపిసోడ్‌లు",
        "synopsis": "📖 కథ",

        "start_battle": "యుద్ధం ప్రారంభించు",
        "generate_quote": "కోట్ సృష్టించు",
        "result_btn": "ఫలితం",
        "next": "తరువాత",
        "prev": "మునుపటి",

        "motivation": "ప్రేరణ",
        "fight_style": "పోరాట శైలి",
        "trait": "లక్షణం",
        "role": "పాత్ర",
        "weakness": "బలహీనత",
        "power_type": "శక్తి రకం",

        "options_power": "శక్తి",
        "options_friendship": "స్నేహం",
        "options_freedom": "స్వేచ్ఛ",
        "options_knowledge": "జ్ఞానం",

        "style_headon": "నేరుగా పోరాటం",
"style_strategic": "వ్యూహాత్మక",
"style_support": "మిత్రులకు మద్దతు",
"style_adapt": "అనుగుణం",

"trait_courage": "ధైర్యం",
"trait_intelligence": "మేధస్సు",
"trait_loyalty": "నిబద్ధత",
"trait_calmness": "శాంతం",

"role_leader": "నాయకుడు",
"role_support": "మద్దతు",
"role_lonely": "ఒంటరి",
"role_strategist": "వ్యూహకర్త",

"weak_anger": "కోపం",
"weak_trust": "నమ్మకం సమస్యలు",
"weak_overconfidence": "అతివిశ్వాసం",
"weak_fear": "భయం",

"power_physical": "శారీరక శక్తి",
"power_speed": "వేగం",
"power_magic": "మాయ/నైపుణ్యం",
"power_tactical": "వ్యూహం",

        "back": "వెనుక",
        "result_text": "మీరు:",
    },

    "Japanese": {
        "title": "🏆 アニメバースAI",
        "chat": "メッセージ入力",
        "chat_hi": "👋 こんにちは！",
        "chat_genre": "🎯 ジャンルを教えてください",
        "chat_default": "🤖 理解しました！",

        "search": "検索",
        "enter": "アニメ名入力",
        "send": "送信",
        "genre": "ジャンル選択",
        "load": "表示",

        "rating": "⭐ 評価",
        "episodes": "🎬 話数",
        "synopsis": "📖 あらすじ",

        "start_battle": "バトル開始",
        "generate_quote": "名言生成",
        "result_btn": "結果",
        "next": "次へ",
        "prev": "前へ",

        "motivation": "動機",
        "fight_style": "戦闘スタイル",
        "trait": "特性",
        "role": "役割",
        "weakness": "弱点",
        "power_type": "能力タイプ",

        "options_power": "力",
        "options_friendship": "友情",
        "options_freedom": "自由",
        "options_knowledge": "知識",

        "style_headon": "正面攻撃",
"style_strategic": "戦略的",
"style_support": "仲間をサポート",
"style_adapt": "適応",

"trait_courage": "勇気",
"trait_intelligence": "知性",
"trait_loyalty": "忠誠",
"trait_calmness": "冷静",

"role_leader": "リーダー",
"role_support": "サポート",
"role_lonely": "一匹狼",
"role_strategist": "戦略家",

"weak_anger": "怒り",
"weak_trust": "不信感",
"weak_overconfidence": "過信",
"weak_fear": "恐怖",

"power_physical": "身体能力",
"power_speed": "スピード",
"power_magic": "魔法/スキル",
"power_tactical": "戦術思考",

        "back": "戻る",
        "result_text": "あなたは:",
    }
}

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

        
st.set_page_config(
    page_title="AnimeVerse AI",
    page_icon="⚔️",
    layout="wide"
)
if "lang" not in st.session_state:
    st.session_state.lang = "English"

col1, col2 = st.columns([8,2])

with col2:
    st.session_state.lang = st.selectbox(
        "🌐 Language",
        ["English", "Hindi", "Telugu", "Japanese"]
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
st.title(TEXT[st.session_state.lang]["title"])
st.subheader({
    "English": "AI-Powered Anime Battle Simulator",
    "Hindi": "AI आधारित एनीमे बैटल सिस्टम",
    "Telugu": "AI ఆధారిత అనిమే బ్యాటిల్ సిస్టమ్",
    "Japanese": "AIアニメバトルシステム"
}[st.session_state.lang])
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    {
        "English": "🔍 Anime Search",
        "Hindi": "🔍 एनीमे खोज",
        "Telugu": "🔍 అనిమే సెర్చ్",
        "Japanese": "🔍 アニメ検索"
    }[st.session_state.lang],

    {
        "English": "🤖 AI Anime Recommender",
        "Hindi": "🤖 AI एनिमे सुझाव",
        "Telugu": "🤖 AI అనిమే సిఫార్సు",
        "Japanese": "🤖 AIアニメ推薦"
    }[st.session_state.lang],

    {
        "English": "⚔️ Battle Simulator",
        "Hindi": "⚔️ युद्ध सिमुलेटर",
        "Telugu": "⚔️ బ్యాటిల్ సిమ్యులేటర్",
        "Japanese": "⚔️ バトルシミュレーター"
    }[st.session_state.lang],

    {
        "English": "✨ Quote Generator",
        "Hindi": "✨ उद्धरण जनरेटर",
        "Telugu": "✨ కోట్ జనరేటర్",
        "Japanese": "✨ 名言ジェネレーター"
    }[st.session_state.lang],

    {
        "English": "🎭 Personality Quiz",
        "Hindi": "🎭 व्यक्तित्व प्रश्नोत्तरी",
        "Telugu": "🎭 వ్యక్తిత్వ క్విజ్",
        "Japanese": "🎭 性格診断"
    }[st.session_state.lang]
])

lang = st.session_state.lang
with tab1:
    st.header(TEXT[lang]["search"])
    name = st.text_input(TEXT[lang]["enter"])

    if st.button(TEXT[lang]["search"]) and name:

        url = f"https://api.jikan.moe/v4/anime?q={name}&limit=1"

        try:
            res = requests.get(url).json()
            data = res.get("data", [])

            if data:
                anime = data[0]

                st.success(anime["title"])
                st.image(anime["images"]["jpg"]["image_url"])   # ✅ THIS IS CORRECT PLACE
                st.write(TEXT[lang]["rating"], anime.get("score", "N/A"))
                st.write(TEXT[lang]["episodes"], anime.get("episodes", "N/A"))
                st.write(TEXT[lang]["synopsis"], anime.get("synopsis", "N/A"))
            else:
                st.error({"English": "No anime found", "Hindi": "कोई एनीमे नहीं मिला", "Telugu": "ఏ అనిమే కనబడలేదు", "Japanese": "アニメが見つかりません"}[lang])

        except:
            st.error("Failed to fetch anime data.")

lang = st.session_state.lang
with tab2:

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
            return TEXT[lang]["chat_hi"]

        if "genre" in msg:
            st.session_state.step = "genre_input"
            return TEXT[lang]["chat_genre"]

        return TEXT[lang]["chat_default"]

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
    user_input = st.text_input(TEXT[lang]["chat"], placeholder=TEXT[lang]["chat"], key="chat_input")

    if st.button(TEXT[lang]["send"]) and user_input:

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

        genre = st.text_input(TEXT[lang]["genre"] + " (Action, Romance, Fantasy...)")

        if st.button(TEXT[lang]["load"]) and genre:

            gid = GENRES.get(genre.lower())

            if not gid:
                st.error({"English": "Invalid genre", "Hindi": "अमान्य जॉनर", "Telugu": "చెల్లని జానర్", "Japanese": "無効なジャンル"}[lang])
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
                if st.button(TEXT[lang]["prev"]):
                    st.session_state.page -= 1
                    st.rerun()
        with c2:
            st.markdown(f"📄 Page {st.session_state.page} / {TOTAL_PAGES}")
        with c3:
            if st.session_state.page < TOTAL_PAGES:
                if st.button(TEXT[lang]["next"]):
                    st.session_state.page += 1
                    st.rerun()
    # =========================
    # ANIME DETAILS PAGE
    # =========================
    if st.session_state.step == "details":

        a = st.session_state.selected_anime

        st.markdown({"English": "## 🎬 Anime Details", "Hindi": "## 🎬 एनीमे विवरण", "Telugu": "## 🎬 అనిమే వివరాలు", "Japanese": "## 🎬 アニメ詳細"}[lang])

        st.image(a["images"]["jpg"]["image_url"], width=250)

        st.write("⭐ Score:", a.get("score"))
        st.write("🎬 Episodes:", a.get("episodes"))
        st.write("📖 Synopsis:", a.get("synopsis"))

        if st.button(TEXT[lang]["back"]):
            st.session_state.step = "show_anime"
            st.rerun()
# =========================
# ⚔️ BATTLE SYSTEM (FIXED UI)
# =========================
with tab3:

    mode = st.selectbox({
    "English": "Select Mode",
    "Hindi": "मोड चुनें",
    "Telugu": "మోడ్ ఎంచుకోండి",
    "Japanese": "モード選択"
}[lang],
        ["1v1 Battle", "2v2 Battle", "4v4 Battle", "Tournament Arc", "Survival Arena"]
    )

    # ---------------- 1v1 ----------------
    if mode == "1v1 Battle":

        a = st.text_input("Character A")
        b = st.text_input("Character B")

        if st.button(TEXT[lang]["start_battle"]) and a and b:

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
    # ================= 2v2 =================
    elif mode == "2v2 Battle":
        a1 = st.text_input("Player-1")
        a2 = st.text_input("Player-2")
        b1 = st.text_input("Player-3")
        b2 = st.text_input("Player-4")
        if st.button(TEXT[lang]["start_battle"]) and all([a1, a2, b1, b2]):
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
       
    # ---------------- 4v4 ----------------
    elif mode == "4v4 Battle":
        t1 = st.text_area("Phantum Troupe")
        t2 = st.text_area("Oración Seis")
        if st.button(TEXT[lang]["start_battle"]) and t1 and t2:
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
    # ---------------- TOURNAMENT ----------------
    elif mode == "Tournament Arc":

        fighters = st.text_area("Enter fighters")

        if st.button(TEXT[lang]["start_battle"]) and fighters:

            result = run_tournament(fighters.split("\n"))

            st.success("👑 " + result["champion"])
            st.info(result["story"])

    # ---------------- SURVIVAL ----------------
    elif mode == "Survival Arena":

        hero = st.text_input("Hero")
        if st.button(TEXT[lang]["start_battle"]) and hero:
            result = survival_mode(hero)
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.markdown("## 🎌 You are")
                st.success(result["character"])
                char_key = result["character"].lower()
                st.image(CHAR_IMAGES.get(char_key, "https://i.imgur.com/default.png") if isinstance(CHAR_IMAGES, dict) else "https://i.imgur.com/default.png")
            st.markdown("## ⭐ Score")
            st.write(result["score"])
            st.markdown("## 📖 Story")
            st.info(result["story"])

# =========================
# ✨ QUOTES
# =========================
with tab4:

    theme = st.selectbox({
    "English": "Theme",
    "Hindi": "विषय",
    "Telugu": "థీమ్",
    "Japanese": "テーマ"
}[lang], ["Motivational", "Friendship", "Success", "Sad", "Funny"])

    if st.button(TEXT[lang]["generate_quote"]):
        st.success(generate_quote(theme))

# =========================
# 🎭 QUIZ
# =========================
with tab5:

    t = TEXT[st.session_state.lang]

    q1 = st.radio(t["motivation"], [
        t["options_power"],
        t["options_friendship"],
        t["options_freedom"],
        t["options_knowledge"]
    ])

    q2 = st.radio(t["fight_style"], [
        t["style_headon"],
        t["style_strategic"],
        t["style_support"],
        t["style_adapt"]
    ])

    q3 = st.radio(t["trait"], [
        t["trait_courage"],
        t["trait_intelligence"],
        t["trait_loyalty"],
        t["trait_calmness"]
    ])

    q4 = st.radio(t["role"], [
        t["role_leader"],
        t["role_support"],
        t["role_lonely"],
        t["role_strategist"]
    ])

    q5 = st.radio(t["weakness"], [
        t["weak_anger"],
        t["weak_trust"],
        t["weak_overconfidence"],
        t["weak_fear"]
    ])

    q6 = st.radio(t["power_type"], [
        t["power_physical"],
        t["power_speed"],
        t["power_magic"],
        t["power_tactical"]
    ])

    if st.button(t["result"]):
        result = get_character_match(q1, q2, q3, q4, q5, q6)
        st.success(t["result"] + " " + result)
