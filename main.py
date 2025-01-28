import streamlit as st
import pandas as pd
from common.scraping import get_comments
from common.scraping import connect_fmkorea
from common.database import insert_data_to_mysql


st.title('Deepseek에 대한 커뮤니티 반응 (에펨코리아)')


with st.form('st_form'):
    pages = st.text_input('몇 페이지까지 스크래핑 하시겠습니까?')
    form_submit = st.form_submit_button('크롤링 시작')


if form_submit and pages is not None:
    for page in range(1, int(pages)+1):
        response = connect_fmkorea(page)
        comments = get_comments(response)
        insert_data_to_mysql(comments)

    result_conn = st.connection('scraping_comments_for_deepseek_db', type='sql', autocommit=True)
    result_df = pd.DataFrame(result_conn.query(sql='select * from comments_fmkorea;', ttl=3600))
    st.write(result_df)

