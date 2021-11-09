from flask import Flask,jsonify,request

# Test API

app = Flask(__name__)

data = [
    {'name':'Rahul','age':35},
    {'name':'Ujjwal','age':33}
]

# First route ( End Point )
@app.route('/getfriend')
def get_friends():
    return jsonify(data)


# Second route ( Second End Point )
@app.route('/get/<name>')
def get_friend_by_name(name):
    for item in data:
        if item['name'] == name:
            # return {'age':item['age']}
            return jsonify(item['age'])
    return 'not present'


# Third End Point 
@app.route('/addfriend',methods=['POST'])
def add_friend():
    if request.method == 'POST':
        response = request.get_json()
        name = response['name']
        age = response['age']
        new_friend = {'name':name,'age':age}
        data.append(new_friend)
        return jsonify(data),201
    else:
        return 'Some error'


# Fourth End Point 
@app.route('/delfriend/<name>',methods=['DELETE'])
def def_friend(name):
    for index,item in enumerate(data):
        if item['name'] == name:
            item.clear()
            data.pop(index)
            print('deleted')
            break
    else:
        return '<h1>Not found</h1>'
    return jsonify(data),202



 

if __name__ == '__main__':
    app.run(debug=True)


