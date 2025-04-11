import streamlit as st 

st.set_page_config(page_title = "My Streamlit App", layout="wide")
st.title("LangGraph Chatbot")
st.write("This is a simple chatbot application using LangGraph and searchtools.")

system_prompt = st.text_area("Select your AI Agent : ", height=70, placeholder="Enter your system prompt here")

MODEL_NAMES_GROQ = ["gemma2-9b-it"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select a provider", ("groq", "openai"))

if provider == "groq":
    model_name = st.selectbox("Select a model", MODEL_NAMES_GROQ)
elif provider == "openai":
    model_name = st.selectbox("Select a model", MODEL_NAMES_OPENAI)

allow_search = st.checkbox("Allow search")

user_query = st.text_area("Enter your query", height=150, placeholder="Ask anything here")

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask Agent"):

    if user_query.strip():
        import requests

        payload = { "model_name": model_name,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_search
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            reponse_data = response.json()
            if "error" in reponse_data:
                st.error(reponse_data["error"])
            else:                
                st.subheader("AI Says")
                st.markdown(f"Final Response : {reponse_data}")