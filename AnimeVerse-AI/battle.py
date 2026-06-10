from gemini_utils import get_gemini_response


def battle_1v1(char1, char2):

    try:
        prompt = f"""
        Simulate a professional anime battle analysis between
        {char1} and {char2}.

        Generate:

        💪 POWER ANALYSIS
        Raw Power (0-100)
        Speed (0-100)
        Intelligence (0-100)
        Battle IQ (0-100)
        Durability (0-100)
        Stamina (0-100)
        Special Powers (0-100)

        📊 DETAILED COMPARISON TABLE

        Strength
        Speed
        Intelligence
        Battle IQ
        Durability
        Stamina
        Special Powers
        Combat Skills
        Experience

        🌟 SIGNATURE ABILITIES

        For both fighters.

        🏆 FINAL VERDICT

        Winner
        Win Probability
        Difficulty Rating
        Battle Score For Each Fighter
        MVP Ability
        Winning Factor

        📖 DETAILED BATTLE STORY

        Create a cinematic anime battle story.
        """

        return get_gemini_response(prompt)

    except Exception:

        return f"""
🏆 Winner: {char1}

Win Probability: 65%
Difficulty: Extreme Diff
Battle Score: 950

MVP Ability:
Ultimate Technique

Winning Factor:
Superior Combat Ability

📖 Battle Story

A fierce battle occurred between {char1} and {char2}.

After an intense clash of abilities and strategy,
{char1} emerged victorious.
"""


def battle_2v2(team1, team2):

    try:
        prompt = f"""
        Simulate an anime team battle.

        Team A:
        {team1}

        Team B:
        {team2}

        Generate:

        Attack Power (0-100)
        Defense (0-100)
        Strategy (0-100)
        Synergy (0-100)
        Special Abilities (0-100)

        Team Comparison

        Winner
        Win Probability
        Difficulty Rating
        MVP Fighter
        Best Combo
        Winning Factor

        Generate a detailed team battle story.
        """

        return get_gemini_response(prompt)

    except Exception:

        return """
🏆 Winner: Team A

Win Probability: 60%

Difficulty:
High Diff

MVP Fighter:
Gojo

Best Combo:
Gojo + Sukuna

Winning Factor:
Superior Team Coordination
"""


def battle_4v4(team1, team2):

    try:
        prompt = f"""
        Simulate an epic 4v4 anime battle.

        Team A:
        {team1}

        Team B:
        {team2}

        Generate:

        Team Power Analysis
        Synergy Score
        Attack Rating
        Defense Rating
        Strategy Rating

        MVP Fighter
        Team Rankings
        Winning Factor

        Winner
        Probability
        Difficulty

        Detailed Battle Story
        """

        return get_gemini_response(prompt)

    except Exception:

        return """
🏆 Winner: Team A

MVP Fighter:
Gojo Satoru

Synergy Score:
89

Attack Rating:
95

Defense Rating:
90

Difficulty:
Extreme Diff
"""


def run_tournament(characters):

    try:
        prompt = f"""
        Run a complete anime tournament.

        Participants:
        {characters}

        Generate:

        Quarter Finals

        Semi Finals

        Grand Final

        Champion

        Tournament MVP

        Total Knockouts

        Most Intense Match

        Hall Of Fame

        Tournament Statistics

        Create detailed tournament commentary.
        """

        return get_gemini_response(prompt)

    except Exception:

        return """
🏆 TOURNAMENT RESULTS

Quarter Finals Completed

Semi Finals Completed

Grand Final Completed

👑 Champion:
Gojo Satoru

🔥 Tournament MVP:
Gojo Satoru

Knockouts:
3

Most Intense Match:
Gojo vs Madara

Hall Of Fame:
Gojo Satoru
"""
        

def survival_mode(character):

    try:
        prompt = f"""
        Character:
        {character}

        Run Survival Arena Mode.

        Generate:

        Round 1

        Round 2

        Round 3

        Opponents

        Victories

        Defeats

        XP Earned

        Survival Score

        Arena Rank

        Achievement Unlocked

        Generate a cinematic survival story.
        """

        return get_gemini_response(prompt)

    except Exception:

        return f"""
🔥 SURVIVAL REPORT

Character:
{character}

Rounds Cleared:
5

Enemies Defeated:
4

XP Earned:
4500

Survival Score:
87%

Arena Rank:
S-TIER

Achievement:
KING OF THE ARENA
"""