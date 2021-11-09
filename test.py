from flask import Flask

app = Flask(__name__)

# Routing Techniques 

@app.route('/')
def home():
    return 'Home page'

@app.route('/about')
def about():
    return ' How about you > About page '

@app.route('/contact')
@app.route('/co')
def contact():
    return 'Contact Page.........'

if __name__ == '__main__':
    app.run(debug=True)










