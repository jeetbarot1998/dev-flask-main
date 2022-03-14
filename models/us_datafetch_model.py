from flask_restx import Namespace, reqparse, fields, inputs
from werkzeug.datastructures import FileStorage


# api = Namespace('USDataFetch', description='Open data from data.ny.gov')
api = Namespace('MovieSearch', description = 'Search On basis of genre in google')

#For File Upload

# FILE_UPLOAD = reqparse.RequestParser(bundle_errors=True)
# FILE_UPLOAD.add_argument('file', location='files', type=FileStorage, required=True)
# FILE_UPLOAD.add_argument('overwrite', type=inputs.boolean, help="to overwrite the file", required=False)


# dummy_fields = api.model('Dummy extracted', {
#     'Year': fields.Integer(attribute='Id'),
#     'Name': fields.String(attribute='name')
#     })

input_different = api.parser()
input_different.add_argument('movie1',location = 'headers')
input_different.add_argument('movie2',location = 'headers')

input_for_movie_link = api.model(
    'input_for_movie_link',{
        'movie1': fields.String(attribute = 'movie1'),
        'movie2': fields.String(attribute = 'movie2'),
    }
)

search_common_movie_link = api.model(
    'search_common_movie_link', {
        'Link' : fields.String(attribute ='link_for_movie_list')
    }
)

test_api_model = api.model(
    'test_api_model', {
        'Test': fields.String(attribute = 'Test'),
    }
)

