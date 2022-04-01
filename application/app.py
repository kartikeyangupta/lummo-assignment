#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request, jsonify
import json
import logging
from logging import Formatter, FileHandler
import os

#----------------------------------------------------------------------------#
# Local Imports
#----------------------------------------------------------------------------#
from utils.utilities import get_values_from_key, get_keys_from_values, load_json_data, upload_json_data

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')

DATA_PATH = app.config.get('DATA_PATH') + app.config.get('DATA_NAME')
DATA = load_json_data(DATA_PATH)

@app.route('/get/<key>/', methods=['GET'])
def get_value(key):
    try:
        value = DATA.get(key, None)
        if value is None:
            app.logger.warning('Key %s is not available in our database', key)
            return jsonify({'result': False, "message" : "There is no such key '{}' available".format(key)}), 404
        else:
            app.logger.info('Key %s has value %s', key, value)
            return jsonify({'result': True, "message": value}), 200
    except AttributeError:
        app.logger.exception('Please check if the Database path is correct or not, failed to fetch key {}'.format(key))
        return jsonify({'result': False, 'message': "Our database is having some issues, value for {} couldn't be fetched".format(key) }), 500
    except Exception as err:
        app.logger.exception('Error occured while fetching data with key {} from our database'.format(key))
        return jsonify({'result': False, 'message': "Error occured while fetch data {}".format(key) }), 500 

@app.route('/set/', methods=['POST'])
def set_value():
    try:
        if request.method == 'POST':
            data = request.json
            key = data.get('key')
            value = data.get('value')
            if DATA.get(key, None):
                DATA[key].append(value)
            else:
                DATA[key] = [value]
            upload_json_data(DATA_PATH, DATA)
            return jsonify({'result': True, "message": "Key {} has a new value {} setted ".format(key, value)}), 201
        else:
            return jsonify({'result': False, 'message': 'Request not allowed'}), 405
    except Exception as err:
        app.logger.exception('Error occured while fetching data with key {} from our database'.format(key))
        return jsonify({'result': False, 'message': "Error occured while fetch data {}".format(key) }), 500 

@app.route('/search', methods=['GET'])
def search():
    try:
        if request.method == 'GET':
            params = request.args
            if params.get('prefix', None):
                result = get_values_from_key(DATA, params.get('prefix'))
                return jsonify({'result': True, 'data': result}), 200
            elif params.get('suffix', None):
                result = get_keys_from_values(DATA, params.get('suffix'))
                return jsonify({'result':True, 'data': result}), 200
            else:
                return jsonify({'result': False, 'message': "Please provide parameter / as args 'prefix/suffix'"}), 405
        else:
            return jsonify({'result': False, 'message': 'Request not allowed'}), 405
    except Exception as err:
        app.logger.exception('Exception {}'.format(type(err).__name__))
        return jsonify({'result':False, 'message':'Exception '}), 500


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'result': False, 'message': 'Internal server Error'}), 500


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'result': False, 'message': 'API not found'}), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000)

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
