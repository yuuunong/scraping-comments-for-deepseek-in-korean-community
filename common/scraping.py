import requests
from bs4 import BeautifulSoup as bs

def connect_fmkorea(p_page:int):
    url = f'https://www.fmkorea.com/search.php?act=IS&is_keyword=%EB%94%A5%EC%8B%9C%ED%81%AC&mid=home&where=document&page={p_page}'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
    response = requests.get(url = url, headers = header)
    return response

def get_comments(p_response:requests.models.Response) -> list:

    if p.response.status_code >= 400:
        return '접속 오류입니다.'

    bs_text = bs(p_response.text, 'html.parser')

    comment_list = bs_text.find_all('dl')

    comment_dict_list = [{
        'title': comment.find('dt').get_text(),
        'comment': comment.find('dd').get_text()
    } for comment in comment_list]

    return comment_dict_list