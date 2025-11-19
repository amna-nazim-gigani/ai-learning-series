from chatbot import SimpleBot

def test_wcc_bot():
    bot = SimpleBot(system_prompt="You are a WCC assistant.")
    
    # Test basic response
    response = bot.chat("What is WCC?")
    assert len(response) > 0
    
    # Test conversation memory
    bot.chat("I'm interested in AI")
    response = bot.chat("Can you recommend a session?")
    assert "AI" in response or "session" in response.lower()
    
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_wcc_bot()