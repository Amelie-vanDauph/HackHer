import streamlit as st
from PIL import Image

def main():
    # Create two columns for the header (title)
    col1, col2 = st.columns([1, 4])  # Adjust column ratio for the title

    # Display the title in the second column with the specified colors and lowercase
    col2.markdown(
        """
        <style>
        .header {
            text-align: left;
            font-size: 3em;
            font-weight: bold;
        }
        .tricolour {
            color: #4285F4;
        }
        .savings {
            color: #EA4335;
        }
        .copyright {
            color: #FDCE0F;
            font-size: 1em;  /* Smaller copyright symbol */
            vertical-align: bottom; /* Aligns copyright symbol towards the bottom */
            margin-left: 5px; /* Slight margin to separate copyright from the word "savings" */
        }
        .lowercase {
            text-transform: lowercase;
        }
        .image-container {
            width: 100%;
            height: 300px; /* Fixed height for the image box */
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden; /* Prevents overflow if image is larger */
        }
        .image-container img {
            width: 100%;
            height: 100%;
            object-fit: contain; /* Ensures images maintain their aspect ratio and fit within the box */
        }
        </style>
        <div class="header">
            <span class="tricolour lowercase">tricolour</span> 
            <span class="savings lowercase">savings</span> 
            <span class="copyright lowercase">©</span>
        </div>
        """, unsafe_allow_html=True
    )

    # Create a new row for the logo and selection bar
    col1, col2 = st.columns([1, 4])  # Create two columns for logo and selection bar

    # Display the logo in the first column
    try:
        logo = Image.open("logo_no_words.png")  # Ensure the logo.png is in the same directory
        col1.image(logo, width=100)  # Adjust the width to double the size of the logo
    except Exception as e:
        st.error(f"Error loading image: {e}")  # Display an error message if the image doesn't load

    # Course selection box in the second column
    with col2:
        option = course_search()

    # Show found options based on the course selected
    if option == "math 110":
        found_options(
            f"{option}", 
            ("cat1.jpg", f"{option} second-hand textbook", "$24", "mcccalllietan", "highlighted already so price lower"),
            ("cat5.jpg", f"{option} calculator", "$19", "carrieetwoooo", "almost new condition!"),
            ("cat3.jpg", f"{option} workbook", "$18", "mahima_pasn0r", "minor wear, great deal!")
        )
    elif option == "stat 263":
        found_options(
            f"{option}", 
            ("cat7.jpg", f"{option} textbook", "$22", "stellaguest1", "well-used, but still good condition"),
            ("cat8.jpg", f"{option} coursebook", "$21", "kelvinn", "barely used, like new"),
            ("cat9.jpg", f"{option} calculator", "$15", "amb3r33", "calculator 115s in excellent condition")
        )
    elif option == "cisc 102":
        found_options(
            f"{option}", 
            ("cat4.jpg", f"{option} textbook", "$22", "liam34noble", "good condition, some highlights"),
            ("cat2.jpg", f"{option} calculator", "$18", "cindyph4m", "in perfect condition"),
            ("cat6.jpg", f"{option} supplies", "$20", "laura678", "used but fully functional")
        )


def course_search():
    # Display a dropdown for selecting a course and make it lowercase
    option = st.selectbox(
        "what course are you looking for supplies for?",
        ("math 110", "stat 263", "cisc 102"),
        index=None,
        placeholder="select course:",
    )
    
    # Replace None with "none" in lowercase
    if option is None:
        option = "none"
    
    st.write(f"you selected: {option.lower()}")  # Show selected course in lowercase
    return option.lower()  # Return the selected course in lowercase


def found_options(course, option_1, option_2, option_3):
    # Display 3 options in 3 columns based on selected course
    left, middle, right = st.columns(3, gap="medium")

    # Option 1: image for the selected course
    left.markdown(f"**option 1 for {course}**")
    left.image(option_1[0], caption=option_1[1], use_container_width=True)
    left.markdown(f"### {option_1[1]}")
    left.markdown(f"**price:** {option_1[2]}")
    left.markdown(f"**username:** {option_1[3]}")
    left.markdown(f"**description:** {option_1[4]}")
    
    # Message seller button for option 1
    if left.button("message seller", key="msg_1", use_container_width=True):
        left.markdown(f"you can now message the seller: {option_1[3]}")

    # Option 2: image for the selected course
    middle.markdown(f"**option 2 for {course}**")
    middle.image(option_2[0], caption=option_2[1], use_container_width=True)
    middle.markdown(f"### {option_2[1]}")
    middle.markdown(f"**price:** {option_2[2]}")
    middle.markdown(f"**username:** {option_2[3]}")
    middle.markdown(f"**description:** {option_2[4]}")
    
    # Message seller button for option 2
    if middle.button("message seller", key="msg_2", use_container_width=True):
        middle.markdown(f"you can now message the seller: {option_2[3]}")

    # Option 3: image for the selected course
    right.markdown(f"**option 3 for {course}**")
    right.image(option_3[0], caption=option_3[1], use_container_width=True)
    right.markdown(f"###  {option_3[1]}")
    right.markdown(f"**price:** {option_3[2]}")
    right.markdown(f"**username:** {option_3[3]}")
    right.markdown(f"**description:** {option_3[4]}")
    
    # Message seller button for option 3
    if right.button("message seller", key="msg_3", use_container_width=True):
        right.markdown(f"you can now message the seller: {option_3[3]}")

# Run the Streamlit app
main()