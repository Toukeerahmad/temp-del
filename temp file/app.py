import streamlit as st

# --- Helper Functions for Pages ---

def home_page():
    """Defines the content for the Home page."""
    
    # Set the page title and header
    st.title("🏡 Welcome to the Basic Streamlit App")
    st.header("Your Simple Introduction")

    st.markdown("""
    This application demonstrates a simple multi-page structure built within a single Streamlit file. 
    Streamlit makes it incredibly easy to turn data scripts into shareable web applications in minutes.
    
    Use the navigation menu on the left (the sidebar) to switch between the 'Home' introduction and the 'Contact' information page.
    
    ### Core Features of this Demo:
    - **Single File:** All logic is contained in one `streamlit_app.py` file.
    - **Navigation:** Uses `st.sidebar.selectbox` for easy switching.
    - **Clear Layout:** Uses built-in Streamlit elements like `st.title`, `st.header`, and `st.markdown`.
    """)

    st.subheader("What is Streamlit?")
    st.info("Streamlit is an open-source Python library that allows you to create beautiful, custom web apps for data science and machine learning, all in pure Python.")

def contact_page():
    """Defines the content for the Contact page."""
    
    st.title("📞 Get In Touch")
    st.header("Contact Information")

    st.markdown("""
    We're always happy to hear from you! Below are the details for reaching out.
    """)

    # Use columns for a neat layout of contact details
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Email")
        st.write("For general inquiries, please email:")
        st.code("support@example.com")
        
    with col2:
        st.subheader("Social Media")
        st.write("Find us on the following platforms:")
        st.markdown(
            """
            - [Twitter/X](https://twitter.com)
            - [LinkedIn](https://linkedin.com)
            - [GitHub](https://github.com)
            """
        )
        
    st.markdown("---")
    st.write("Thank you for your interest!")


# --- Main Application Logic ---

# 1. Configure the page settings
st.set_page_config(
    page_title="Simple Streamlit App",
    page_icon="✨",
    layout="centered"
)

# 2. Create the navigation menu in the sidebar
PAGES = {
    "Home": home_page,
    "Contact": contact_page
}

st.sidebar.title("App Navigation")
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))

# 3. Display the selected page content
page = PAGES[selection]
page()

# Optional: Add a footer to the sidebar
st.sidebar.markdown("---")
st.sidebar.write("Developed with Streamlit.")
