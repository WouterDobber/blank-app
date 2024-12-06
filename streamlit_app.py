import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Sidebar button
if st.sidebar.button("README"):
    with st.sidebar:
        st.write("### README")
        st.write("Here is some random text to display when the button is clicked!")
