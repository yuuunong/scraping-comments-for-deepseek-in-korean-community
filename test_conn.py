import streamlit as st
import pandas as pd
from sqlalchemy import text

st.title('sql 접근 테스트')

conn = st.connection('scraping_comments_for_deepseek_db', type='sql', autocommit=True)

st.write(pd.DataFrame(result))


conn.session.execute(text("INSERT INTO comments_fmkorea (title, comment) VALUES ('hello', 'hi');"))
conn.session.commit()

result = conn.query(sql="select * from comments_fmkorea;", ttl=3600)
st.write(pd.DataFrame(result))