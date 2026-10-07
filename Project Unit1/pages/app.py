import streamlit as st

st.set_page_config(
    page_title="Tarhal",
    layout="wide"
)

# Load CSS
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# Store registration data
if "user" not in st.session_state:
    st.session_state.user = {}


# Control the current page
if "page" not in st.session_state:
    st.session_state.page = "Login"


col1, col2 = st.columns([1,0.60])


# =========================
# LEFT SIDE
# =========================

with col1:

    st.image("Images/IMG.jpeg", use_container_width=True)

    st.markdown(
        """
        <div class="left-content">
            <p class="small-text">MADE FOR SAUDI ADVENTURES</p>
            <h1>Every journey<br>begins with <i>wonder.</i></h1>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================
# RIGHT SIDE
# =========================

with col2:

    if st.session_state.page == "Login":
        st.markdown(
            """
            <div class="welcome-text">
                <p class="welcome-small">WELCOME TO TARHAL</p>
                <h2>Welcome back</h2>
                <p>Sign in to continue planning your next Saudi adventure.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div class="welcome-text">
                <p class="welcome-small">WELCOME TO TARHAL</p>
                <h2>Create your account</h2>
                <p>Join Tarhal and start planning memorable trips across the Kingdom.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


    # =========================
    # LOGIN
    # =========================

    if st.session_state.page == "Login":

        username = st.text_input(
            "Uername",
            key="login_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        


        if st.button("Login →"):

            if (
                username == st.session_state.user.get("username")
                and password == st.session_state.user.get("password")
            ):
                st.success("Login successful!")
                st.switch_page("pages/Explore.py")

            else:
                st.error("Invalid username or password")


        st.markdown(
            '<p class="account-text">New to Tarhal?</p>',
            unsafe_allow_html=True
        )


        with st.container(key="create-account"):

            if st.button("Create an account"):

                st.session_state.page = "Register"
                st.rerun()


    # =========================
    # REGISTER
    # =========================

    elif st.session_state.page == "Register":

        email = st.text_input(
            "Email address",
            key="register_email"
        )

        username = st.text_input(
            "Username",
            key="register_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="register_password"
        )


        if st.button("Create account →"):

            if "@" not in email or not email.endswith(".com"):

                st.error("Invalid email")

            elif not username:

                st.warning("Please enter a username")

            elif len(password) < 8:

                st.warning(
                    "Password must be at least 8 characters"
                )

            else:

                st.session_state.user = {
                    "email": email,
                    "username": username,
                    "password": password
                }

                st.success("Registration successful!")

                st.session_state.page = "Login"
                st.rerun()


        st.markdown(
            '<p class="account-text">Already have an account?</p>',
            unsafe_allow_html=True
        )


        with st.container(key="login-account"):

            if st.button("Login"):

                st.session_state.page = "Login"
                st.rerun()

            