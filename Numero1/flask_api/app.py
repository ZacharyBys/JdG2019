import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template

app = Flask(__name__)

aliens = {}
current_index = 0


# post request must be in a form-data
#@app.route('/image', methods=['GET', 'POST'])
#def upload_file():
#    if request.method == 'POST':
        


# post request must be in a form-data
#@app.route('/qr/<string:qr>', methods=['PUT'])
#def upload_qr_2_file(qr):

@app.route('/api/alien', methods=['GET', 'POST'])
def alien():
    if request.method == 'GET':
        return aliens
    if request.method == 'POST':
        content = request.json

@app.route('/api/alien', methods=['POST'])
def add_alien():
    if not request.is_json:
        return abort(400)

    content = request.get_json()
    print(content)
    aliens[str(current_index)] = content
    return "alien added"


@app.route('/api/alien/name/<string:id>', methods=['PUT', 'DELETE'])
def modify_alien(id):
    if request.method == 'DELETE':
        del aliens[id]
    if request.method == 'PUT':
        content = request.json
        aliens[id] = content


@app.route('/')
def test():
    return "success"


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)