from flask import Flask ,request
from flask_restful import Resource,Api

items =[]

app = Flask(__name__)
api = Api(app)
class Item(Resource):
    def get(self,name):
        item = next(filter(Lambda x: x['name'] == name,items))

        return {"item":None},404

    def post(self,name):
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
