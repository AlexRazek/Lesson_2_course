import json

def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

posts = read_json('data/posts.json')
comments = read_json('data/comments.json')

# Получаем подсчет комментариев для шага 1
# Используем для вывод нужных постов шага 2

def get_post():
    with open("data/posts.json", "r", encoding="utf-8") as file:
        posts = json.load(file)
    for item in range(len(posts)):
        pk = posts[item]['pk']
        posts[item]['comments_len'] = len(get_comment_for_post(pk))
    return posts

# *** получаем посты по Id *** (Шаг 2)

def get_for_post(post_id):
    posts_for_post = []
    # with open("data/posts.json", "r", encoding="utf-8") as file:
    #     posts = json.load(file)
    for post in posts:
        if post.get("pk") == post_id:
            posts_for_post.append(post)
    return posts_for_post


 #*** Получаем комментарии для Шага 2 ***

def get_comment_for_post(post_id):
    comments_for_post = []
    # with open("data/comments.json", "r", encoding="utf-8") as file:
    #     comments = json.load(file)
    for comment in comments:
        if comment.get("post_id") == post_id:
            comments_for_post.append(comment)
    return comments_for_post

#*** Выполняем поиск  *** (Шаг 3)

def posts_search_by_word(s):
    # with open("data/posts.json", "r", encoding="utf-8") as file:
    #     posts = json.load(file)
    post_match = []
    if s:
        post_match = [x for x in posts if s in x.get('content').lower()]
        post_match.append(s)
    return post_match

#*** Реализуем вывод по пользователю  *** (Шаг 4)

def show_user(username):
    show_user = []
    # with open("data/posts.json", "r", encoding="utf-8") as file:
    #     posts = json.load(file)
    for user in posts:
        if user.get("poster_name") == username:
            show_user.append(user)
    return show_user




