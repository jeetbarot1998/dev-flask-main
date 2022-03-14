# from dal.data_fetch import data_fetch_from_api
import config


# def api_datafetch_factoring():
#     '''format raw api data'''
#     dataset_list = list()
#     json_data = data_fetch_from_api(config.jobs_by_industry_data_url)
#     for raw_rowdata in json_data:
#         rowdata = dict()
#         rowdata['Year'] = raw_rowdata[8]
#         rowdata['Region'] = raw_rowdata[9]
#         rowdata['NAICS Code'] = raw_rowdata[10]
#         rowdata['Industry'] = raw_rowdata[11]
#         rowdata['Jobs'] = raw_rowdata[12]
#         dataset_list.append(rowdata)
#     return dataset_list

def common_movie_search(genre_1_list,genre_2_list):
    common_genre_list =list()
    for val in genre_1_list:
        if val in genre_2_list:
            common_genre_list.append(val)
    common_string_for_sarch = '+'.join(common_genre_list)
    link_for_movie_list = config.base_url_for_movie + str(common_string_for_sarch) +'+movies'
    link_for_movie = {'link_for_movie_list' : link_for_movie_list}

    return link_for_movie

