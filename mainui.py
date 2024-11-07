import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streamlit Multi-Page App", page_icon=":rocket:", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "home"

def switch_page(page_name):
    st.session_state.page = page_name

st.title("VidyaRANG : Learning Made Easy")

with st.sidebar:
    st.header("Navigation")
    if st.button("Home"):
        switch_page("home")
    if st.button("Settings"):
        switch_page("settings")
    if st.button("About"):
        switch_page("about")

    st.subheader("Choose Action")
    # Replace selectbox with buttons for different actions
    if st.button("Create New Course"):
        switch_page("create_course")
    if st.button("Chat with Course"):
        st.session_state.page = "chat_course"
    if st.button("Assign Course"):
        st.session_state.page = "assign_course"

    st.subheader("Learner's Performance")
    # Display courses with analytics links in a table format
    data = {
        "Course Name": ["History", "Science", "Maths"],
        "Analytics": [
            "[View Analytics](#)",  # Link placeholder
            "[View Analytics](#)",  # Link placeholder
            "[View Analytics](#)"   # Link placeholder
        ]
    }
    df = pd.DataFrame(data)

    st.write("Courses Created by USER:")
    # Display the DataFrame as a markdown table to enable links
    st.markdown(df.to_markdown(index=False), unsafe_allow_html=True)

# Page content based on selected page
if st.session_state.page == "home":
    st.header("Home Page")
    st.write("Welcome to the Home page!")

elif st.session_state.page == "settings":
    st.header("Settings Page")
    st.write("Configure your app settings here.")

elif st.session_state.page == "about":
    st.header("About Page")
    st.write("This is the About page of the app.")

elif st.session_state.page == "create_course":
    st.header("Create New Course")
    st.write("Here you can create a new course.")

elif st.session_state.page == "chat_course":
    st.header("Chat with Course")
    st.write("Here you can interact with a course.")

elif st.session_state.page == "assign_course":
    st.header("Assign Course")
    st.write("Here you can assign courses.")

elif st.session_state.page == "analytics1":
    st.header("Analytics for History")
    st.write("Detailed analytics for the History course.")

elif st.session_state.page == "analytics2":
    st.header("Analytics for Science")
    st.write("Detailed analytics for the Science course.")

elif st.session_state.page == "analytics3":
    st.header("Analytics for Maths")
    st.write("Detailed analytics for the Maths course.")
