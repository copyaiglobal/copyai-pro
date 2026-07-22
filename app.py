import streamlit as st
import requests

# Yenilənmiş tam təhlükəsiz və pulsuz model açarı
API_KEY = "gsk_yV8jM3Z7P6VvXN2BfR1KWGdyb3FYM3Z7P6VvXN2BfR1K" 

PLAN_LIMITS = {"Starter": 50000, "Growth": 200000, "Enterprise": 9999999}

if "used_words" not in st.session_state:
    st.session_state.used_words = 0
if "current_plan" not in st.session_state:
    st.session_state.current_plan = "Starter"

st.set_page_config(page_title="CopyAI Pro - SaaS", page_icon="🚀", layout="centered")

st.title("🚀 CopyAI Pro — AI Text Generator")
st.subheader("Global SaaS Platform for Freelancers & Agencies")

st.sidebar.header("📊 User Dashboard")
st.sidebar.write(f"Current Plan: {st.session_state.current_plan} Plan")
st.sidebar.progress(min(st.session_state.used_words / PLAN_LIMITS[st.session_state.current_plan], 1.0))
st.sidebar.write(f"📝 Used Words: {st.session_state.used_words} / {PLAN_LIMITS[st.session_state.current_plan]}")

user_prompt = st.text_area(
    "What do you want the AI to write? (e.g., 'Social media post')",
    placeholder="Enter your topic here...",
    height=150
)

if st.button("Generate Text ✨", use_container_width=True):
    if not user_prompt.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("AI is thinking, please wait..."):
            try:
                url = "https://groq.com"
                headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
                data = {
                    "model": "llama3-8b-8192",  # Daha stabil və sürətli pulsuz model
                    "messages": [
                        {"role": "system", "content": "You are a professional copywriter."},
                        {"role": "user", "content": user_prompt}
                    ]
                }
                res = requests.post(url, json=data, headers=headers).json()
                
                # Zəmanətli cavab yoxlaması
                if 'choices' in res and len(res['choices']) > 0:
                    ai_generated_text = res['choices'][0]['message']['content']
                    st.success("Text generated successfully!")
                    st.write(ai_generated_text)
                else:
                    st.error("System is busy, please click 'Generate Text' again.")
            except Exception as e:
                st.error("System is initializing, please click again.")
