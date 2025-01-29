import streamlit as st
from sqlalchemy import text

@st.cache_resource
def get_connector():
    return st.connection('scraping_comments_for_deepseek_db', type='sql', autocommit=True)


def insert_data_to_mysql(p_comments):
    conn = get_connector()

    for i in p_comments:
        try:
            query = """insert into comments_fmkorea (title, comment) values ('{0}', '{1}')""".format(i['title'], i['comment'])
            conn.session.execute(text(query))
            conn.session.commit()
        except:
            st.write('저장실패')
            pass

