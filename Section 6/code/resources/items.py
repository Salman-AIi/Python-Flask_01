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
        item = ItemModel(name,data['price'])

        try:
            item.insert()
        except:
            return{'message':'An Error Has Occurred While Inserting The Item.'},500

        return item.json(),201

    def delete(self,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query , (name,))

        connection.commit()
        connection.close()
        return {'message':'The Item Has Been Deleted!'}
    def put(self,name):

        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name,data['price'])

        if item:
            try:
                updated_item.insert()
            except:
                return {'message':'An Error Has Occurred While Inserting The Item.'} , 500
        else:
            try:
                updated_item.update()
            except:
                return {'message':'An Error Has Occurred While Updating The Item.'}
        return updated_item.json()

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name':row[0] , 'price':row[1]})
        connection.close()
        return {'items':items}
