from flask import Flask
from flask import request, jsonify, Blueprint
from datetime import datetime
from flask_cors import CORS, cross_origin

from database import datos, setup


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

setup.create_table() #crea la tabla

@app.route('/data', methods=['POST'])
def add_data():
    temperatura = request.json['temperatura']
    #ph = request.json['ph']
    created_date = datetime.now().strftime("%x") #5/22/2021

    data = (temperatura, created_date) #para guardar
    data_id = datos.insert_data(data) #devuelve el id

    if data_id:
        datas = datos.select_data_by_id(data_id)
        return jsonify({"data": datas}) 
    return jsonify({"message": "Internal Error"})


@app.route('/data', methods=['GET'])
def get_tasks():
    """
    Ruta para mostrar todas las tareas creadas
    """
    data = datos.select_all_data()
    if data:
        return jsonify({"data" : data})
    elif data == False:
        return jsonify({"message": "Internal Error"})
    else:
        return jsonify({"message": {}}) 
if __name__ == ('__main__'):
    app.run(debug=False)