from flask import request
import config
import jwt
from datetime import datetime, timedelta
from functools import wraps
import json


def create_token(user_details, duaration_of_valididty, private_key):
    """ Create JWT token for the user """
    token = jwt.encode(
        {
            'user_details' : user_details,
            'validity' : json.dumps(datetime.utcnow() + timedelta(minutes= duaration_of_valididty), indent=4, sort_keys=True, default=str)
        }, private_key,
        algorithm= 'HS256')
    return {'token' : token.decode('UTF-8') , 'status': 'success'}


def token_required(input_func):
    """ Token Required"""
    @wraps(input_func)
    def decorator(*args , **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        else:
            return 'You are not Authorized', 401
        try:
            data = jwt.decode(token,
                              config.Private_key,
                              algorithms='HS256')
        except jwt.ExpiredSignatureError:
            return {'message' : 'Token is Expired'}, 401
        except Exception:
            return {'message': 'Token is Invalid'}, 401

        return input_func(*args, **kwargs)
    return decorator


def get_token_info():
    token = None
    if 'Authorization' in request.headers:
        token = request.headers['Authorization']

    if not token:
        raise Exception('Token is Missing')

    data = jwt.decode(token,config.Private_key,algorithm = 'HS256')
    return data