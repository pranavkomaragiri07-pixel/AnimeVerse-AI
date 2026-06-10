from gemini_utils import get_gemini_response
import random

# =========================
# CORE STAT GENERATOR
# =========================

def generate_stats():
    return {
        "Power": random.randint(60, 100),
        "Speed": random.randint(60, 100),
        "Battle IQ": random.randint(60, 100),
        "Durability": random.randint(60, 100),
        "Stamina": random.randint(60, 100),
        "Weapon Mastery": random.randint(60, 100)
    }

# =========================
# ⚔️ 1v1 BATTLE
# =========================

def battle_1v1(a, b):

    fighter_a = {"name": a, "stats": generate_stats()}
    fighter_b = {"name": b, "stats": generate_stats()}

    category_winners = {}

    for k in fighter_a["stats"]:
        category_winners[k] = (
            a if fighter_a["stats"][k] > fighter_b["stats"][k] else b
        )

    score_a = sum(fighter_a["stats"].values())
    score_b = sum(fighter_b["stats"].values())

    winner = a if score_a > score_b else b

    return {
        "fighter_a": fighter_a,
        "fighter_b": fighter_b,
        "category_winners": category_winners,
        "winner": winner,
        "story": f"{a} vs {b} ended in an intense clash. {winner} won using superior overall stats."
    }

# =========================
# 👥 2v2 BATTLE
# =========================

def battle_2v2(team_a, team_b):

    score_a = sum([sum(generate_stats().values()) for _ in team_a])
    score_b = sum([sum(generate_stats().values()) for _ in team_b])

    winner = "Team A" if score_a > score_b else "Team B"

    return {
        "winner": winner,
        "team_a_score": score_a,
        "team_b_score": score_b,
        "story": f"{team_a} battled {team_b}. {winner} dominated with better coordination and power."
    }

# =========================
# ⚔️ 4v4 BATTLE
# =========================

def battle_4v4(team_a, team_b):

    score_a = sum([sum(generate_stats().values()) for _ in team_a])
    score_b = sum([sum(generate_stats().values()) for _ in team_b])

    winner = "Team Alpha" if score_a > score_b else "Team Omega"

    return {
        "winner": winner,
        "score_a": score_a,
        "score_b": score_b,
        "story": f"4v4 battle concluded. {winner} dominated after extreme combat pressure."
    }

# =========================
# 🏆 TOURNAMENT MODE
# =========================

def run_tournament(characters):

    shuffled = characters[:]
    random.shuffle(shuffled)

    rounds = []

    while len(shuffled) > 1:

        next_round = []

        for i in range(0, len(shuffled), 2):

            if i+1 < len(shuffled):

                a = shuffled[i]
                b = shuffled[i+1]

                winner = a if sum(generate_stats().values()) > sum(generate_stats().values()) else b
                next_round.append(winner)

                rounds.append(f"{a} vs {b} → {winner}")

            else:
                next_round.append(shuffled[i])

        shuffled = next_round

    champion = shuffled[0]

    return {
        "champion": champion,
        "rounds": rounds,
        "story": f"{champion} survived all rounds and became the champion."
    }

# =========================
# 🔥 SURVIVAL MODE
# =========================

def survival_mode(character):

    rounds = []
    score = 0

    for i in range(1, 6):

        enemy = f"Enemy {i}"
        win = random.choice([True, False])

        if win:
            score += random.randint(80, 120)
            rounds.append(f"Round {i}: {character} defeated {enemy}")
        else:
            rounds.append(f"Round {i}: {character} lost to {enemy}")
            break

    return {
        "character": character,
        "score": score,
        "rounds": rounds,
        "story": f"{character} survived {len(rounds)} rounds in the arena."
    }
