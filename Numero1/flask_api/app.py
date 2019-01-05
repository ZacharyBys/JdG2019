import os
from flask import *

app = Flask(__name__)
app.secret_key = 'xyz'

# post request must be in a form-data
#@app.route('/image', methods=['GET', 'POST'])
#def upload_file():
#    if request.method == 'POST':
        


# post request must be in a form-data
#@app.route('/qr/<string:qr>', methods=['PUT'])
#def upload_qr_2_file(qr):

@app.route('/api/alien/', methods=['GET', 'POST'])
def alien():
    if request.method == 'GET':
        if 'aliens' not in session:
            return "No Aliens"
        else:
            return jsonify(session['aliens']), 200

    if request.method == 'POST':
        content = request.get_json()

        if 'current_index' not in session:
            session['current_index'] = 0
        if 'aliens' not in session:
            session['aliens'] = {}

        session['aliens'][str(session['current_index'])] = content
        content['id'] = session['current_index']
        session['current_index'] += 1

        return jsonify(content), 200


@app.route('/api/alien/name/<string:id>', methods=['PUT', 'DELETE', 'GET'])
def modify_alien(id):
    if request.method == 'GET':
        if 'aliens' in session:
            if id in session['aliens']:
                return jsonify(session['aliens'][id]), 200

        return jsonify('Alien does not exist'), 400

    if request.method == 'DELETE':
        if 'aliens' in session:
            if id in session['aliens']:
                aliens = session['aliens']
                del aliens[id]
                del session['aliens']
                session['aliens'] = aliens
                session.modified = True 
                return "Alien Deleted"

        return jsonify('alien does not exist'), 400

    if request.method == 'PUT':
        if 'aliens' in session:
            if id in session['aliens']:
                aliens = session['aliens']
                aliens[id] = request.json
                del session['aliens']
                session['aliens'] = aliens

                session.modified = True 
                return jsonify(session['aliens'][id]), 200

        return jsonify('alien does not exist'), 400


@app.route('/')
def test():
    return "success"


if __name__ == '__main__':
    app.run(host='127.0.0.1')