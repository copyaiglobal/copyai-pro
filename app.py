import streamlit as st
import google.generativeai as genai

# Google Gemini API Key tənzimləməsi (Secrets-dən oxunur)
api_key = st.secrets.get("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

PLAN_LIMITS = {
    "Starter": 50000,
    "Growth": 200000,
    "Enterprise": 9999999
}

def count_words(text):
    if not text:
        return 0
    return len(text.split())

if "registered_users" not in st.session_state:
    st.session_state.registered_users = {}

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if "used_words" not in st.session_state:
    st.session_state.used_words = 0

if "current_plan" not in st.session_state:
    st.session_state.current_plan = "Starter"

st.set_page_config(page_title="CopyAI Pro - SaaS", page_icon="🚀", layout="centered")

# --- 🔐 QEYDİYYAT VƏ GİRİŞ SİSTEMİ ---
if not st.session_state.is_logged_in:
    st.title("🔐 Welcome to CopyAI Pro")
    st.subheader("Please sign up or log in to access the platform")
    
    auth_tab1, auth_tab2 = st.tabs(["🆕 Sign Up (Create Account)", "🔑 Log In (Access Account)"])
    
    with auth_tab1:
        st.write("### Create a New Account")
        new_email = st.text_input("Enter your Email Address", key="signup_email")
        new_password = st.text_input("Create a Secure Password", type="password", key="signup_pass")
        
        if st.button("Register & Pay ($19 / $49 / $300) 💳", use_container_width=True):
            if not new_email or not new_password:
                st.warning("Please fill in all fields.")
            elif new_email in st.session_state.registered_users:
                st.error("This email is already registered! Please log in.")
            else:
                st.session_state.registered_users[new_email] = new_password
                st.success("Account created successfully! Payment verification simulated.")
                st.info("💡 Please switch to Log In tab to access your dashboard.")
                
    with auth_tab2:
        st.write("### Log In to Your Dashboard")
        login_email = st.text_input("Email Address", key="login_email")
        login_password = st.text_input("Password", type="password", key="login_pass")
        
        if st.button("Verify & Log In 🚀", use_container_width=True):
            if login_email in st.session_state.registered_users and st.session_state.registered_users[login_email] == login_password:
                st.session_state.is_logged_in = True
                st.success("Access Granted! Welcome back.")
                st.rerun()
            else:
                st.error("Invalid email or password! Please check your credentials or purchase a plan.")

# --- 📊 REAL DASHBOARD ---
else:
    st.title("🚀 CopyAI Pro — AI Text Generator")
    st.subheader("Global SaaS Platform for Freelancers & Agencies")

    st.sidebar.header("📊 User Dashboard")
    st.sidebar.write(f"Current Plan: {st.session_state.current_plan} Plan")
    st.sidebar.progress(min(st.session_state.used_words / PLAN_LIMITS[st.session_state.current_plan], 1.0))
    st.sidebar.write(f"📝 Used Words: {st.session_state.used_words} / {PLAN_LIMITS[st.session_state.current_plan]}")
    
    if st.sidebar.button("Log Out 🚪", use_container_width=True):
        st.session_state.is_logged_in = False
        st.rerun()

    user_prompt = st.text_area(
        "What do you want the AI to write? (e.g., 'Social media post', 'Blog article')",
        placeholder="Enter your topic here...",
        height=150
    )

    if st.button("Generate Text ✨", use_container_width=True):
        if not user_prompt.strip():
            st.warning("Please enter a topic first.")
        elif not api_key:
            st.error("⚠️ API Key is missing! Please configure GEMINI_API_KEY in Streamlit Secrets.")
    elif st.session_state.used_words >= PLAN_LIMITS[st.session_state.current_plan]:
            st.error("⚠️ Monthly word limit reached! Please upgrade your plan.")
    else:
            with st.spinner("AI is thinking, please wait..."):
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    response = model.generate_content(
                        f"You are a professional copywriter and marketer. Prompt: {user_prompt}"
                    )
                    ai_generated_text = response.text
                    new_words_count = count_words(ai_generated_text)
                    st.session_state.used_words += new_words_count
                    
                    st.success(f"Text generated successfully! (Words: {new_words_count})")
                    st.write(ai_generated_text)
                except Exception as e:
                    st.error(f"API Error: {str(e)}")