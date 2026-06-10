from gemini_utils import get_gemini_response
import random


# =========================
# 🎯 STAT GENERATOR (FALLBACK CORE)
# =========================
def generate_stats(name):
    return {
        "Raw Power": random.randint(70, 100),
        "Speed": random.randint(70, 100),
        "Battle IQ": random.randint(70, 100),
        "Durability": random.randint(70, 100),
        "Special Ability": random.randint(70, 100),
        "Experience": random.randint(70, 100),
        "Stamina": random.randint(70, 100),
        "Weapon Mastery": random.randint(70, 100)
    }


# =========================
# ⚔️ 1v1 BATTLE (UPGRADED)
# =========================
def battle_1v1(char1, char2):

    try:
        stats1 = generate_stats(char1)
        stats2 = generate_stats(char2)

        # category winners
        category_winners = {}

        score1 = 0
        score2 = 0

        for key in stats1:
            if stats1[key] > stats2[key]:
                category_winners[key] = char1
                score1 += 1
            else:
                category_winners[key] = char2
                score2 += 1

        winner = char1 if score1 > score2 else char2

        prompt = f"""
Create a cinematic anime battle story between {char1} and {char2}
based on their strengths and weaknesses.

Winner: {winner}
"""

        story = get_gemini_response(prompt)

        return {
            "fighter_a": {
                "name": char1,
                "stats": stats1
            },
            "fighter_b": {
                "name": char2,
                "stats": stats2
            },
            "category_winners": category_winners,
            "winner": winner,
            "story": story
        }

    except Exception:

        return {
            "fighter_a": {"name": char1, "stats": generate_stats(char1)},
            "fighter_b": {"name": char2, "stats": generate_stats(char2)},
            "category_winners": {},
            "winner": random.choice([char1, char2]),
            "story": f"{char1} and {char2} fought an intense battle."
        }


# =========================
# 👥 2v2 BATTLE
# =========================
def battle_2v2(team1, team2):

    t1_score = random.randint(70, 100)
    t2_score = random.randint(70, 100)

    winner = "Team A" if t1_score > t2_score else "Team B"

    return {
        "team_a_score": t1_score,
        "team_b_score": t2_score,
        "winner": winner,
        "story": f"{'Team A' if winner=='Team A' else 'Team B'} dominated the battlefield."
    }


# =========================
# ⚔️ 4v4 BATTLE
# =========================
def battle_4v4(team1, team2):

    t1 = sum(generate_stats(p)["Raw Power"] for p in team1)
    t2 = sum(generate_stats(p)["Raw Power"] for p in team2)

    winner = "Team Alpha" if t1 > t2 else "Team Omega"

    return {
        "winner": winner,
        "team_alpha_power": t1,
        "team_omega_power": t2,
        "story": f"{winner} won after an intense 4v4 clash."
    }


# =========================
# 🏆 TOURNAMENT MODE
# =========================
def run_tournament(characters):

    champion = random.choice(characters)

    return {
        "champion": champion,
        "story": f"{champion} defeated all opponents in the tournament.",
        "participants": characters
    }


# =========================
# 🔥 SURVIVAL MODE
# =========================
def survival_mode(character):

    rounds = random.randint(3, 8)

    return {
        "character": character,
        "rounds_survived": rounds,
        "stamina_left": random.randint(30, 100),
        "xp": rounds * 500,
        "rank": "S-TIER" if rounds > 5 else "A-TIER",
        "achievement": "KING OF THE ARENA"
    }
