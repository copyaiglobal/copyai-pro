import streamlit as st
import openai

openai.api_key = st.secrets.get("OPENAI_API_KEY", "your_api_key_here")

PLAN_LIMITS = {
    "Starter": 50000,
    "Growth": 200000,
    "Enterprise": 9999999
}

def count_words(text):
    if not text:
        return 0
    return len(text.split())

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
    "What do you want the AI to write? (e.g., 'Social media post', 'Blog article')",
    placeholder="Enter your topic here...",
    height=150
)

if st.button("Generate Text ✨", use_container_width=True):
    if not user_prompt.strip():
        st.warning("Please enter a topic first.")
    
    elif st.session_state.used_words >= PLAN_LIMITS[st.session_state.current_plan]:
        st.error("⚠️ Monthly word limit reached! Please upgrade your plan.")
        st.info("💡 Available Plans: Starter ($19) | Growth ($49) | Enterprise ($300)")
    
    else:
        with st.spinner("AI is thinking, please wait..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a professional copywriter and marketer."},
                        {"role": "user", "content": user_prompt}
                    ],
                    max_tokens=1000
                )
                
                ai_generated_text = response.choices.message['content']
                new_words_count = count_words(ai_generated_text)
                st.session_state.used_words += new_words_count
                
                st.success(f"Text generated successfully! (Words: {new_words_count})")
                st.write(ai_generated_text)
                st.rerun()
                
            except Exception as e:
                st.error(f"API Error: {str(e)}")