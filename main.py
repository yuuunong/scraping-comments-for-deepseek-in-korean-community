import logging
logging.basicConfig(level=logging.INFO)

import streamlit as st
from common.scraping import get_comments
from common.scraping import connect_fmkorea

import pandas as pd

st.title('fmkorea에서의 deepseek에 대한 반응')



with st.form('st_form'):
    pages = st.text_input('몇 페이지까지 스크래핑 하시겠습니까?: ')
    form_submit = st.form_submit_button('크롤링 시작')

sql_total = '''
select *
from comments_fmkorea;
'''

response = connect_fmkorea(1)
comments = get_comments(response)


if form_submit and pages is not None:
    for page in range(1, int(pages)+1):
        response = connect_fmkorea(page)
        comments = get_comments(response)
        st.write(comments)


    st.write('저장성공')
    result_conn = st.connection('scraping_comments_for_deepseek_db', type='sql', autocommit=True)
    result_df = pd.DataFrame(result_conn.query(sql=sql_total,ttl=3600))
    st.write(result_df)
    
