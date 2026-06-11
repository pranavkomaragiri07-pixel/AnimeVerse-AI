import random

# =========================
# STATS ENGINE (UPDATED)
# =========================
def generate_stats():
    return {
        "Power": random.randint(60, 100),
        "Speed": random.randint(60, 100),
        "Battle IQ": random.randint(60, 100),
        "Durability": random.randint(60, 100),
        "Stamina": random.randint(60, 100),
        "Weapon Mastery": random.randint(60, 100),
        "Combat Skills": random.randint(60, 100)  # ✅ ADDED
    }


# =========================
# ⚔️ 1v1 BATTLE
# =========================
def battle_1v1(a, b):

    fa = generate_stats()
    fb = generate_stats()

    category_winners = {
        "Power": a if fa["Power"] > fb["Power"] else b,
        "Speed": a if fa["Speed"] > fb["Speed"] else b,
        "Battle IQ": a if fa["Battle IQ"] > fb["Battle IQ"] else b,
        "Durability": a if fa["Durability"] > fb["Durability"] else b,
        "Stamina": a if fa["Stamina"] > fb["Stamina"] else b,
        "Weapon Mastery": a if fa["Weapon Mastery"] > fb["Weapon Mastery"] else b,
        "Combat Skills": a if fa["Combat Skills"] > fb["Combat Skills"] else b
    }

    a_score = sum(fa.values())
    b_score = sum(fb.values())

    winner = a if a_score > b_score else b

    return {
        "fighter_a": {"name": a, "stats": fa},
        "fighter_b": {"name": b, "stats": fb},
        "category_winners": category_winners,
        "winner": winner,
        "story": f"{a} vs {b} ended in an epic battle. {winner} won."
    }


# =========================
# 👥 2v2 BATTLE
# =========================
def battle_2v2(team_a, team_b):

    score_a = sum(sum(generate_stats().values()) for _ in team_a)
    score_b = sum(sum(generate_stats().values()) for _ in team_b)

    winner = "Team A" if score_a > score_b else "Team B"

    return {
        "winner": winner,
        "category_winners": {
            "Power": winner,
            "Speed": winner,
            "Battle IQ": winner,
            "Durability": winner,
            "Stamina": winner,
            "Weapon Mastery": winner,
            "Combat Skills": winner
        },
        "story": f"{team_a} vs {team_b} was a brutal clash. {winner} dominated."
    }


# =========================
# ⚔️ 4v4 BATTLE
# =========================
def battle_4v4(team_a, team_b):

    score_a = sum(sum(generate_stats().values()) for _ in team_a)
    score_b = sum(sum(generate_stats().values()) for _ in team_b)

    winner = "Team Alpha" if score_a > score_b else "Team Omega"

    return {
        "winner": winner,
        "category_winners": {
            "Power": winner,
            "Speed": winner,
            "Battle IQ": winner,
            "Durability": winner,
            "Stamina": winner,
            "Weapon Mastery": winner,
            "Combat Skills": winner
        },
        "story": f"4v4 battle ended. {winner} crushed the opponent team."
    }


# =========================
# 🏆 TOURNAMENT MODE
# =========================
def run_tournament(fighters):

    fighters = [f for f in fighters if f.strip()]
    random.shuffle(fighters)

    rounds = []

    while len(fighters) > 1:

        next_round = []

        for i in range(0, len(fighters), 2):

            if i + 1 < len(fighters):

                a = fighters[i]
                b = fighters[i + 1]

                sa = sum(generate_stats().values())
                sb = sum(generate_stats().values())

                winner = a if sa > sb else b
                next_round.append(winner)

                rounds.append(f"{a} vs {b} → {winner}")

            else:
                next_round.append(fighters[i])

        fighters = next_round

    champion = fighters[0]

    return {
        "champion": champion,
        "rounds": rounds,
        "story": f"{champion} became the tournament champion after intense battles."
    }


# =========================
# 🔥 SURVIVAL MODE
# =========================
def survival_mode(character):

    rounds = []
    score = 0

    for i in range(1, 6):

        enemy = f"Enemy {i}"

        c_stats = sum(generate_stats().values())
        e_stats = sum(generate_stats().values())

        if c_stats > e_stats:
            score += 100
            rounds.append(f"Round {i}: {character} defeated {enemy}")
        else:
            rounds.append(f"Round {i}: {character} lost to {enemy}")
            break

    return {
        "character": character,
        "score": score,
        "rounds": rounds,
        "story": f"{character} survived {len(rounds)} arena rounds."
    }
