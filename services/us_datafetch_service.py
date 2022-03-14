from flask_restx import Resource
from flask import request
from utilities.Jwt_auth import token_required, get_token_info
# from utilities.ssp_cache import cache
from models.us_datafetch_model import api,search_common_movie_link,input_for_movie_link,input_different, test_api_model
# from bl.us_datafetch_bl import api_datafetch_factoring
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
import ssl
from dal.data_fetch import search_common
import requests
import ast
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# @api.route('/jobsbyindustry')
# class dummy(Resource):
#     @api.doc(response={200: 'Success', 400: 'Validation Error'})
#     @api.marshal_with(dummy_fields)
#     @api.response('default', 'Error')
#     def get(self):
#         '''This data shows jobs by industry, beginning in 2012, created from a dataset of economic profiles of the 10 Empire State Development (ESD) economic development regions. Refer to the About section for the data dictionary and other information.'''
#
#         '''NY Open Data'''
#         response = api_datafetch_factoring()
#         return response

@api.route('/search_for_common_differnt_inputs')
class search_differnt_inputs(Resource):
    # @api.expect(input_for_movie_link)
    @api.expect(input_different)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @token_required
    @api.marshal_with(search_common_movie_link)
    def post(self):
        # movie1 = api.payload['movie1']
        # movie2 = api.payload['movie2']
        movie1= request.headers['movie1']
        movie2 = request.headers['movie2']
        movie_link = search_common(movie1,movie2)
        return movie_link

@api.route('/test_api')
class Test_Api(Resource):
    # @api.expect(test_api_model)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @token_required
    # def post(self):
    #     test_api_rx = api.payload['Test']
    #     return 'Successfully recieved the payload as: ' + test_api_rx

    def get(self):
        a= get_token_info()
        print(a)
        return 'Successfully recieved the get request'

# TODO:FOR CACHE REER TTLCACHE AS WELL
# @cache.memoize(timeout=300)
@api.route('/search_for_common')
class search(Resource):
    @api.expect(input_for_movie_link)
    # @api.expect(input_different)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.response('default', 'Error')
    @api.marshal_with(search_common_movie_link)
    def post(self):
        movie1 = api.payload['movie1']
        movie2 = api.payload['movie2']
        # movie1= request.headers['movie1']
        # movie2 = request.headers['movie2']
        movie_link = search_common(movie1,movie2)
        if movie_link == 0:
            return 'Error occured while inserting in database'
        else:
            return movie_link




