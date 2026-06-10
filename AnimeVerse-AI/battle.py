from gemini_utils import get_gemini_response


# =========================
# 🥊 1v1 BATTLE SYSTEM
# =========================
def battle_1v1(char1, char2):

    try:
        prompt = f"""
You are an expert anime battle analyst.

Simulate a cinematic 1v1 battle between {char1} and {char2}.

FORMAT OUTPUT EXACTLY LIKE THIS:

💪 POWER ANALYSIS
- Raw Power (0-100)
- Speed (0-100)
- Intelligence (0-100)
- Battle IQ (0-100)
- Durability (0-100)
- Stamina (0-100)
- Special Powers (0-100)

📊 DETAILED COMPARISON
Compare both fighters in:
Strength, Speed, Intelligence, Battle IQ, Durability, Stamina, Special Powers, Combat Skills, Experience

🌟 SIGNATURE ABILITIES
List abilities for both fighters

🏆 FINAL VERDICT
- Winner
- Battle Score (each fighter)
- MVP Ability
- Winning Factor
- Difficulty (Easy / Medium / Hard / Extreme)

📖 BATTLE STORY
Write cinematic anime-style fight story with actions, emotions, and abilities.
"""

        return get_gemini_response(prompt)

    except Exception:
        return f"""
🏆 WINNER: {char1}

Battle Score:
{char1}: 950
{char2}: 870

MVP Ability:
Ultimate Technique

Winning Factor:
Superior Combat Skill

📖 STORY:
A fierce battle between {char1} and {char2} ends with {char1} emerging victorious.
"""


# =========================
# 👥 2v2 BATTLE SYSTEM
# =========================
def battle_2v2(team1, team2):

    try:
        prompt = f"""
Simulate a cinematic 2v2 anime team battle.

Team A: {team1}
Team B: {team2}

FORMAT:

📊 TEAM ANALYSIS
- Attack Power
- Defense
- Strategy
- Synergy
- Special Abilities

🏆 FINAL RESULT
- Winning Team
- MVP Fighter
- Best Combo
- Winning Factor

📖 BATTLE STORY
Cinematic anime fight narration
"""

        return get_gemini_response(prompt)

    except Exception:
        return f"""
🏆 WINNER: Team A

MVP: Gojo

Best Combo:
Gojo + Sukuna

Winning Factor:
Superior coordination and teamwork
"""


# =========================
# ⚔️ 4v4 BATTLE SYSTEM
# =========================
def battle_4v4(team1, team2):

    try:
        prompt = f"""
Simulate an epic 4v4 anime battle.

Team A: {team1}
Team B: {team2}

FORMAT:

📊 TEAM STATS
- Power
- Strategy
- Coordination
- Synergy

🏆 RESULT
- Winner
- MVP Fighter
- Battle Highlights
- Winning Factor

📖 CINEMATIC STORY
Epic anime battle narration with transformations and final clash.
"""

        return get_gemini_response(prompt)

    except Exception:
        return f"""
🏆 WINNER: Team A

MVP: Gojo Satoru

Battle Highlight:
Dominated the battlefield with overwhelming power and strategy
"""


# =========================
# 🏆 TOURNAMENT MODE
# =========================
def run_tournament(characters):

    try:
        prompt = f"""
Run a full anime tournament.

Participants:
{characters}

FORMAT:

🥊 Quarter Finals
🥊 Semi Finals
🥊 Grand Final

🏆 CHAMPION
🏅 TOURNAMENT MVP
🔥 MOST INTENSE MATCH

📜 HALL OF FAME
List top performers

📊 TOURNAMENT SUMMARY
Brief analytics
"""

        return get_gemini_response(prompt)

    except Exception:
        return f"""
🏆 CHAMPION: Gojo Satoru

🔥 MVP: Gojo

Most Intense Match:
Gojo vs Madara

Hall of Fame:
Gojo, Madara, Naruto
"""


# =========================
# 🔥 SURVIVAL MODE
# =========================
def survival_mode(character):

    try:
        prompt = f"""
Run survival arena mode for {character}.

FORMAT:

🔥 ROUNDS
Round 1
Round 2
Round 3

⚔️ OPPONENTS
List enemies faced

📊 RESULTS
Wins / Losses

🏆 FINAL STATS
- XP Earned
- Survival Score
- Arena Rank
- Achievement

📖 STORY
Cinematic survival journey narration
"""

        return get_gemini_response(prompt)

    except Exception:
        return f"""
🔥 SURVIVAL REPORT

Character: {character}

Rounds Cleared: 5
XP Earned: 4500
Survival Score: 87%
Rank: S-TIER
Achievement: KING OF THE ARENA
"""
