import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(page_title="VidyaRANG : Learning Made Easy", page_icon=":rocket:", layout="wide")

# Initialize session state for page navigation if not already set
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function to switch pages by setting session state
def switch_page(page_name):
    st.session_state.page = page_name

st.title("VidyaRANG : Learning Made Easy")

# Sidebar with navigation buttons
with st.sidebar:
    st.header("Navigation")
    if st.button("Home"):
        switch_page("home")
    
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
            "[View Analytics - History](#)",  # Link for History
            "[View Analytics - Science](#)",  # Link for Science
            "[View Analytics - Maths](#)"     # Link for Maths
        ]
    }
    df = pd.DataFrame(data)

    # Display the DataFrame as a markdown table to enable links
    st.markdown(df.to_markdown(index=False), unsafe_allow_html=True)

# Check for the link clicked in the table and update session state accordingly
# Check the URL parameter and update session state if needed
if "View Analytics - History" in st.session_state.page:
    st.session_state.page = "analytics1"

elif "View Analytics - Science" in st.session_state.page:
    st.session_state.page = "analytics2"

elif "View Analytics - Maths" in st.session_state.page:
    st.session_state.page = "analytics3"

# Page content based on selected page
if st.session_state.page == "home":

    
    # Center align the title and subtitle container
    title_container = st.container()
    with title_container:
        st.markdown("""
            <div style="text-align: center;">
                <h1>Next Level AI Tutoring</h1>
                <p>Create a custom learning pathway to help you achieve more in school, work, and life.</p>
            </div>
            """, unsafe_allow_html=True)

    # Center align the search bar and generate course button container
    search_container = st.container()
    with search_container:
        st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
        search_term = st.text_input("Select Course to take quiz", key="search_input", label_visibility="collapsed")
        if st.button("Evaluate Yourself"):
            st.write(f"Generating Quiz for: {search_term}")
            # Add your course generation logic here
        st.markdown('</div>', unsafe_allow_html=True)

    # Center align the popular topics section
    topics_container = st.container()
    with topics_container:
        st.markdown("""
            <div style="text-align: center;">
                <h3>Popular Topics:</h3>
                <p>Programming, Walking meditation, How to be happy</p>
            </div>
            """, unsafe_allow_html=True)

    # Add some styling
    st.markdown("""
        <style>
            .stApp {
                background-color: #F0F2F6;
            }
        </style>
        """, unsafe_allow_html=True)

elif st.session_state.page == "about":
    st.header("About Page")
    st.write("This is the About page of the app.")

elif st.session_state.page == "create_course":
    st.header("Create New Course")
    st.write("Here you can create a new course.")

elif st.session_state.page == "chat_course":
    st.header("Chat with Course")
    #st.title("Course Feedback Form")
    
    # Initialize session state for message sent
    if "message_sent" not in st.session_state:
        st.session_state.message_sent = False

    # Course selection dropdown at the top
    course = st.selectbox("Select Course", ["Select a course", "Course 1", "Course 2", "Course 3", "Course 4"])

    # Input message bar
    message = st.text_input("Enter your message:")

    # "Send" button for the message
    if st.button("Send"):
        if course == "Select a course":
            st.warning("Please select a course before sending your message.")
        elif not message:
            st.warning("Please enter a message.")
        else:
            st.success(f"Message sent for {course}!")
            st.write("Your message:", message)
            st.session_state.message_sent = True  # Mark that a message has been sent

    # Feedback slider, visible only after the first message is sent
    if st.session_state.message_sent:
        feedback = st.slider("Rate your experience:", 1, 5, 3)
        if st.button("Submit Rating"):
            st.write("Thank you for your feedback!")
            st.write("Your feedback rating:", feedback)
elif st.session_state.page == "assign_course":
    st.header("Assign Course")
    st.write("Here you can assign courses.")

# Display the content based on selected analytics page
if st.session_state.page == "analytics1":
    st.header("Analytics for History")
    st.write("Detailed analytics for the History course.")

elif st.session_state.page == "analytics2":
    st.header("Analytics for Science")
    st.write("Detailed analytics for the Science course.")

elif st.session_state.page == "analytics3":
    st.header("Analytics for Maths")
    st.write("Detailed analytics for the Maths course.")
