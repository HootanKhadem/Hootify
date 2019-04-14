import json
from src.controller.Main import Methods as methods

files_and_folders = {}


def create_env_file():
    env_file = open("./.env", "w+")
    env_file.close()


def generate_env_file(root, dirs, files):
    create_env_file()
    env_file = open("./.env", "a")
    database_host = input("Please enter the database host")
    database_password = input("Please enter the database password")
    methods.write_in_env_file('DB_HOST', database_host, env_file)
    methods.write_in_env_file('DB_PASSWORD', database_password, env_file)




    # for file in files:
    #     formatted_file_name = methods.remove_unwanted_substring(file).strip()
    #     files_and_folders[formatted_file_name].append({
    #         'file': file,
    #         'root': root,
    #         'directories': dirs
    #     })
