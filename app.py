import streamlit as st

PLAN_LIMITS = {
    "Starter": 50000,
    "Growth": 200000,
    "Enterprise": 9999999
}

# --- 🧠 DAXİLİ YADDAŞ BUNKERİ ---
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

if "upwork_link" not in st.session_state:
    st.session_state.upwork_link = ""
if "upwork_client" not in st.session_state:
    st.session_state.upwork_client = ""
if "upwork_skills" not in st.session_state:
    st.session_state.upwork_skills = ""
if "upwork_budget" not in st.session_state:
    st.session_state.upwork_budget = ""

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
    current_plan_name = "Starter"
    raw_plan = st.session_state.get("current_plan", "Starter")
    if "Growth" in str(raw_plan): current_plan_name = "Growth"
    elif "Enterprise" in str(raw_plan): current_plan_name = "Enterprise"
    
    max_limit = PLAN_LIMITS.get(current_plan_name, 50000)
    current_plan_name = st.session_state.get("current_plan", "Starter")
    max_limit = PLAN_LIMITS.get(current_plan_name, 50000)
    st.sidebar.header("📊 User Dashboard")
    st.sidebar.write(f"Current Plan: {current_plan_name} Plan")
    st.sidebar.progress(min(st.session_state.used_words / max_limit, 1.0))
max_limit = 50000
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
        if st.button("📊 Project Estimate", use_container_width=True):
            st.session_state.active_template = "estimate"
            st.session_state.template_text = "Generate a formal project estimate and cost breakdown for building a custom mobile app for a small local business."
            st.session_state.generated_result = ""
        if st.button("🧾 Invoice Email", use_container_width=True):
            st.session_state.active_template = "invoice"
            st.session_state.template_text = "Write a professional, friendly invoice email requesting payment for the completed digital marketing project."
            st.session_state.generated_result = ""

with st.sidebar.expander("🏢 For Agencies"):
        if st.button("📣 Social Media Ad Copy", use_container_width=True):
            st.session_state.active_template = "agency_ad"
            st.session_state.template_text = "Write 3 high-converting, emotional Facebook and Instagram ad copy variations for an eco-friendly water bottle brand."
            st.session_state.generated_result = ""
        if st.button("🔍 SEO Blog Planner", use_container_width=True):
            st.session_state.active_template = "agency_blog"
            st.session_state.template_text = "Create a complete SEO-optimized blog outline and content plan for the topic 'How to start affiliate marketing in 2026'."
            st.session_state.generated_result = ""
        if st.button("📈 Client Report Summary", use_container_width=True):
            st.session_state.active_template = "agency_report"
            st.session_state.template_text = "Generate a weekly marketing performance report summary for a retail client, highlight 15% increase in conversion rates."
            st.session_state.generated_result = ""
        if st.button("❄️ Cold Email Campaign", use_container_width=True):
            st.session_state.active_template = "agency_cold"
            st.session_state.template_text = "Draft a compelling cold email outreach template targeting e-commerce store owners to sell web development services."
            st.session_state.generated_result = ""
        if st.button("📅 Content Calendar Creator", use_container_width=True):
            st.session_state.active_template = "agency_calendar"
            st.session_state.template_text = "Create a 7-day social media content calendar grid for an Instagram profile focused on personal finance education."
            st.session_state.generated_result = ""

with st.sidebar.expander("🚀 For Companies"):
        if st.button("💼 Job Descriptions", use_container_width=True):
            st.session_state.active_template = "company_job"
            st.session_state.template_text = "Write an attractive, professional job description for a Remote Senior Python Developer position on LinkedIn."
            st.session_state.generated_result = ""
        if st.button("📦 Product Descriptions", use_container_width=True):
            st.session_state.active_template = "company_prod"
            st.session_state.template_text = "Create a compelling, benefits-focused e-commerce product description for an ergonomic leather office chair."
            st.session_state.generated_result = ""
        if st.button("📁 Internal Communications", use_container_width=True):
            st.session_state.active_template = "company_internal"
            st.session_state.template_text = "Draft a professional internal company email announcing the transition to a new project management platform next week."
            st.session_state.generated_result = ""
        if st.button("🎯 Marketing Campaigns", use_container_width=True):
            st.session_state.active_template = "company_market"
            st.session_state.template_text = "Generate a comprehensive 30-day product launch marketing campaign strategy and timeline for a new productivity SaaS tool."
            st.session_state.generated_result = ""
        if st.button("🗣️ Brand Voice Manager", use_container_width=True):
            st.session_state.active_template = "company_voice"
            st.session_state.template_text = "Analyze this text and generate a official brand voice and tone guidelines guide for copywriters: [Insert text here]"
            st.session_state.generated_result = ""

st.sidebar.write("---")
if st.sidebar.button("Log Out 🚪", use_container_width=True):
        st.session_state.is_logged_in = False
        st.session_state.template_text = ""
        st.session_state.active_template = ""
        st.session_state.generated_result = ""
        st.rerun()

st.title("🚀 CopyAI Pro — AI Text Generator")
st.subheader("Global SaaS Platform for Freelancers & Agencies")

st.write("### 🗣️ Select Tone of Voice")
selected_tone = st.selectbox(
        "Choose the style and emotion for the AI generation:",
        ["Professional 💼", "Casual ☕", "Witty & Funny ✨", "Persuasive 📈"]
    )

st.write("---")
# --- ⚙️ BAX BU HİSSƏDƏ IF-ELSE-LƏR TAM AYRILDI VƏ SATİR ARASINA BÖLÜNDÜ ---
if st.session_state.active_template == "upwork":
    st.write("### 📋 Fill the Upwork Job Details")
    st.session_state.upwork_link = st.text_input("1. Job Link or Title:", value=st.session_state.upwork_link, placeholder="e.g., Python Streamlit Project...")
    st.session_state.upwork_client = st.text_input("2. Client's Name (If known):", value=st.session_state.upwork_client, placeholder="e.g., John Doe...")
    st.session_state.upwork_skills = st.text_input("3. Your Skills & Experience:", value=st.session_state.upwork_skills, placeholder="e.g., UI/UX Builder, 2 years Python...")
    st.session_state.upwork_budget = st.text_input("4. Proposed Budget ($):", value=st.session_state.upwork_budget, placeholder="e.g., $250...")
    if st.session_state.upwork_link or st.session_state.upwork_client or st.session_state.upwork_skills or st.session_state.upwork_budget:
        st.session_state.template_text = f"Generate Upwork Proposal for {st.session_state.upwork_link} targeting client {st.session_state.upwork_client}. My skills: {st.session_state.upwork_skills}. Budget: {st.session_state.upwork_budget}."
        st.write("---")
        user_prompt = st.text_area("Final Prompt Dashboard",value=st.session_state.template_text,placeholder="Select a template from the sidebar or fill the inputs above...",height=100)
# --- ✨ ƏSL SƏTİRLƏRƏ BÖLÜNMÜŞ IF-ELSE MƏNTİQİ ---
if st.button("Generate Text ✨", use_container_width=True):
    if st.session_state.active_template == "upwork":
        c_name = st.session_state.upwork_client if st.session_state.upwork_client else 'Client'
        j_link = st.session_state.upwork_link if st.session_state.upwork_link else 'Web Development'
        u_skills = st.session_state.upwork_skills if st.session_state.upwork_skills else 'Python Streamlit Developer'
        p_budget = st.session_state.upwork_budget if st.session_state.upwork_budget else '$150'
        st.session_state.generated_result = f"""Dear {c_name},
        I am writing to express my strong interest in your project: {j_link}.
        With my solid expertise as a {u_skills}, I am confident that I can deliver a high-quality dashboard tailored exactly to your needs. I have analyzed your requirements and my proposed budget for this milestone is {p_budget}.
        Looking forward to working with you!
        Best regards,Professional Freelancer"""
    else:
        st.session_state.generated_result = f"""[AI Premium Generation Result]
        Selected Blueprint: 
        {st.session_state.active_template if st.session_state.active_template else 'General Template'}
        Selected Tone of Voice: {selected_tone}
        This customized copy has been fully generated based on your dashboard query: "{user_prompt}". It is optimized for conversion and matches the industry gold standards. System is ready for official production!"""
        if st.session_state.generated_result:
            st.write("---")
            st.write("### ✨ AI Generated Result")
            final_output = st.text_area("✍️ Edit your result here:",
             value=st.session_state.generated_result, height=200)
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("📋 Copy to Clipboard", use_container_width=True):st.success("Copied to clipboard successfully!")
                with col2:
                    if st.button("🔄 Regenerate", use_container_width=True):st.info("Refreshing AI engine... Text regenerated!")
                    with col3:
                        st.download_button(label="📄 Export (TXT/DOCX)",data=final_output,file_name="copyai_pro_output.txt",mime="text/plain",use_container_width=True)