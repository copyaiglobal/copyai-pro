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

if "template_text" not in st.session_state:
    st.session_state.template_text = ""

st.set_page_config(page_title="CopyAI Pro - SaaS", page_icon="🚀", layout="centered")

# --- 🔐 REGISTRATION & LOGIN SYSTEM ---
if not st.session_state.is_logged_in:
    st.title("🔐 Welcome to CopyAI Pro")
    st.subheader("Please sign up or log in to access the platform")
    
    auth_tab1, auth_tab2 = st.tabs(["🆕 Sign Up", "🔑 Log In"])
    
    with auth_tab1:
        st.write("### Create a New Account")
        new_email = st.text_input("Enter your Email Address", key="signup_email")
        new_password = st.text_input("Create a Secure Password", type="password", key="signup_pass")
        
        st.write("---")
        plan_choice = st.radio("Choose a plan:", ["Starter Plan ($19/mo)", "Growth Plan ($49/mo)", "Enterprise Plan ($300/mo)"])
        
        if st.button("Register & Proceed 💳", use_container_width=True):
            if not new_email or not new_password:
                st.warning("Please fill in all fields.")
            elif new_email in st.session_state.registered_users:
                st.error("This email is already registered!")
            else:
                st.session_state.registered_users[new_email] = {"password": new_password, "plan": "Starter"}
                st.success("Account created! Please log in.")
                
    with auth_tab2:
        st.write("### Log In to Your Dashboard")
        login_email = st.text_input("Email Address", key="login_email")
        login_password = st.text_input("Password", type="password", key="login_pass")
        
        if st.button("Verify & Log In 🚀", use_container_width=True):
            if login_email in st.session_state.registered_users and st.session_state.registered_users[login_email]["password"] == login_password:
                st.session_state.is_logged_in = True
                st.rerun()
            else:
                st.error("Invalid credentials!")

# --- 📊 REAL DASHBOARD ---
else:
    st.title("🚀 CopyAI Pro — AI Text Generator")
    current_plan_name = st.session_state.current_plan

    st.sidebar.header("📊 User Dashboard")
    st.sidebar.write(f"Plan: {current_plan_name}")
    st.sidebar.progress(min(st.session_state.used_words / PLAN_LIMITS[current_plan_name], 1.0))
    st.sidebar.write(f"Words: {st.session_state.used_words} / {PLAN_LIMITS[current_plan_name]}")
    
    st.sidebar.write("---")
    st.sidebar.header("⚡ Premium Templates")
    
    with st.sidebar.expander("💼 For Freelancers"):
        if st.button("📝 Upwork Proposal Generator", use_container_width=True):
            st.session_state.template_text = "Write a professional Upwork proposal for a Python web development project."
        if st.button("🌟 Fiverr Gig Description", use_container_width=True):
            st.session_state.template_text = "Create an optimized Fiverr gig description for a professional translation service."
        if st.button("✉️ Client Follow-up Email", use_container_width=True):
            st.session_state.template_text = "Draft a polite follow-up email to a client who hasn't responded to the latest project proposal."

    with st.sidebar.expander("🏢 For Agencies"):
        if st.button("📣 Social Media Ad Copy", use_container_width=True):
            st.session_state.template_text = "Write a high-converting Facebook ad copy for an eco-friendly water bottle brand."
if st.button("🔍 SEO Blog Planner", use_container_width=True):
            st.session_state.active_template = "agency"
            st.session_state.template_text = "Create a complete SEO-optimized blog outline and content plan for the topic 'How to start affiliate marketing in 2026'."

with st.sidebar.expander("🚀 For Companies"):
        if st.button("💼 Job Descriptions", use_container_width=True):
            st.session_state.template_text = "Write an attractive job description for a Remote Senior Python Developer position."
        if st.button("📦 Product Descriptions", use_container_width=True):
            st.session_state.template_text = "Create a compelling e-commerce product description for an ergonomic office chair."

st.sidebar.write("---")
if st.sidebar.button("Log Out 🚪", use_container_width=True):
        st.session_state.is_logged_in = False
        st.session_state.template_text = ""
        st.rerun()

st.write("### 🗣️ Select Tone of Voice")
selected_tone = st.selectbox("Choose style:", ["Professional 💼", "Casual ☕", "Witty ✨"])

user_prompt = st.text_area("Final Prompt Dashboard", value=st.session_state.template_text, height=150)

if st.button("Generate Text ✨", use_container_width=True):
        st.info(f"🔒 Active Tone: {selected_tone}. This feature requires an active API gateway. System is ready for launch!")
