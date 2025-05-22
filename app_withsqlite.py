import sqlite3
import streamlit as st

conn=sqlite3.connect('mydb.db')


cursor=conn.cursor()

# query="create table mytable(id int,name varchar(100))"

# cursor.execute(query)
# conn.commit()

num=st.number_input("enter number")
name=st.text_input("enter name")
if st.button("submit"):
    query="insert into mytable values(?,?)"

    cursor.execute(query,(num,name))
    conn.commit()

    conn.close()