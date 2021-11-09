from flask import Flask 

# print(__name__)
app  = Flask(__name__)

@app.route('/')
def index():
    return """<html>
                <title>Hello</title>
                <style>
                body{
                    background:lightblue;
                }
                </style>
                <body>
                 
                 <div class='container'>
                 <ul>
                     <li>Food</li>
                     <li>Drinks</li>
                     <li>Machines</li>
                     <li>Groceries</li>
                  
                 </ul>
                 
                 </div>
                
                </body>
                
                
                """

if __name__ == '__main__':
    app.run(debug=True)
