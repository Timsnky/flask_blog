from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 1',
        'content': 'First log post',
        'date_posted': 'January 5, 2022'
    },
    {
        'author': 'Joe Public',
        'title': 'Blog Post 2',
        'content': 'Second log post',
        'date_posted': 'January 6, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
