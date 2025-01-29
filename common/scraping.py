import requests
from bs4 import BeautifulSoup as bs
import streamlit as st


def connect_community(p_page:int, p_community):
    fmkorea_url = f'https://www.fmkorea.com/search.php?act=IS&is_keyword=%EB%94%A5%EC%8B%9C%ED%81%AC&mid=home&where=document&page={p_page}'
    dcinside_url = f'https://search.dcinside.com/post/p/{p_page}/q/%EB%94%A5%EC%8B%9C%ED%81%AC'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'}

    if p_community == 'fmkorea':
        response = requests.get(url = fmkorea_url, headers = header)
    
    if p_community == 'dcinside':
        response = requests.get(url = dcinside_url, headers = header)
    
    return response



def get_comments(p_response:requests.models.Response, p_community:str) -> list:

    if p_response.status_code >= 400:
        st.write('접속 오류입니다.')
        return

    bs_text = bs(p_response.text, 'html.parser')

    if p_community == 'fmkorea':
        comment_list = bs_text.find('ul', class_='searchResult').find_all('li')
        comment_dict_list = [{
            'title': comment.find('dl').find('dt').find('a').get_text(),
            'comment': comment.find('dl').find('dd').get_text(),
            'gallery': comment.find('dl').find('dt').find('a').get_text()[1:comment.find('dl').find('dt').find('a').get_text().index(']')],
            'date_': comment.find('address').find('span', class_='time').get_text()
        } for comment in comment_list]

        return comment_dict_list

    if p_community == 'dcinside':
        comments_list = bs_text.find('ul',class_='sch_result_list').find_all('li')
        comments_dict_list = [{
            'title': comment.find('a').get_text(),
            'comment': comment.find('p', class_='link_dsc_txt').get_text(),
            'gallery': comment.find('p', class_='link_dsc_txt dsc_sub').find('a').get_text(),
            'date_': comment.find('p', class_='link_dsc_txt dsc_sub').find('span').get_text()
        } for comment in comments_list]

        return comments_dict_list
