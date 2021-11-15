from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html', title='Our First FSD')


if __name__ == '__main__':
    app.run(debug=True)
