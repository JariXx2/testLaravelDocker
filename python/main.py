from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Подключение к MongoDB
client = MongoClient('mongodb://root:root@mongodb:27017/')
db = client['mydatabase']
collection = db['mycollection']

@app.route('/api/data', methods=['GET'])
def get_data():
    data = collection.find_one()
    return jsonify({'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
