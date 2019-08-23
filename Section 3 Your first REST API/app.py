from flask import Flask ,jsonify , request , render_template

app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello u0o! c:'
#
# app.run(port = 5000)
stores = [
    {
        'name':'amazon',
        'items' : [
            {
            'name':'Keyboard',
            'price':19.99
            }
         ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')




@app.route('/store' ,methods=['POST'])
def create_store():
    request_data = request.get_json()

    new_store = {
        'name':request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

# def create_store():
#     pass
@app.route('/store/<string:name>') #https://12.0.0.1/store/some_item
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found noob'})

@app.route('/store')
def get_stores():
    return jsonify({"stores":stores})

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store():
    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price' : []
                }
            stores['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:

        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message':'store not found'})


app.run(debug=True,port = 5000)
