from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Подключение к MongoDB
client = MongoClient('mongodb://root:root@mongodb:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Функция для добавления данных в MongoDB
@app.route('/api/add', methods=['POST'])
def add_data():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({'message': f'Данные добавлены с ID: {result.inserted_id}'})

# Функция для получения данных из MongoDB
@app.route('/api/data', methods=['GET'])
def get_data():
    data = collection.find_one()
    return jsonify({'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
