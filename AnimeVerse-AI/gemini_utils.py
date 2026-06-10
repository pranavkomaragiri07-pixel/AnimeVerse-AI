from google import genai
from config import GEMINI_API_KEY
import time

client = genai.Client(api_key=GEMINI_API_KEY)

def get_gemini_response(prompt):

    for _ in range(3):

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            return response.text

        except Exception:
            time.sleep(5)

    return "Gemini service is busy. Please try again."