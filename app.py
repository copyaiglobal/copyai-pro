import streamlit as st

PLAN_LIMITS = {
    "Starter": 50000,
    "Growth": 200000,
    "Enterprise": 9999999
}

# --- XƏTANIN QARŞISINI ALAN ƏSAS QURĞU ---
if "template_text" not in st.session_state:
    st.session_state.template_text = ""

if "registered_users" not in st.session_state:
    st.session_state.registered_users = {}

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if "used_words" not in st.session_state:
    st.session_state.used_words = 0

if "current_plan" not in st.session_state:
    st.session_state.current_plan = "Starter"

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
        st.write("### 💳 Select Your Subscription Plan")
        plan_choice = st.radio("Choose a plan to continue:", ["Starter Plan ($19/mo)", "Growth Plan ($49/mo)", "Enterprise Plan ($300/mo)"])
        
        if st.button("Register & Proceed to Payment 💳", use_container_width=True):
            if not new_email or not new_password:
                st.warning("Please fill in all fields.")
            elif new_email in st.session_state.registered_users:
                st.error("This email is already registered! Please log in.")
            else:
                # Plan adını tərtəmiz sadəcə bircə söz halına salırıq ("Starter")
                selected_plan_word = plan_choice.split(" ")[0]
                st.session_state.registered_users[new_email] = {
                    "password": new_password,
                    "plan": selected_plan_word
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
                
                # Giriş zamanı datanı yoxlayırıq və bircə söz olduğuna əmin oluruq
                user_raw_plan = st.session_state.registered_users[login_email]["plan"]
                if isinstance(user_raw_plan, list):
                    st.session_state.current_plan = str(user_raw_plan[0])
                else:
                    st.session_state.current_plan = str(user_raw_plan)
                
                st.success("Access Granted! Welcome back.")
                st.rerun()
            else:
                st.error("Invalid email or password! Please check your credentials.")

# --- 📊 REAL DASHBOARD & PREMIUM TEMPLATES (100% ENGLISH) ---
else:
    st.title("🚀 CopyAI Pro — AI Text Generator")
    st.subheader("Global SaaS Platform for Freelancers & Agencies")

    # --- 🛡️ KÖHNƏ LİST DATALARINI TƏMİZLƏYƏN QƏTİ FİLTR ---
    raw_plan = st.session_state.get("current_plan", "Starter")
    if isinstance(raw_plan, list):
        current_plan_name = str(raw_plan[0]) if raw_plan else "Starter"
    else:
        current_plan_name = str(raw_plan)

    if current_plan_name not in PLAN_LIMITS:
        current_plan_name = "Starter"
# --- 📋 ENGLISH SIDEBAR TEMPLATES ---
    st.sidebar.header("📊 User Dashboard")
    st.sidebar.write(f"Current Plan: {current_plan_name} Plan")
    st.sidebar.progress(min(st.session_state.used_words / PLAN_LIMITS[current_plan_name], 1.0))
    st.sidebar.write(f"📝 Used Words: {st.session_state.used_words} / {PLAN_LIMITS[current_plan_name]}")
    
    st.sidebar.write("---")
    st.sidebar.header("⚡ Premium Templates")
    
    # 1. For Freelancers Section
    with st.sidebar.expander("💼 For Freelancers"):
        if st.button("📝 Upwork Proposal Generator", use_container_width=True):
            st.session_state.template_text = "Write a high-converting, personalized Upwork proposal for a web design project. Focus on solving the client's problem."
        if st.button("🌟 Fiverr Gig Description", use_container_width=True):
            st.session_state.template_text = "Create an optimized, catchy Fiverr gig description for a professional translation service with SEO keywords."
        if st.button("✉️ Client Follow-up Email", use_container_width=True):
            st.session_state.template_text = "Draft a polite and professional follow-up email to a client who hasn't responded to the latest design submission."
        if st.button("📊 Project Estimate", use_container_width=True):
            st.session_state.template_text = "Generate a formal project estimate and cost breakdown for building a custom mobile app for a small local business."
        if st.button("🧾 Invoice Email", use_container_width=True):
            st.session_state.template_text = "Write a professional, friendly invoice email requesting payment for the completed digital marketing project."

    # 2. For Agencies Section
    with st.sidebar.expander("🏢 For Agencies"):
        if st.button("📣 Social Media Ad Copy", use_container_width=True):
            st.session_state.template_text = "Write 3 high-converting, emotional Facebook and Instagram ad copy variations for an eco-friendly water bottle brand."
        if st.button("🔍 SEO Blog Planner", use_container_width=True):
            st.session_state.template_text = "Create a complete SEO-optimized blog outline and content plan for the topic 'How to start affiliate marketing in 2026'."
        if st.button("📈 Client Report Summary", use_container_width=True):
            st.session_state.template_text = "Generate a weekly marketing performance report summary for a retail client, highlight 15% increase in conversion rates."
        if st.button("❄️ Cold Email Campaign", use_container_width=True):
            st.session_state.template_text = "Draft a compelling cold email outreach template targeting e-commerce store owners to sell web development services."
        if st.button("📅 Content Calendar Creator", use_container_width=True):
            st.session_state.template_text = "Create a 7-day social media content calendar grid for an Instagram profile focused on personal finance education."

    # 3. For Companies Section
    with st.sidebar.expander("🚀 For Companies"):
        if st.button("💼 Job Descriptions", use_container_width=True):
            st.session_state.template_text = "Write an attractive, professional job description for a Remote Senior Python Developer position on LinkedIn."
        if st.button("📦 Product Descriptions", use_container_width=True):
            st.session_state.template_text = "Create a compelling, benefits-focused e-commerce product description for an ergonomic leather office chair."
        if st.button("📁 Internal Communications", use_container_width=True):
            st.session_state.template_text = "Draft a professional internal company email announcing the transition to a new project management platform next week."
        if st.button("🎯 Marketing Campaigns", use_container_width=True):
            st.session_state.template_text = "Generate a comprehensive 30-day product launch marketing campaign strategy and timeline for a new productivity SaaS tool."
        if st.button("🗣️ Brand Voice Manager", use_container_width=True):
            st.session_state.template_text = "Analyze this text and generate a official brand voice and tone guidelines guide for copywriters: [Insert text here]"

    st.sidebar.write("---")
    if st.sidebar.button("Log Out 🚪", use_container_width=True):
        st.session_state.is_logged_in = False
        st.session_state.template_text = ""
        st.rerun()

# --- 📝 MAIN TEXT AREA ---
    user_prompt = st.text_area(
    "What do you want the AI to write? (e.g., 'Social media post', 'Blog article')",
    value=st.session_state.template_text,
    placeholder="Select a template from the sidebar or enter your topic here...",
    height=150
)

if st.button("Generate Text ✨", use_container_width=True):
    st.info("🔒 This feature requires an active production API gateway. System is ready for launch!")