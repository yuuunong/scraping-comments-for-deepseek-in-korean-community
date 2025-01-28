import logging
import streamlit as st
from sqlalchemy import text

@st.cache_resource
def get_connector():
    return st.connection('scraping_comments_for_deepseek_db', type='sql', autocommit=True)


#def create_table():
#   query = '''
#    use scraping_comments_for_deepseek;
#    
#    create table comments_fmkorea(
#        title varchar,
#        comment varchar)
#    ;
#    '''
'''
def insert_query(sql_constant:INSERT_SQLs, datas:list) -> list:
    conn = get_connector()
    list_error = []
    logging.info(f"[insert_query] len(datas): {len(datas)}")

    for idx, data in enumerate(datas):
        try:
            
            logging.info(f"[insert_query] len(datas)[idx]: {idx}")
            insert_sql = sql_constant.value[1].format(
                title=data['title'],
                comment=data['comment']
            )
            conn.connect().execute(text(insert_sql))
        except Exception as e:
            
            data['error'] = str(e)
            list_error.append(data)
    
    return list_error
'''