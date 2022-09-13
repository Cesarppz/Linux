from flask import jsonify


def bad_request():
    return jsonify({
        'susccess':False,
        'data':{},
        'message':'Bad Request', 
        'error':'400'
    }), 400

def not_found():
    return jsonify({
        "error":404,
        'data':{},
        'susccess':False,
        'message':'Resource not found'
        }), 404


def response(data):
    return jsonify({
        'susccess': True,
        'data': data
    }), 200