import sqlite3
import streamlit as st

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS mytable (id INT, name TEXT)")
conn.commit()

# --- Input Section ---
st.header("Add New Record")
num = st.number_input("Enter number", step=1)
name = st.text_input("Enter name")

if st.button("Submit"):
    cursor.execute("INSERT INTO mytable (id, name) VALUES (?, ?)", (num, name))
    conn.commit()
    st.success("Data inserted successfully!")

# --- Display Table Section ---
st.header("📋 Records in Database")

cursor.execute("SELECT * FROM mytable")
rows = cursor.fetchall()

if rows:
    st.table(rows)  # You can also use st.dataframe(rows)
else:
    st.info("No records found.")

# Close connection
conn.close()
