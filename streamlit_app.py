import streamlit as st

# Add custom CSS for the button
st.markdown(
    """
    <style>
    .custom-button-container {
        position: fixed;
        bottom: 10px;
        left: 10px;
        z-index: 9999;
    }
    .custom-button {
        background-color: #007BFF;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
    }
    .custom-button:hover {
        background-color: #0056b3;
    }
    </style>
    <div class="custom-button-container">
        <button class="custom-button" onclick="window.open('', '_self')">README</button>
    </div>
    """,
    unsafe_allow_html=True,
)

# Display content when button is clicked
if "show_modal" not in st.session_state:
    st.session_state["show_modal"] = False

if st.button("README", key="readme"):
    st.session_state["show_modal"] = not st.session_state["show_modal"]

if st.session_state["show_modal"]:
    st.write("""
    ### Modal Window
    Here is some random text to display when the button is clicked!
    """)
