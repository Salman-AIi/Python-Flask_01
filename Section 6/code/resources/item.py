import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import JWT , jwt_required
from models.item import ItemModel



class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='This Field Is Required!'
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help='Every Store Needs An ID!'
    )
    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'Item Not Found'},404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':"An Item With Name'{}' Already Exists.".format(name)}, 400
        data = Item.parser.parse_args()
        item = {'name':name,'price':data['price']}
        item = ItemModel(name, **data)

        try:
            item.save_to_db(item)
        except:
            return{'message':'An Error Has Occurred While Inserting The Item.'},500

        return item.json(),201

    def delete(self,name):
        item = ItemModel.find_by_name(name)

        if item:
            item.delete_from_db(item)
        return {'message':'The Item Has Been Deleted Fam!'}

    def put(self,name):

        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)


        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_db(item)
        return item.json()

class ItemList(Resource):
    def get(self):
        return {'items':[item.json() for item in ItemModel.query.all()]}
