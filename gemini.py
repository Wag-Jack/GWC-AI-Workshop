from google import genai
from dotenv import load_dotenv

# Loads in Gemini API key we put into .env
load_dotenv()

# Make our Gemini client
client = genai.Client()

while True:
    query = input("How can I help you? (Type \'Q\' to exit.)\n")

    if query == 'Q':
        break

    # Connect to the Gemini client and make a response
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=query
    )

    print(response.text)