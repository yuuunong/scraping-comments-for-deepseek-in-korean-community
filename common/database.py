import logging
import streamlit as st
from sqlalchemy import text
from .sql_constant import INSERT_SQLs

@st.cache_resource
def get_connector():
    return st.connection('scraping_comments_for_deepseek_db', type='sql', autocommit=True)


def insert_query(sql_constant:INSERT_SQLs, datas:list) -> list:
    conn = get_connector()
    list_error = []
    logging.info(f"[insert_query] len(datas): {len(datas)}")