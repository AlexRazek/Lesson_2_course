from flask import Flask, request, render_template
from functions import read_json

posts = read_json('data/posts.json')
comments = read_json('data/comments.json')

# POST_PATH = "posts.json"
# # UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template("index.html", posts=posts, comments=comments)


app.run()