from flask import Flask,request
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

items = []

class Item(Resource):
    def get(self,name):
        # Try using filter()
        item = next(filter(lambda n: n['name']==name,items),None)
        return {"item": item},200 if item is not None else 404

    def post(self,name):
        data = request.get_json()
        item={'name':name,'price':data['price']}
        items.append(item)
        return item,201

class ItemList(Resource):
    def get(self):
        return {'item':items}
     
api.add_resource(Item, '/item/<name>')
api.add_resource(ItemList, '/items')
if __name__=='__main__':
    app.run(debug=True)