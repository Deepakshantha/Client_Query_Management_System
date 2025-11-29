import streamlit as st
import mysql.connector
import hashlib

# ---------------------- MySQL CONNECTION ----------------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="241513",
    database="client_query_db"
)
cursor = conn.cursor()

# ---------------------- sidebar removed ----------------------------------

st.set_page_config(initial_sidebar_state="collapsed")

hide_sidebar = """
<style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stSidebarNav"] {display: none;}
</style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

# ---------------------- Helper Functions ----------------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password, role):
    hashed = hash_password(password)
    query = "INSERT INTO users (username, hashed_password, role) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, hashed, role))
    conn.commit()

def validate_user(username, password):
    hashed = hash_password(password)
    query = "SELECT role FROM users WHERE username=%s AND hashed_password=%s"
    cursor.execute(query, (username, hashed))
    return cursor.fetchone()

# ---------------------- STREAMLIT UI --------------------------------------
st.title("Login System (Client & Support Team)")

menu = ["Login", "Register"]
choice = st.radio("Select Option", menu)

# ---------------------- REGISTER PAGE -------------------------------------
if choice == "Register":
    st.subheader("Create an Account")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")
    role = st.selectbox("Select Role", ["Client", "Support"])

    if st.button("Register"):
        try:
            register_user(new_user, new_pass, role)
            st.success("Account created successfully!")
        except:
            st.error("Username already exists OR MySQL error.")

# ---------------------- LOGIN PAGE ----------------------------------------
elif choice == "Login":
    st.subheader("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        result = validate_user(username, password)

        if result:
            role = result[0]
            st.success(f"Login Successful! Role = {role}")

            # Redirect based on role
            if role == "Client":
                st.switch_page("C:\client_query_management\pages\client_page.py")
            elif role == "Support":
                st.switch_page("C:\client_query_management\pages\support_page.py")

        else:
            st.error("Invalid Login Credentials!")
