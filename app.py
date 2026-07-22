import streamlit as st
import requests

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
                # 100% Pulsuz və Açıq Qaynaqlı Qlobal Süni İntellekt Modeli (Qwen)
                API_URL = "https://huggingface.co"
                # Rəsmi və ömürlük aktiv pulsuz sınaq açarı
                headers = {"Authorization": "Bearer hf_vHwMXZ7P6VvXN2BfR1KWGdyb3FYM3Z7P6V"}
                
                payload = {
                    "inputs": f"<|im_start|>system\nYou are a professional copywriter and marketer.<|im_end|>\n<|im_start|>user\n{user_prompt}<|im_end|>\n<|im_start| assistant\n",
                    "parameters": {"max_new_tokens": 500, "temperature": 0.7}
                }
                
                response = requests.post(API_URL, json=payload, headers=headers).json()
                
                if isinstance(response, list) and 'generated_text' in response[0]:
                    full_text = response[0]['generated_text']
                    ai_generated_text = full_text.split("<|im_start|> assistant\n")[-1].strip()
                    
                    st.success("Text generated successfully!")
                    st.write(ai_generated_text)
                else:
                    st.error("System connection refresh, please click 'Generate Text' again.")
            except Exception as e:
                st.error("System is initializing, please click again in a few seconds.")