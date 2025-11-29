import pandas as pd
import mysql.connector
from datetime import datetime

# --------------------- MySQL CONNECTION --------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="241513",
    database="client_query_db"
)
cursor = conn.cursor()

# ---------------------- ISERTING CSV ---------------------------

df = pd.read_csv("C:/Users/ADMIN/Downloads/synthetic_client_queries.csv")

# --------------------- Convert Date Columns -------------------
def convert_to_datetime(date_value):
    if pd.isna(date_value) or date_value == "":
        return None

    return datetime.strptime(date_value, "%m/%d/%Y")  # MM/DD/YYYY

df["date_raised"] = df["date_raised"].apply(convert_to_datetime)
df["date_closed"] = df["date_closed"].apply(convert_to_datetime)

# ---------------- STATUS FIX ----------------
allowed = ["Open", "Closed"]

df["status"] = df["status"].astype(str).str.strip().str.title()
df["status"] = df["status"].apply(
    lambda x: x if x in allowed else "Open"
)

print("CSV Status Values After Cleaning:", df["status"].unique())

# --------------------- Insert into MySQL ----------------------
insert_query = """
INSERT INTO queries (
    mail_id,
    mobile_number,
    query_heading,
    query_description,
    status,
    query_created_time,
    query_closed_time
)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

for index, row in df.iterrows():
    data = (
        row["client_email"],
        row["client_mobile"],
        row["query_heading"],
        row["query_description"],
        row["status"],
        row["date_raised"],     # DATETIME
        row["date_closed"]      # DATETIME or NULL
    )
    cursor.execute(insert_query, data)

conn.commit()
cursor.close()
conn.close()

print("CSV data imported successfully!")


