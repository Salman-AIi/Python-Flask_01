from flask import Flask ,request
from flask_restful import Resource,Api
from flask_jwt import JWT

items =[]

app = Flask(__name__)
api = Api(app)
class Item(Resource):
    def get(self,name):
        item = next(filter(Lambda x: x['name'] == name,items),None)

        return {"item":item},200 if item else 404

    def post(self,name):

        if next(filter(Lambda x: x['name'==name,items),None):
            return {'message':"An Item With Name'{}' Already Exists.".format(name)}, 400
        data = request.get_json()
        item = {'name':name,'price':data['price']}
        items.append(item)
        return item,201

class ItemList(Resource):
    def get(self):
        return {'items':items}


api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/item')
app.run(port=5000,debug=True)
