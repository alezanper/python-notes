from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        "name": "My store",
        "items": [
            {
                "name": "my item",
                "price": 15.9
            }
        ]
    }
]
# POST Used to receive data
# GET used to send data back only

# POST /store data: {name:}
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    pass

# GET /store    return list
@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})

# POST /store/<string:name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    pass


app.run(port=5000)