from templates import show_result
import streamlit as st

st.set_page_config(
    page_title="CopyAI Pro - SaaS",
    page_icon="🚀",
    layout="centered"
)

# -----------------------------
# PLAN LIMITS
# -----------------------------
PLAN_LIMITS = {
    "Starter": 50000,
    "Growth": 200000,
    "Enterprise": 9999999
}

# -----------------------------
# SESSION STATE
# -----------------------------
if "registered_users" not in st.session_state:
    st.session_state.registered_users = {}

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if "current_plan" not in st.session_state:
    st.session_state.current_plan = "Starter"

if "used_words" not in st.session_state:
    st.session_state.used_words = 0

if "template_text" not in st.session_state:
    st.session_state.template_text = ""

if "upwork_mode" not in st.session_state:
    st.session_state.upwork_mode = False

# -----------------------------
# LOGIN / SIGNUP
# -----------------------------
if not st.session_state.is_logged_in:

    st.title("🔐 Welcome to CopyAI Pro")
    st.subheader("Please sign up or log in to access the platform")

    signup_tab, login_tab = st.tabs(
        [
            "🆕 Sign Up (Create Account)",
            "🔑 Log In (Access Account)"
        ]
    )

    # -------------------------
    # SIGN UP
    # -------------------------
    with signup_tab:

        st.write("### Create a New Account")

        new_email = st.text_input(
            "Enter your Email Address",
            key="signup_email"
        )

        new_password = st.text_input(
            "Create a Secure Password",
            type="password",
            key="signup_password"
        )

        st.write("---")

        st.write("### 💳 Select Your Subscription Plan")

        selected_plan = st.radio(
            "Choose a plan:",
            [
                "Starter Plan ($19/mo)",
                "Growth Plan ($49/mo)",
                "Enterprise Plan ($300/mo)"
            ]
        )

        if st.button(
            "Register & Proceed to Payment 💳",
            use_container_width=True
        ):

            if new_email == "" or new_password == "":
                st.warning("Please fill in all fields.")

            elif new_email in st.session_state.registered_users:
                st.error("This email is already registered.")

            else:

                plan_name = selected_plan.split()[0]

                st.session_state.registered_users[new_email] = {
                    "password": new_password,
                    "plan": plan_name
                }

                st.success(
                    "Account created successfully!"
                )

                st.info(
                    "💡 Please switch to 'Log In' tab to access your secure dashboard."
                )

    # -------------------------
    # LOGIN
    # -------------------------
    with login_tab:

        st.write("### Log In to Your Dashboard")

        login_email = st.text_input(
            "Email Address",
            key="login_email"
        )

        login_password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button(
            "Verify & Log In 🚀",
            use_container_width=True
        ):

            if (
                login_email in st.session_state.registered_users
                and
                st.session_state.registered_users[login_email]["password"] == login_password
            ):

                st.session_state.is_logged_in = True

                st.session_state.current_plan = (
                    st.session_state
                    .registered_users[login_email]["plan"]
                )

                st.rerun()

            else:

                st.error(
                    "Invalid email or password."
                )

else:
    st.title("🚀 CopyAI Pro — AI Text Generator")
    st.subheader("Global SaaS Platform for Freelancers & Agencies")

    current_plan_name = st.session_state.current_plan

    if current_plan_name not in PLAN_LIMITS:
        current_plan_name = "Starter"

    # -----------------------------
    # SIDEBAR
    # -----------------------------
    st.sidebar.header("📊 User Dashboard")

    st.sidebar.write(f"Current Plan: {current_plan_name} Plan")

    st.sidebar.progress(
        st.session_state.used_words /
        PLAN_LIMITS[current_plan_name]
    )

    st.sidebar.write(
        f"📝 Used Words: {st.session_state.used_words} / {PLAN_LIMITS[current_plan_name]}"
    )

    st.sidebar.write("---")
    st.sidebar.header("⚡ Premium Templates")

    # -----------------------------
    # FREELANCERS
    # -----------------------------
    with st.sidebar.expander("💼 For Freelancers"):

        if st.button("📝 Upwork Proposal Generator", use_container_width=True):
            st.session_state.upwork_mode = True

        if st.button("🌟 Fiverr Gig Description", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Create an optimized Fiverr gig description."

        if st.button("✉️ Client Follow-up Email", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Write a professional follow-up email."

        if st.button("📊 Project Estimate", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Generate a project estimate."

        if st.button("🧾 Invoice Email", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Write an invoice email."

    # -----------------------------
    # AGENCIES
    # -----------------------------
    with st.sidebar.expander("🏢 For Agencies"):

        if st.button("📣 Social Media Ad Copy", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Write social media ads."

        if st.button("🔍 SEO Blog Planner", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Create an SEO blog plan."

        if st.button("📈 Client Report Summary", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Write a client report."

        if st.button("❄️ Cold Email Campaign", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Write a cold email."

        if st.button("📅 Content Calendar Creator", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Create a content calendar."

    # -----------------------------
    # COMPANIES
    # -----------------------------
    with st.sidebar.expander("🚀 For Companies"):

        if st.button("💼 Job Description", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Write a job description."

        if st.button("📦 Product Description", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Write a product description."

        if st.button("📁 Internal Communication", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Write an internal email."

        if st.button("🎯 Marketing Campaign", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Create a marketing campaign."

        if st.button("🗣️ Brand Voice Manager", use_container_width=True):
            st.session_state.upwork_mode = False
            st.session_state.template_text = "Analyze brand voice."
st.sidebar.write("---")

if st.sidebar.button("Log Out 🚪", use_container_width=True):
        st.session_state.is_logged_in = False
        st.session_state.template_text = ""
        st.session_state.upwork_mode = False
        st.rerun()
        # -----------------------------
    # MAIN PAGE
    # -----------------------------

st.write("### 🗣️ Select Tone of Voice")

selected_tone = st.selectbox(
        "Choose the style and emotion for the AI generation:",
        [
            "Professional 💼",
            "Casual ☕",
            "Witty & Funny ✨",
            "Persuasive & Sales 📈",
            "Bold & Confident 🔥",
            "Empathetic & Friendly ❤️"
        ]
    )

st.write("---")

    # =============================
    # UPWORK TEMPLATE
    # =============================
if st.session_state.upwork_mode:

        st.subheader("💼 Upwork Proposal Generator")

        project_title = st.text_input("Project Title")

        client_problem = st.text_area(
            "Client Job Description"
        )

        required_skills = st.text_input(
            "Required Skills"
        )

        your_experience = st.text_area(
            "Your Experience"
        )

        proposal_tone = st.selectbox(
            "Proposal Tone",
            [
                "Professional",
                "Friendly",
                "Persuasive",
                "Short & Direct"
            ]
        )

        if st.button(
            "Generate Upwork Proposal 🚀",
            use_container_width=True
        ):

            st.session_state.template_text = f"""
Write a {proposal_tone} Upwork proposal.

Project Title:
{project_title}

Client Job Description:
{client_problem}

Required Skills:
{required_skills}

My Experience:
{your_experience}

Create a proposal that focuses on the client's problem and explains why I am the best person for the job.
"""

            st.session_state.upwork_mode = False
            st.rerun()

    # =============================
    # NORMAL AI GENERATOR
    # =============================
else:

        user_prompt = st.text_area(
            "What do you want the AI to write?",
            value=st.session_state.template_text,
            placeholder="Select a template from the sidebar or enter your topic here...",
            height=180
        )

        if st.button(
            "Generate Text ✨",
            use_container_width=True
        ):

            st.info(
                f"🔒 Active Tone: {selected_tone}. OpenAI integration will generate the final content here."
            )
show_result()
