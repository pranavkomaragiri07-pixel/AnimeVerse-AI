from gemini_utils import get_gemini_response

def generate_quote(theme):

    try:
        prompt = f"""
        Generate an anime quote.

        Theme: {theme}

        Return:
        Quote
        Character
        Anime
        """

        result = get_gemini_response(prompt)

        if "Gemini service is busy" in result:
            raise Exception("Gemini Busy")

        return result

    except Exception:

        return """
Quote:
Never give up, no matter how difficult the path becomes.

Character:
Naruto Uzumaki

Anime:
Naruto
"""