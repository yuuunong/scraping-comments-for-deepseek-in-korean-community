import streamlit as st
from sqlalchemy import text

@st.cache_resource
def get_connector():
    return st.connection('scraping_comments_for_deepseek_db', type='sql', autocommit=True)


def insert_data_to_mysql(p_comments: list, p_community:str):
    conn = get_connector()

    for i in p_comments:
        query = f"insert into comments_{p_community} (title, comment, gallery, date_) values ('{i['title']}', '{i['comment']}', '{i['gallery']}', '{i['date_']}')"
        conn.session.execute(text(query))
        conn.session.commit()

