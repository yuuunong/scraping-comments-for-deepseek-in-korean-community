import enum

class INSERT_SQLs(enum.Enum):
    comments = (enum.auto(), """
    insert
        comments_fmkorea (title, comment)
    values
        ('{title}, {comment})
    """, '데이터 저장')