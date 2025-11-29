import streamlit as st
import mysql.connector

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

def insert_query(mail_id, mobile_number, query_heading, query_description):
    query = "INSERT INTO queries (mail_id, mobile_number, query_heading, query_description, status)VALUES (%s,%s,%s,%s,'Open')"
    cursor.execute(query, (mail_id, mobile_number, query_heading, query_description))
    conn.commit()

# ---------------------- # Client page ----------------------------------

st.title("Client Query Submission")

st.subheader("Enter Your Query")

mail_id = st.text_input("Email ID")
mobile_number = st.text_input("Mobile Number")
query_heading = st.text_input("Query Heading")
query_description = st.text_area("Query Description")

if st.button("Submit Query"):
    if mail_id and query_heading and query_description:
        insert_query(mail_id, mobile_number, query_heading, query_description)

        st.success("Your query has been submitted!")

        st.subheader("Submitted Data")
        st.write("**Email:**", mail_id)
        st.write("**Mobile:**", mobile_number)
        st.write("**Heading:**", query_heading)
        st.write("**Description:**", query_description)

    else:
        st.error("Please fill required fields.")

   
