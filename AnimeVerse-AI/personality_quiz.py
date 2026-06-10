from gemini_utils import get_gemini_response

def get_character_match(answers):

    try:
        prompt = f"""
        User Answers:
        {answers}

        Determine anime character.

        Return:
        Character Name
        Match Percentage
        Personality Explanation
        """

        result = get_gemini_response(prompt)

        if "Gemini service is busy" in result:
            raise Exception("Gemini Busy")

        return result

    except Exception:

        return """
Character: Monkey D. Luffy

Match Percentage: 92%

Traits:
• Adventurous
• Fearless
• Optimistic
• Loyal to Friends

Explanation:
You love freedom, value friendship,
and never back down from challenges.
"""