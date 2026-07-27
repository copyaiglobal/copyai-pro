import streamlit as st

PLAN_LIMITS = {
    "Starter": 50000,
    "Growth": 200000,
    "Enterprise": 9999999
}

# --- 🧠 XƏTANIN QARŞISINI ALAN DAXİLİ YADDAŞ BUNKERİ ---
if "template_text" not in st.session_state:
    st.session_state.template_text = ""

if "active_template" not in st.session_state:
    st.session_state.active_template = ""

if "generated_result" not in st.session_state:
    st.session_state.generated_result = ""

if "registered_users" not in st.session_state:
    st.session_state.registered_users = {}

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if "used_words" not in st.session_state:
    st.session_state.used_words = 0

if "current_plan" not in st.session_state:
    st.session_state.current_plan = "Starter"

# Məlumatların itməməsi üçün onları yaddaş qutularına qoyuruq
if "job_link_val" not in st.session_state:
    st.session_state.job_link_val = ""
if "client_name_val" not in st.session_state:
    st.session_state.client_name_val = ""
if "user_skills_val" not in st.session_state:
    st.session_state.user_skills_val = ""
if "proposed_budget_val" not in st.session_state:
    st.session_state.proposed_budget_val = ""

st.set_page_config(page_title="CopyAI Pro - SaaS", page_icon="🚀", layout="centered")

# --- 🔐 REGISTRATION & LOGIN SYSTEM ---
if not st.session_state.is_logged_in:
    st.title("🔐 Welcome to CopyAI Pro")
    st.subheader("Please sign up or log in to access the platform")
    
    auth_tab1, auth_tab2 = st.tabs(["🆕 Sign Up (Create Account)", "🔑 Log In (Access Account)"])
    
    with auth_tab1:
        st.write("### Create a New Account")
        new_email = st.text_input("Enter your Email Address", key="signup_email")
        new_password = st.text_input("Create a Secure Password", type="password", key="signup_pass")
        
        st.write("---")
        plan_choice = st.radio("Choose a plan to continue:", ["Starter Plan ($19/mo)", "Growth Plan ($49/mo)", "Enterprise Plan ($300/mo)"])
        
        if st.button("Register & Proceed to Payment 💳", use_container_width=True):
            if not new_email or not new_password:
                st.warning("Please fill in all fields.")
            elif new_email in st.session_state.registered_users:
                st.error("This email is already registered! Please log in.")
            else:
                st.session_state.registered_users[new_email] = {"password": new_password, "plan": "Starter"}
                st.success("Account created successfully! Payment gateway ready.")
                st.info("💡 Please switch to 'Log In' tab to access your secure dashboard.")
                
    with auth_tab2:
        st.write("### Log In to Your Dashboard")
        login_email = st.text_input("Email Address", key="login_email")
        login_password = st.text_input("Password", type="password", key="login_pass")
        
        if st.button("Verify & Log In 🚀", use_container_width=True):
            if login_email in st.session_state.registered_users and st.session_state.registered_users[login_email]["password"] == login_password:
                st.session_state.is_logged_in = True
                st.success("Access Granted! Welcome back.")
                st.rerun()
            else:
                st.error("Invalid email or password! Please check your credentials.")

# --- 📊 REAL DASHBOARD & PREMIUM TEMPLATES ---
else:
    st.title("🚀 CopyAI Pro — AI Text Generator")
    st.subheader("Global SaaS Platform for Freelancers & Agencies")

    current_plan_name = st.session_state.current_plan

    # --- 📋 ENGLISH SIDEBAR TEMPLATES ---
    st.sidebar.header("📊 User Dashboard")
    st.sidebar.write(f"Current Plan: {current_plan_name} Plan")
    st.sidebar.progress(min(st.session_state.used_words / PLAN_LIMITS[current_plan_name], 1.0))
st.sidebar.write(f"📝 Used Words: {st.session_state.used_words} / {PLAN_LIMITS[current_plan_name]}")
    
st.sidebar.write("---")
st.sidebar.header("⚡ Premium Templates")
    
    # 1. BÜTÜN FREELANCER ŞABLONLARI GERİ GƏLDİ
with st.sidebar.expander("💼 For Freelancers"):
        if st.button("📝 Upwork Proposal Generator", use_container_width=True):
            st.session_state.active_template = "upwork"
            st.session_state.template_text = ""
            st.session_state.generated_result = ""
        if st.button("🌟 Fiverr Gig Description", use_container_width=True):
            st.session_state.active_template = "fiverr"
            st.session_state.template_text = "Create an optimized, catchy Fiverr gig description for a professional translation service with SEO keywords."
            st.session_state.generated_result = ""
        if st.button("✉️ Client Follow-up Email", use_container_width=True):
            st.session_state.active_template = "followup"
            st.session_state.template_text = "Draft a polite and professional follow-up email to a client who hasn't responded to the latest design submission."
            st.session_state.generated_result = ""
        if st.button("📊 Project Estimate", use_container_width=True):
            st.session_state.active_template = "estimate"
            st.session_state.template_text = "Generate a formal project estimate and cost breakdown for building a custom mobile app for a small local business."
            st.session_state.generated_result = ""
        if st.button("🧾 Invoice Email", use_container_width=True):
            st.session_state.active_template = "invoice"
            st.session_state.template_text = "Write a professional, friendly invoice email requesting payment for the completed digital marketing project."
            st.session_state.generated_result = ""

    # 2. BÜTÜN AGENTLİK ŞABLONLARI GERİ GƏLDİ
with st.sidebar.expander("🏢 For Agencies"):
        if st.button("📣 Social Media Ad Copy", use_container_width=True):
            st.session_state.active_template = "agency"
            st.session_state.template_text = "Write 3 high-converting, emotional Facebook and Instagram ad copy variations for an eco-friendly water bottle brand."
            st.session_state.generated_result = ""
        if st.button("🔍 SEO Blog Planner", use_container_width=True):
            st.session_state.active_template = "agency"
            st.session_state.template_text = "Create a complete SEO-optimized blog outline and content plan for the topic 'How to start affiliate marketing in 2026'."
            st.session_state.generated_result = ""
        if st.button("📈 Client Report Summary", use_container_width=True):
            st.session_state.active_template = "agency"
            st.session_state.template_text = "Generate a weekly marketing performance report summary for a retail client, highlight 15% increase in conversion rates."
            st.session_state.generated_result = ""
        if st.button("❄️ Cold Email Campaign", use_container_width=True):
            st.session_state.active_template = "agency"
            st.session_state.template_text = "Draft a compelling cold email outreach template targeting e-commerce store owners to sell web development services."
            st.session_state.generated_result = ""
        if st.button("📅 Content Calendar Creator", use_container_width=True):
            st.session_state.active_template = "agency"
            st.session_state.template_text = "Create a 7-day social media content calendar grid for an Instagram profile focused on personal finance education."
            st.session_state.generated_result = ""

    # 3. BÜTÜN ŞİRKƏT ŞABLONLARI GERİ GƏLDİ
with st.sidebar.expander("🚀 For Companies"):
        if st.button("💼 Job Descriptions", use_container_width=True):
            st.session_state.active_template = "company"
            st.session_state.template_text = "Write an attractive, professional job description for a Remote Senior Python Developer position on LinkedIn."
            st.session_state.generated_result = ""
        if st.button("📦 Product Descriptions", use_container_width=True):
            st.session_state.active_template = "company"
            st.session_state.template_text = "Create a compelling, benefits-focused e-commerce product description for an ergonomic leather office chair."
            st.session_state.generated_result = ""
        if st.button("📁 Internal Communications", use_container_width=True):
            st.session_state.active_template = "company"
            st.session_state.template_text = "Draft a professional internal company email announcing the transition to a new project management platform next week."
            st.session_state.generated_result = ""
        if st.button("🎯 Marketing Campaigns", use_container_width=True):
            st.session_state.active_template = "company"
            st.session_state.template_text = "Generate a comprehensive 30-day product launch marketing campaign strategy and timeline for a new productivity SaaS tool."
            st.session_state.generated_result = ""
        if st.button("🗣️ Brand Voice Manager", use_container_width=True):
            st.session_state.active_template = "company"
            st.session_state.template_text = "Analyze this text and generate a official brand voice and tone guidelines guide for copywriters: [Insert text here]"
            st.session_state.generated_result = ""

            st.sidebar.write("---")
        if st.sidebar.button("Log Out 🚪", use_container_width=True):
            st.session_state.is_logged_in = False
            st.session_state.template_text = ""
            st.session_state.active_template = ""
            st.session_state.generated_result = ""
            st.rerun()

    # --- 🎭 TONE OF VOICE SELECTOR ---
st.write("### 🗣️ Select Tone of Voice")
selected_tone = st.selectbox(
        "Choose the style and emotion for the AI generation:",
        ["Professional 💼", "Casual ☕", "Witty & Funny ✨", "Persuasive 📈"]
    )

st.write("---")