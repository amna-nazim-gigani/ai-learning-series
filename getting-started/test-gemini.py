import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure API
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    print("❌ Error: GEMINI_API_KEY not found in .env file")
    exit(1)

genai.configure(api_key=api_key)

# Test the API
try:
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    response = model.generate_content("What is AI? Explain to a novice.")
    print("✅ API is working!")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"❌ Error: {e}")