import streamlit as st
import json
from chatbot import SimpleBot

st.set_page_config(page_title="WCC Info Bot", page_icon="🤖")

st.title("🤖 WCC Info Bot")
st.markdown("Ask me anything about Women Coding Community!")

# Load FAQs
with open("wcc_faqs.json") as f:
    wcc_data = json.load(f)

faq_text = "\n".join([
    f"Q: {faq['question']}\nA: {faq['answer']}"
    for faq in wcc_data["faqs"]
])

system_prompt = f"""You are a friendly WCC assistant...
{faq_text}"""

# Initialize bot
if "bot" not in st.session_state:
    st.session_state.bot = SimpleBot(system_prompt=system_prompt)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if user_input := st.chat_input("Ask me about WCC..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    response = st.session_state.bot.chat(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    with st.chat_message("assistant"):
        st.markdown(response)