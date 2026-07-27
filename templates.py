import streamlit as st
# -----------------------------
# GENERATED RESULT
# -----------------------------
def show_result():
    if "generated_text" not in st.session_state:
        st.session_state.generated_text = ""

    if st.session_state.generated_text != "":

        st.write("---")
    st.subheader("📄 Generated Result")

    st.text_area(
        "AI Output",
        value=st.session_state.generated_text,
        height=300
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📋 Copy", use_container_width=True):
            st.success("Text copied!")

    with col2:
        if st.button("✏️ Edit", use_container_width=True):
            st.info("Edit mode will be available soon.")

    with col3:
        if st.button("🔄 Regenerate", use_container_width=True):
            st.info("Generating a new version...")