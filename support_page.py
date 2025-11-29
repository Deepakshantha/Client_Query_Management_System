import streamlit as st
import mysql.connector
from datetime import datetime
import plotly.express as px
import pandas as pd

# --------------------- MySQL CONNECTION --------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="241513",
    database="client_query_db"
)
cursor = conn.cursor(dictionary=True)

# ---------------------- sidebar removed ----------------------------------

st.set_page_config(initial_sidebar_state="collapsed")

hide_sidebar = """
<style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stSidebarNav"] {display: none;}
</style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)


# --------------------- DB FUNCTIONS ------------------------------
def get_queries(filter_status):
    if filter_status == "All":
        cursor.execute("SELECT * FROM queries ORDER BY query_created_time DESC")
    else:
        cursor.execute("SELECT * FROM queries WHERE status=%s ORDER BY query_created_time DESC", (filter_status,))
    return cursor.fetchall()


def close_query(query_id):
    close_time = datetime.now()
    query = """
        UPDATE queries 
        SET status='Closed', query_closed_time=%s
        WHERE query_id=%s
    """
    cursor.execute(query, (close_time, query_id))
    conn.commit()


# --------------------- STREAMLIT UI -------------------------------
st.title("Support Team - Query Management")

st.subheader("View & Manage Client Queries")

# ---------------------- FILTER SECTION ----------------------------
filter_choice = st.selectbox("Filter by Status", ["All", "Open", "Closed"])

queries = get_queries(filter_choice)

# ---------------------- DISPLAY RESULTS ---------------------------
if not queries:
    st.info("No queries available.")
else:
    for q in queries:
        with st.expander(f"Query #{q['query_id']} - {q['query_heading']}  | Status: {q['status']}"):
            
            st.write("**Email:**", q['mail_id'])
            st.write("**Mobile:**", q['mobile_number'])
            st.write("**Description:**", q['query_description'])
            st.write("**Created At:**", q['query_created_time'])
            st.write("**Closed At:**", q['query_closed_time'])

            # Show Close Button only if status is OPEN
            if q['status'] == "Open":
                if st.button(f"Close Query #{q['query_id']}", key=q['query_id']):
                    close_query(q['query_id'])
                    st.success(f"Query #{q['query_id']} has been closed.")
                    st.rerun()


# --------------------- plot ----------------------

query = "SELECT query_id, status FROM queries"
df = pd.read_sql(query, conn)

fig = px.line(df, x="status", y="query_id", title="Query Trend")
st.plotly_chart(fig)
