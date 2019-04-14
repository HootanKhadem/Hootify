from src.dao.database import DB as mysql_instance


def create_or_read_config_file():
    # TODO: edit this file with adding env file.
    # TODO: we need a logger to log application's progress
    # TODO: decouple this part of code. create a config manager. merge GenerateEnv and Config to track and update the contents of config files
    try:
        config_file = open('../../conf.txt', 'r')
        if 'INITIAL_CONFIG: DONE \n database created\n' in config_file:
            config_file.close()
        else:
            raise FileNotFoundError('config file not found')

    except:
        print('Creating config file...')
        config_file = open('../../conf.txt', 'a')
        mysql_instance.create_database_and_tables(mysql_instance)
        config_file.write('INITIAL_CONFIG: DONE \n database created')
        config_file.close()


def write_into_config_file(table_type, movie_name=None):
    config_file = open('../../conf.txt', 'a')
    if table_type == "Miscellaneous":
        config_file.write('Miscellaneous Folder Created \n')
    if table_type == 'Documentary':
        config_file.write('Documentary Folder Created \n')
    if table_type == 'Directors':
        config_file.write('Directors Folder Created \n')
    if table_type == 'copy':
        config_file.write('copying' + movie_name)
    if table_type == 'Done':
        config_file.write('Done ' + movie_name)
    config_file.close()
