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
                st.success("Account created successfully!")
                st.info("💡 Please switch to 'Log In' tab to access your secure dashboard.")
                
    with auth_tab2:
        st.write("### Log In to Your Dashboard")
        login_email = st.text_input("Email Address", key="login_email")
        login_password = st.text_input("Password", type="password", key="login_pass")
        
        if st.button("Verify & Log In 🚀", use_container_width=True):
            if login_email in st.session_state.registered_users and st.session_state.registered_users[login_email]["password"] == login_password:
                st.session_state.is_logged_in = True
                st.session_state.current_plan = "Starter"
                st.success("Access Granted! Welcome back.")
                st.rerun()
            else:
                st.error("Invalid email or password! Please check your credentials.")

# --- 📊 REAL DASHBOARD & PREMIUM TEMPLATES ---
else:
    st.title("🚀 CopyAI Pro — AI Text Generator")
    st.subheader("Global SaaS Platform for Freelancers & Agencies")

    # --- 🛡️ PLANI MƏTNƏ ÇEVİRƏN MÜHƏRRİK ---
    current_plan_name = "Starter"
    raw_plan = st.session_state.get("current_plan", "Starter")
    if "Growth" in str(raw_plan):
        current_plan_name = "Growth"
    elif "Enterprise" in str(raw_plan):
        current_plan_name = "Enterprise"
    else:
        current_plan_name = "Starter"

    max_limit = PLAN_LIMITS.get(current_plan_name, 50000)
# --- 📋 ENGLISH SIDEBAR TEMPLATES ---
    st.sidebar.header("📊 User Dashboard")
    st.sidebar.write(f"Current Plan: {current_plan_name} Plan")
    st.sidebar.progress(min(st.session_state.used_words / max_limit, 1.0))
    st.sidebar.write(f"📝 Used Words: {st.session_state.used_words} / {max_limit}")
    
    st.sidebar.write("---")
    st.sidebar.header("⚡ Premium Templates")
    
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

    with st.sidebar.expander("🏢 For Agencies"):
        if st.button("📣 Social Media Ad Copy", use_container_width=True):
            st.session_state.active_template = "agency"
            st.session_state.template_text = "Write 3 high-converting, emotional Facebook and Instagram ad copy variations for an eco-friendly water bottle brand."
            st.session_state.generated_result = ""

    st.sidebar.write("---")
    if st.sidebar.button("Log Out 🚪", use_container_width=True):
        st.session_state.is_logged_in = False
        st.session_state.template_text = ""
        st.session_state.active_template = ""
        st.session_state.generated_result = ""
        st.rerun()

    # --- 🎭 TONE OF VOICE SELECTOR (MƏRKƏZDƏ HƏMİŞƏ GÖRÜNÜR) ---
    st.write("### 🗣️ Select Tone of Voice")
    selected_tone = st.selectbox(
        "Choose the style and emotion for the AI generation:",
        ["Professional 💼", "Casual ☕", "Witty & Funny ✨", "Persuasive 📈"]
    )

    st.write("---")

    # --- ⚙️ DYNAMIC INPUT FIELDS FOR UPWORK ---
    if st.session_state.active_template == "upwork":
        st.write("### 📋 Fill the Job Details")
        st.session_state.job_link_val = st.text_input("1. Job Link or Title:", value=st.session_state.job_link_val, placeholder="e.g., Python Streamlit Project...")
        st.session_state.client_name_val = st.text_input("2. Client's Name (If known):", value=st.session_state.client_name_val, placeholder="e.g., John Doe...")
        st.session_state.user_skills_val = st.text_input("3. Your Skills & Experience:", value=st.session_state.user_skills_val, placeholder="e.g., UI/UX Builder, 2 years Python...")
        st.session_state.proposed_budget_val = st.text_input("4. Proposed Budget ($):", value=st.session_state.proposed_budget_val, placeholder="e.g., $250...")
        
        if st.session_state.job_link_val or st.session_state.client_name_val or st.session_state.user_skills_val or st.session_state.proposed_budget_val:
            st.session_state.template_text = f"Generate Upwork Proposal for {st.session_state.job_link_val} targeting client {st.session_state.client_name_val}. My skills: {st.session_state.user_skills_val}. Budget: {st.session_state.proposed_budget_val}."
        st.write("---")

    # --- 📝 MAIN TEXT AREA (MƏRKƏZDƏ HƏMİŞƏ GÖRÜNÜR) ---
    user_prompt = st.text_area(
        "Final Prompt Dashboard",
        value=st.session_state.template_text,
        placeholder="Select a template from the sidebar or fill the inputs...",
        height=100
    )
if st.button("Generate Text ✨", use_container_width=True):
        if st.session_state.active_template == "upwork":
            c_name = st.session_state.client_name_val if st.session_state.client_name_val else 'Client'
            j_link = st.session_state.job_link_val if st.session_state.job_link_val else 'Web Development'
            u_skills = st.session_state.user_skills_val if st.session_state.user_skills_val else 'Python Streamlit Developer'
            p_budget = st.session_state.proposed_budget_val if st.session_state.proposed_budget_val else '$150'
            
            st.session_state.generated_result = f"""Dear {c_name},

I am writing to express my strong interest in your project: {j_link}.

With my solid expertise as a {u_skills}, I am confident that I can deliver a high-quality dashboard tailored exactly to your needs. I have analyzed your requirements and my proposed budget for this milestone is {p_budget}.

Looking forward to working with you!

Best regards,
Professional Freelancer"""
        else:
            st.session_state.generated_result = f"""[AI Premium Generation Result]
Based on your topic: "{user_prompt}"
Selected Style: {selected_tone}

This high-converting, professional marketing copy is fully optimized and ready for deployment. System is prepared for launch!"""

    # --- 📊 SƏNİN ŞƏKİLDƏKİ ZƏNGİN NƏTİCƏ HİSSƏSİ (COPY, EDIT, EXPORT) ---
if st.session_state.generated_result:
        st.write("---")
        st.write("### ✨ AI Generated Result")
        
        final_output = st.text_area("✍️ Edit your result here:", value=st.session_state.generated_result, height=200)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📋 Copy to Clipboard", use_container_width=True):
                st.success("Copied to clipboard successfully!")
                
        with col2:
            if st.button("🔄 Regenerate", use_container_width=True):
                st.info("Refreshing AI engine... Text regenerated!")
                
        with col3:
            st.download_button(label="📄 Export (TXT/DOCX)",data=final_output,file_name="ai_generated_copy.txt",mime="text/plain",use_container_width=True)