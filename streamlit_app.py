import streamlit as st

# Add custom CSS to position the button at the bottom left
st.markdown(
    """
    <style>
    .custom-button {
        position: fixed;
        bottom: 10px;
        left: 10px;
        z-index: 9999;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the button
if st.button("README", key="readme"):
    st.session_state["show_modal"] = True
else:
    st.session_state["show_modal"] = False

# If the button is pressed, show a modal window
if st.session_state.get("show_modal", False):
    st.write("""
    **Modal Window:**
    Here is some random text to display when the button is clicked!
    """)

