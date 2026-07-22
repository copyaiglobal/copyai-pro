import streamlit as st

PLAN_LIMITS = {
    "Starter": 50000,
    "Growth": 200000,
    "Enterprise": 9999999
}

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
        
        st.write("---")
        st.write("### 💳 Select Your Subscription Plan")
        plan_choice = st.radio("Choose a plan to continue:", ["Starter Plan ($19/mo)", "Growth Plan ($49/mo)", "Enterprise Plan ($300/mo)"])
        
        if st.button("Register & Proceed to Payment 💳", use_container_width=True):
            if not new_email or not new_password:
                st.warning("Please fill in all fields.")
            elif new_email in st.session_state.registered_users:
                st.error("This email is already registered! Please log in.")
            else:
                selected_plan_name = plan_choice.split(" ")[0]
                st.session_state.registered_users[new_email] = {
                    "password": new_password,
                    "plan": selected_plan_name
                }
                st.success("Account created successfully! Payment gateway ready.")
                st.info("💡 Please switch to 'Log In' tab to access your secure dashboard.")
                
    with auth_tab2:
        st.write("### Log In to Your Dashboard")
        login_email = st.text_input("Email Address", key="login_email")
        login_password = st.text_input("Password", type="password", key="login_pass")
        
        if st.button("Verify & Log In 🚀", use_container_width=True):
            if login_email in st.session_state.registered_users and st.session_state.registered_users[login_email]["password"] == login_password:
                st.session_state.is_logged_in = True
                st.session_state.current_plan = st.session_state.registered_users[login_email]["plan"]
                st.success("Access Granted! Welcome back.")
                st.rerun()
            else:
                st.error("Invalid email or password! Please check your credentials.")

# --- 📊 REAL DASHBOARD VITRINI (YALNIZ GİRİŞ EDƏNDƏ GÖRÜNÜR) ---
else:
    st.title("🚀 CopyAI Pro — AI Text Generator")
    st.subheader("Global SaaS Platform for Freelancers & Agencies")

    current_plan_name = st.session_state.get("current_plan", "Starter")
    if current_plan_name not in PLAN_LIMITS:
        current_plan_name = "Starter"

    st.sidebar.header("📊 User Dashboard")
    st.sidebar.write(f"Current Plan: {current_plan_name} Plan")
    st.sidebar.progress(min(st.session_state.used_words / PLAN_LIMITS[current_plan_name], 1.0))
    st.sidebar.write(f"📝 Used Words: {st.session_state.used_words} / {PLAN_LIMITS[current_plan_name]}")
    
    if st.sidebar.button("Log Out 🚪", use_container_width=True):
        st.session_state.is_logged_in = False
        st.rerun()

    user_prompt = st.text_area(
        "What do you want the AI to write? (e.g., 'Social media post', 'Blog article')",
        placeholder="Enter your topic here...",
        height=150
    )

    if st.button("Generate Text ✨", use_container_width=True):
        st.info("🔒 This feature requires an active production API gateway. System is ready for launch!")