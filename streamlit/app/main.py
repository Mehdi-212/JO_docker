import psycopg2
import pandas as pd
import streamlit as st

st.title("requete sql")

conn = psycopg2.connect(
    dbname="airflow",
    user="airflow",
    password="airflow",
    host="postgres",
    port="5432"
)

query = st.text_input("Requete", "SELECT * FROM public.data;")

def rekait(query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        if cursor.description:
            result = cursor.fetchall()
            df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])
            st.dataframe(df)
        conn.commit()
        cursor.close()
    except Exception as e:
        st.error(f"Error: {e}")

if st.button("Run requete"):
    rekait(query)

if st.button("delete la db"):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM data;
        DELETE FROM file_name;
    """)
    conn.commit()
    cursor.close()
    st.write("la db est delete")
