import os as os
from src.controller.IMDB import GetData as imdbData
from src.dao.data.DataHandler import DataHandler
from src.controller.Configurations import Config as Config
from src.controller.Google import GetData as googelData
from src.controller.Main import Methods as methods


# TODO:
# this method is supposed to save the progress of the program
# for E.G:
# if this is the first time ever the program is being started on a system
# keep a record of the files that have been copied and already backed up so if for any reason the program was stopped
#   it would not start over or forget the progress


def hootify_directory(target_folder_path):
    methods.create_hootify_folders(target_folder_path=target_folder_path)
    for root, dirs, files in os.walk(target_folder_path):

        for file in files:
            formatted_file_name = methods.remove_unwanted_substring(file).strip()
            movie_object = imdbData.get_movie(formatted_file_name)
            data_handler = DataHandler(movie_object.data)
            if movie_object is not None:
                data_handler.bind_data()
                # TODO: implement the moving process of the files inside designated folders


            else:
                try:
                    movie_name = googelData.google_search(formatted_file_name)
                except:
                    movie_name = None
                if movie_name is not None:
                    movie_object = imdbData.get_movie(movie_name)
                    data_handler.data = movie_object.data
                    if movie_object is not None:
                        data_bound = data_handler.bind_data()
                    else:
                        print('movie not found check the file name and try again later')
                        # TODO: move this file to a location for later user interaction
            # if data_bound:
