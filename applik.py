import json
from flask import Flask, request, render_template
from functions import get_post, get_comment_for_post, get_for_post, posts_search_by_word, show_user
app = Flask(__name__)

# posts = read_json('data/posts.json')
# comments = read_json('data/comments.json')


@app.route("/")
def page_index():
    posts = get_post()
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    with open("data/comments.json", "r", encoding="utf-8") as file:
        comments = json.load(file)
    comments_add = get_comment_for_post(post_id)
    postik = get_for_post(post_id)
    return render_template("post.html", posts=postik, comments=comments, comments_add=comments_add, comments_count=len(comments_add))


@app.route("/search/")
def page_search():
    s = request.args.get("s")
    posts = posts_search_by_word(s)
    return render_template("search.html", posts=posts, posts_count=len(posts), s=s)


@app.route("/user-feed/<username>")
def show_user_all_posts(username):
    with open("data/comments.json", "r", encoding="utf-8") as file:
        comments = json.load(file)
    posts = show_user(username)
    return render_template("user-feed.html", posts=posts, comments=comments)


app.run()
