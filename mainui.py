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

title_container = st.container()
with title_container:
    st.markdown("""
        <div style="text-align: center;">
            <h1>VidyaRANG : Learning Made Easy</h1>
            <p>Upload, Learn, Interact, Assess, and Improve – Your Complete Learning Journey.</p>
        </div>
        """, unsafe_allow_html=True)
     
# Page content based on selected page
if st.session_state.page == "home":

    
    # Center align the title and subtitle container
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.write("")
    search_container = st.container()
    
    # Custom CSS to style the dropdown
    st.markdown("""
        <style>
        /* Change background color of dropdown */
        .stSelectbox div[data-baseweb="select"] > div {
            background-color: white; /* Set background color to white */
            color: black;            /* Text color */
            font-weight: normal;     /* Optional: Set text to normal weight */
        }

        /* Style the dropdown options */
        .stSelectbox div[data-baseweb="select"] ul {
            background-color: white;
            color: black;
        }
        </style>
        """, unsafe_allow_html=True)

    # Layout container for search and button
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])  # Adding empty columns on sides to center-align

        with col2:
            # Center-align dropdown and button by placing them within the same column
            st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
            
            # Dropdown to select course (centered in the middle column)
            selected_course = st.selectbox("Select Course to take quiz", ["Select a course", "History", "Science", "Maths"])
            col1, col2, col3 = st.columns([1, 1, 1]) 
            # Button directly below the selectbox
            with col2:
            # Center-align dropdown and button by placing them within the same column
                if st.button("Begin Assessment"):
                    st.write(f"Generating Quiz for: {selected_course}")
                
            st.markdown('</div>', unsafe_allow_html=True)

    # Center align the popular topics section (if you want to add it below)
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

    
    # Introduction Section
    st.header("About the Product")
    st.write("""
    Welcome to VidyaRANG, your smart companion for learning! VidyaRANG is an AI-powered educational platform designed to make studying simpler, more interactive, and engaging. With VidyaRANG, you can easily upload your study materials, chat directly with your documents to get instant answers, take quizzes to test your knowledge, and analyze your progress with in-depth feedback. 
    """)
             
    st.write("""Whether you're a student or a lifelong learner, VidyaRANG makes learning easier and more effective. Dive into a personalized learning experience and see how VidyaRANG can help you reach your educational goals with confidence!
    """)

    # Product Features
    st.header("Key Features of VidyaRANG")
    st.markdown("""
    - **Privacy-First Document Sharing:** Your uploaded documents are secure and private to you, and you have the control to share them only with assigned users. 
    - **Interactive Chat with YouTube Educational Videos:** Expand your learning with our video chat feature.
    - **Diverse Quizzes: Factual, Memory, and Reasoning:** Take a variety of quizzes designed to test different types of knowledge.
    - **Comprehensive Evaluation and Analytics:** Understand your progress better with in-depth evaluations and analytics.
    """)

    # Demo Section
    st.header("VidyaRANG Demo")
    st.write("Discover VidyaRANG in action – watch our demo to see how you can transform your learning journey with AI-powered insights, interactive quizzes, and personalized document interactions!")

    # Embed YouTube videos
    st.video("https://youtu.be/9ttvfEUE5RI?si=fG95m4SRGF98M9Fl")  # Replace with actual video link
    st.video("https://youtu.be/bai3ngmbheo?si=u4H0GON1S-SmMKAV")  # Replace with actual video link

    # Team Members Section
    st.header("Meet the Team")

    # Display team members' details with images
    team_members = [
        {"name": "Alice Johnson", "role": "CEO", "bio": "Alice is a visionary leader with a passion for AI.", "image": "https://via.placeholder.com/150"},
        {"name": "Bob Smith", "role": "CTO", "bio": "Bob is the mastermind behind the technology.", "image": "https://via.placeholder.com/150"},
        {"name": "Claire Davis", "role": "Lead Data Scientist", "bio": "Claire brings expertise in machine learning.", "image": "https://via.placeholder.com/150"},
        {"name": "David Brown", "role": "Product Manager", "bio": "David ensures that the product meets customer needs.", "image": "https://via.placeholder.com/150"}
    ]

    cols = st.columns(len(team_members))
    for i, member in enumerate(team_members):
        with cols[i]:
            st.image(member["image"], width=150)
            st.subheader(member["name"])
            st.write(f"*{member['role']}*")
            st.write(member["bio"])

    # Contact Section
    st.header("Get in Touch")
    st.write("""
    For more information about our product, please contact us at:
    - **Email:** [contact@ourproduct.com](mailto:contact@ourproduct.com)
    - **Support:** [support@ourproduct.com](mailto:support@ourproduct.com)
    """)

    st.write("Stay connected with us on our journey to make AI accessible to everyone!")

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
