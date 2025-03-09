import streamlit as st

# Set the page title
st.set_page_config(page_title="Homepage", page_icon="🏠", layout="wide", initial_sidebar_state="collapsed")

# Add custom CSS to center everything and control width
st.markdown("""
    <style>
        /* Set background color for the whole page */
        body{
            background-color: #f0f8ff; /* Light blue background color */
            font-size: 20px; /* Custom font size */
            color: #FF6347; /* Tomato color */
            font-weight: bold; /* Make the title bold */
            font-family: 'Arial', sans-serif; /* Custom font family */
            text-align: center; /* Center the text */
        }

        /* Banner image style */
        .banner-image {
            width: 100%; /* Make the image span the full width of the screen */
            height: auto; /* Maintain the aspect ratio */
        }

        /* Container to center content and control width */
        .centered {
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: center;
            padding-top: 50px;
            text-align: center;
            max-width: 1000px; /* Control the maximum width */
            margin: 0 auto; /* Center the content horizontally */
        }

        /* Style for the title */
        .custom-title {
            font-size: 64px  !important; /* Custom font size */
            font-weight: bold; /* Make the title bold */
            font-family: 'Arial', sans-serif; /* Custom font family */
            text-align: center; /* Center the text */
            color: #28282B; /* Font color for the title */
            margin-bottom: 30px !important;
            margin-top: 30px !important;
        } 

        .tricolour {
            color: #4285F4; /* Color for "Tricolour" */
        }

        .savings {
            color: #EA4335; /* Color for "Savings" */
        }

        .copyright {
            color: #FDCE0F; /* Color for "copyright symbol" */
        }

        .custom-h2 {
            font-size: 20px; /* Custom font size */
            color: #4285F4  !important; /* Tomato color */
            font-weight: bold; /* Make the title bold */
            font-family: 'Arial', sans-serif; /* Custom font family */
            text-align: center  !important; /* Center the text */
            padding-top: 30px !important;  /* Adjust padding for better spacing */
            padding-left: 20px  !important;
        }

        /* Custom styling for the username and password input fields box (container) */
        .stTextInput > div {
            width: 100%;  /* Set the width to 100% of the container */
            max-width: 400px;  /* Control the max-width of the input box */
            padding: 10px;  /* Adjust padding for better spacing */
            margin: 0 auto;  /* Center the input field */
        }

        /* Center-align text inside input fields */
        .stTextInput input {
            text-align: left; /* Align text to the left inside the input field */
            font-size: 18px;  /* Adjust font size for better readability */
            padding: 10px;  /* Add padding */
        }

        /* Center-align the labels above the input fields */
        .stTextInput label {
            display: block; /* Make label a block element so it takes up full width */
            text-align: center; /* Center the label */
            font-size: 24px !important;  /* Adjust font size for better readability */
            padding: 10px;  /* Add padding */
            margin-bottom: 5px;  /* Add a bit of space below the label */
        }

        /* Style for the buttons */
        .stButton button {
            background-color: #4285F4; /* Tomato background color */
            color: white; /* White text color */
            border: none; /* Remove the default border */
            border-radius: 5px; /* Round the corners of the button */
            padding: 7px 40px; /* Add padding to make the button bigger */
            font-size: 18px; /* Increase font size */
            cursor: pointer; /* Change cursor to a pointer on hover */
            transition: background-color 0.3s ease; /* Smooth transition on hover */
            margin-top: 20px; /* Add space above the button */
        }

        /* Button hover effect */
        .stButton button:hover {
            background-color: #EA4335; /* Darker red when hovered */
            color: white; /* White text color */
        }
    </style>
""", unsafe_allow_html=True)

# Function to authenticate user
def authenticate(username, password):
    correct_username = "iluvhackher"
    correct_password = "12345678"
    
    if username == correct_username and password == correct_password:
        return True
    else:
        return False

# Add the banner image
st.image("/Users/amvm/HackHer/hackHer tricolour savings banner.png", use_container_width=True)


# Create a container and apply the centered style
with st.container():
    
    # Add a title with custom CSS using st.markdown and HTML
    st.markdown("""
        <h1 class="custom-title">
            welcome to <span class="tricolour">tricolour</span> <span class="savings">savings</span><span class="copyright"> ©</span>!
        </h1>
    """, unsafe_allow_html=True)
    
    # Create a login form
    st.markdown('<h3 class="custom-h2">please log in</h3>', unsafe_allow_html=True)
    username = st.text_input("username")
    password = st.text_input("student ID", type="password")

    # Check if the user has submitted the login form
    if st.button("login"):
        if authenticate(username, password):
            st.success("Login successful!")
            st.switch_page("pages/main.py")
        else:
            st.error("Incorrect username or password. Please try again.")


    # Custom HTML content
    st.markdown("""
        <style>
            .big-font {
                font-size:24px !important;
                color: #EA4335;
                padding-top: 30px;
            }
        </style>
        <p class="big-font">save more, stress less.</p>
    """, unsafe_allow_html=True)

    # Footer Section
    st.markdown("---")
    st.write("created by Amelie, Gertrudis, Shillisa, Katrina.")
