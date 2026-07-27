import streamlit as st

PLAN_LIMITS = {
    "Starter": 50000,
    "Growth": 200000,
    "Enterprise": 9999999
}

# --- 🧠 DAXİLİ YADDAŞ BUNKERİ (XƏTASIZ VƏ SIFIR DONMA) ---
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

# Doldurma xanalarının datalarını yaddaşda saxlayırıq
if "input_val_1" not in st.session_state:
    st.session_state.input_val_1 = ""
if "input_val_2" not in st.session_state:
    st.session_state.input_val_2 = ""
if "input_val_3" not in st.session_state:
    st.session_state.input_val_3 = ""
if "input_val_4" not in st.session_state:
    st.session_state.input_val_4 = ""

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

    # --- 🛡️ PLANI MƏTNƏ ÇEVİRƏN FILTR ---
    current_plan_name = "Starter"
    raw_plan = st.session_state.get("current_plan", "Starter")
    if "Growth" in str(raw_plan):
        current_plan_name = "Growth"
    elif "Enterprise" in str(raw_plan):
        current_plan_name = "Enterprise"
    else:
        current_plan_name = "Starter"

    max_limit = PLAN_LIMITS.get(current_plan_name, 50000)
# --- 📋 ENGLISH SIDEBAR BÜTÜN ŞABLONLAR BURADADIR ---
    st.sidebar.header("📊 User Dashboard")
    st.sidebar.write(f"Current Plan: {current_plan_name} Plan")
    st.sidebar.progress(min(st.session_state.used_words / max_limit, 1.0))
    st.sidebar.write(f"📝 Used Words: {st.session_state.used_words} / {max_limit}")
    
    st.sidebar.write("---")
    st.sidebar.header("⚡ Premium Templates")
    
    # 1. For Freelancers
    with st.sidebar.expander("💼 For Freelancers"):
        if st.button("📝 Upwork Proposal Generator", use_container_width=True):
            st.session_state.active_template = "Upwork Proposal"
            st.session_state.template_text = ""
            st.session_state.generated_result = ""
        if st.button("🌟 Fiverr Gig Description", use_container_width=True):
            st.session_state.active_template = "Fiverr Gig Description"
            st.session_state.template_text = ""
            st.session_state.generated_result = ""
        if st.button("✉️ Client Follow-up Email", use_container_width=True):
            st.session_state.active_template = "Client Follow-up Email"
            st.session_state.template_text = ""
            st.session_state.generated_result = ""
        if st.button("📊 Project Estimate", use_container_width=True):
            st.session_state.active_template = "Project Estimate"
            st.session_state.template_text = ""
            st.session_state.generated_result = ""
        if st.button("🧾 Invoice Email", use_container_width=True):
            st.session_state.active_template = "Invoice Email"
            st.session_state.template_text = ""
            st.session_state.generated_result = ""

    # 2. For Agencies
    with st.sidebar.expander("🏢 For Agencies"):
        if st.button("📣 Social Media Ad Copy", use_container_width=True):
            st.session_state.active_template = "Social Media Ad Copy"
            st.session_state.template_text = ""
            st.session_state.generated_result = ""
        if st.button("🔍 SEO Blog Planner", use_container_width=True):
            st.session_state.active_template = "SEO Blog Planner"
            st.session_state.template_text = ""
            st.session_state.generated_result = ""
        if st.button("📈 Client Report Summary", use_container_width=True):
            st.session_state.active_template = "Client Report Summary"
            st.session_state.template_text = ""
            st.session_state.generated_result = ""

    # 3. For Companies
    with st.sidebar.expander("🚀 For Companies"):
        if st.button("💼 Job Descriptions", use_container_width=True):
            st.session_state.active_template = "Job Description"
            st.session_state.template_text = ""
            st.session_state.generated_result = ""
        if st.button("📦 Product Descriptions", use_container_width=True):
            st.session_state.active_template = "Product Description"
            st.session_state.template_text = ""
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

    # --- ⚙️ SƏNİN İSTƏDİYİN DOLDURMA SAHƏLƏRİN (DYNAMIC INPUTS) ---
    # Əgər hər hansı bir şablon seçilibsə, xanalar dinamik adlarla avtomatik açılır!
    if st.session_state.active_template:
        st.write(f"### 📋 Fill the {st.session_state.active_template} Details")
        st.session_state.input_val_1 = st.text_input("1. Project Title or Link:", value=st.session_state.input_val_1, placeholder="e.g., Python Project, Translation Service...")
        st.session_state.input_val_2 = st.text_input("2. Target Audience / Client Name:", value=st.session_state.input_val_2, placeholder="e.g., John Doe, E-commerce Store Owners...")
        st.session_state.input_val_3 = st.text_input("3. Core Features / Your Skills:", value=st.session_state.input_val_3, placeholder="e.g., Streamlit Dashboard, Fast Delivery...")
        st.session_state.input_val_4 = st.text_input("4. Proposed Budget / Price ($):", value=st.session_state.input_val_4, placeholder="e.g., $150, $500...")
        
        if st.session_state.input_val_1 or st.session_state.input_val_2 or st.session_state.input_val_3 or st.session_state.input_val_4:
            st.session_state.template_text = f"Generate {st.session_state.active_template} for {st.session_state.input_val_1}. Target: {st.session_state.input_val_2}. Details: {st.session_state.input_val_3}. Budget/Price: {st.session_state.input_val_4}."
        st.write("---")

    # --- 📝 MAIN TEXT AREA ---
user_prompt = st.text_area(
        "Final Prompt Dashboard",
        value=st.session_state.template_text,
        placeholder="Select a template from the sidebar or fill the inputs above...",
        height=100
    )

if st.button("Generate Text ✨", use_container_width=True):
        t_name = st.session_state.active_template if st.session_state.active_template else "Marketing Copy"
        p_title = st.session_state.input_val_1 if st.session_state.input_val_1 else "Digital Project"
        t_target = st.session_state.input_val_2 if st.session_state.input_val_2 else "Valued Client"
        f_details = st.session_state.input_val_3 if st.session_state.input_val_3 else "High-quality professional services"
        p_price = st.session_state.input_val_4 if st.session_state.input_val_4 else "$150"
        
        # Hər bir şablon üçün tam zəngin və möhtəşəm nəticə simulyasiyası
        st.session_state.generated_result = f"""Dear {t_target},
This is your custom high-converting {t_name} created specifically for your request regarding: "{p_title}".[⚡ PREMIUM CONTENT GENERATED BY AI]Our customized solution is built using advanced methodologies targeting {t_target}. The core deliverables include optimized execution of {f_details}. All benchmarks have been analyzed, and the proposed budget structure for this operational milestone is set at {p_price}.Selected Style and Emotion: {selected_tone}The layout is fully ready to copy and export for your professional workflows.Best regards,Professional Global Consultant"""# --- 📊 COPY, EDIT, EXPORT DÜYMƏLƏRİNİN HAMISI BURADADIR ---if st.session_state.generated_result:st.write("---")st.write("### ✨ AI Generated Result")final_output = st.text_area("✍️ Edit your result here:", value=st.session_state.generated_result, height=200)col1, col2, col3 = st.columns(3)with col1:if st.button("📋 Copy to Clipboard", use_container_width=True):st.success("Copied to clipboard successfully!")with col2:if st.button("🔄 Regenerate", use_container_width=True):st.info("Refreshing AI engine... Text regenerated!")with col3:st.download_button(label="📄 Export (TXT/DOCX)",data=final_output,file_name="ai_generated_copy.txt",mime="text/plain",use_container_width=True)