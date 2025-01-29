import streamlit as st
import pandas as pd
import common.scraping as scraping
from common.database import insert_data_to_mysql

st.title('Deepseek에 대한 한국 커뮤니티 반응')

with st.form('st_form'):
    community = st.selectbox('커뮤니티를 선택하세요', ('fmkorea', 'dcinside'))
    pages = st.text_input('몇 페이지까지 스크래핑 하시겠습니까?')
    
    if not pages.isdecimal():
        st.write('숫자를 입력하세요')
    
    form_submit = st.form_submit_button('시작')

if form_submit and pages.isdecimal() and community:
    for page in range(1, int(pages)+1):
        try:
            response = scraping.connect_community(page, community)
            comments = scraping.get_comments(response, community)
            insert_data_to_mysql(comments, community)
        except Exception as e:
            st.write('저장실패했습니다.')
            st.write(str(e))

    result_conn = st.connection('scraping_comments_for_deepseek_db', type='sql', autocommit=True)
    result_df1 = pd.DataFrame(result_conn.query(sql='select * from comments_fmkorea;', ttl=3600))
    result_df2 = pd.DataFrame(result_conn.query(sql='select * from comments_dcinside;', ttl=3600))
    
    st.write('fmkorea')
    st.write(result_df1)
    st.write('dcinside')
    st.write(result_df2)

