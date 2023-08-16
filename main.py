# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-16

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 59 - Blog with Style

from flask import Flask, render_template
import requests
import json

# BLOG_URL = "https://api.npoint.io/46b7d5447ebd3c655f57"  # this gets pruned periodically, populate from blog-data.txt



app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def get_blog_data():
    # Get blog data from bin
    # response = requests.get(url=BLOG_URL)
    # response.raise_for_status()
    # data = response.json()
    # print("Obtained blog data")
    # print(data)
    with open('fake_api.json','r',encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@app.route('/')
def home():
    # Homepage for blog
    blog_posts = get_blog_data()
    print("Loaded blog posts")
    return render_template("index.html", posts=blog_posts)


@app.route('/about.html')
def about():
    # About
    return render_template("about.html")


@app.route('/contact.html')
def contact():
    # Contact
    return render_template("contact.html")

@app.route('/post/<num>')
def read_post(num):
    # Specific post
    blog_posts = get_blog_data()
    print("Loaded blog posts")
    requested_post = []
    for i in blog_posts:
        if str(i["id"]) == str(num):
            requested_post = i
    print("Selected blog post")
    return render_template("post.html", posts=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
