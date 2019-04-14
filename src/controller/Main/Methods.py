import os as os
from src.controller.Configurations import Config as Config
from src.controller.IMDB import GetData as imdb
from src.controller.Main import Hootify as Hootify

miscellaneous = 'Miscellaneous'
documentary = 'Documentary'
directors = 'Directors'
user_interaction = 'userInteraction'
supported_video_format = ('mkv', 'mp4', 'avi', 'm4v')
unwanted = ['480p', '480', '720p', '720', '1080p', '1080', 'm480p', 'm480', 'm720p', 'm720', 'm1080p', 'm1080',
            'bluray', 'BluRay', 'brrip', 'br ', 'ShAaNiG.com', 'ShAaNiG', 'YIFI', 'x264', 'x265', 'BOKUTOX', 'H264',
            'AAC-RARBG', 'XviD', 'AC3-VLiS', 'BDRip', 'www.TamilRockers.net',
            ' [Tamil + English]', 'anoXmous', 'IranFilm', 'Best-Movies.info', 'tinymoviez',
            'dvdrip', 'm-720p_shan', 'My-Top250_Org', 'MissRipZ', 'DUBFA', 'zeberzee', '[ENG]', 'GAZ', 'MVGroup.org',
            'AAC', 'Ganool', '30NAMA', 'YekMovie', 'bestmovies.info', 'BDRip', 'Qi-Yin', 'Film2Movie_ORG', 'PsyCoSys',
            '(5.1)', 'mkv-Zen_Bud', 'Deceit', 'KickASS', '(MicroStar RG)', 'MicroStar RG', 'MicroStarRG', 'BeLLBoY',
            '(Kingdom-Release)', 'Iran-Film_2', 'Mediasity', 'LavinMovie', 'HDTVRiP', 'VLiS',
            'Team Nanban', 'UsaBit.com', 'axxo', 'Top250_org', 'Film2Movie', 'm-hd', 'teh-song', 'MkvCage',
            'HDBRiSe', 'DTS', 'MitZep', 'PhoenixRG', 'PhoenixRG', 'Film2Movie_INFO', 'MovieSharghi', 'BR-Rip',
            'IMDB-DL.Com', 'BEROZFILM', 'Ganool_2', 'DibaMovie', 'nLiBRA', 'AC3', 'AC3-nLiBRA', 'LFilm', 'extended',
            'Directors Cut', 'DirCut', 'Qi-Yin', 'AsCo_By IAL', 'UNRATED', 'DC', 'Film2Movie_BiZ', 'NLtoppers',
            'WEB-DL', 'WEBDL', 'WEB_DL', 'WEB DL', 'www.UsaBit.com ', ' (StyLish Release)', 'StyLishSaLH', 'Iran-Film',
            'PatoghDL', '(1)', 'Teh-Music', 'anoXmous_', 'MP3-RARBG', 'UNRATED', 'UNRATED CUT', '6CH', 'MMKV',
            'SHULiBAN', 'HD3D', 'HD3D1', 'iMovie-DL.Com', 'BlRy', 'WBB', 'LIMITED', 'HDRip', 'YTS.AG', '10bit',
            'PSA.lavinMovie', 'PSA_lavinMovie', 'PSA lavinMoive', 'HEVC', 'MP3-FGT', '30NAMA_2', 'RMTeam', 'GECKOS',
            'YTS.PE', 'b.lu.ry', 'info_-_', 'NF.WEB-DL', 'MULTISUB', '{Simba}', 'PARENTE', 'IMAX', 'Tigole',
            'vatanmovie', 'Ozlem', 'tenzin', 'www.film2serial.ir', 'P4DGE', 'www.superfundo.org', 'KAA', '3F518C0F',
            'kitty kode', 'AVC', 'Studio Ghibli', 'aka ', 'JRR', 'EuReKA', 'dxva', 'HDScene Release', 'RmD',
            'ShareConnector', 'NiXX', 'iNTERNAL.CD2', 'iNTERNAL.CD1', 'UNCUT', 'Studio Ghibli', 'AnimeRG', '10bit BD',
            'bd72', 'WEBRip', 'AAC-ETRG', 'best-movies.info_-_', 'best_movies.info', 'MZABI', 'BrRip_Joy', 'x0r',
            'Filmha  .Org', 'MyKavirMusic', 'AMIABLE', 'Sujaidr', 'HDTV', 'Doostiha.NET', 'full movie', 'fullmovie',
            'filmir', 'SamSerial', 'mkv', 'mp4', 'avi', 'm4v']

unwanted_compound = ['english', 'farsi', 'audio', 'dub', 'dubbed', 'dual', 'japanese', 'italian', 'FA', 'JP', 'ENG',
                     'jap', 'jpn']

case_sensitive_strings = ['PSA', 'BR', 'KOREAN', '2CH', 'MVG']
special_characters = ['.', '_', '(', ')', '[', ']']

def start_app():
    print("welcome to a app that will backup your movies for you!")
    Config.create_or_read_config_file()
    Hootify.hootify_directory(get_src_directory())


def y_n_switch_case(x):
    return {
        'Y': True,
        'y': True,
        'yes': True,
        'N': False,
        'n': False,
        'no': False,
    }[x]


def get_text_from_user():
    user_text = input()
    return user_text


def get_usb_device():
    devices = []
    command_result = os.popen('ls /media/$USER').read()
    logged_in_user = os.popen('echo $USER').read()
    if command_result != '':
        print("Each device shown below has a number before it's name \n"
              "please select the source hard disk using ONLY it's number")
        devices = command_result.split('\n')
        i = 1
        for device in devices:
            if device != '':
                print(str(i) + '- ' + device)
                i += 1

        user_choice = get_text_from_user()
        print("you chose: " + user_choice)
        usb_address = '/media/' + logged_in_user.strip() + '/' + str(devices[int(user_choice) - 1])
        return usb_address
    else:
        print("no usb device is connected please connect a device and try again")
        print("type 'OK' when done")
        user_ready = get_text_from_user()
        if user_ready.lower() == 'ok':
            get_usb_device()


def get_src_directory():
    print("Please enter the path for your backup directory")
    src_directory = get_text_from_user()
    if os.path.isdir(src_directory):
        if os.path.exists(src_directory):
            return src_directory
        else:
            print("this path does not exists.")
            return get_src_directory()
    else:
        print("this is not a directory")
        return get_src_directory()


def get_person_name(person):
    unformatted_name = person.data["name"].split(', ')
    if len(unformatted_name) == 1:
        return unformatted_name, "_"
    return unformatted_name[1], unformatted_name[0]


def create_hootify_folders(target_folder_path):
    if not os.path.exists(target_folder_path + '/Miscellaneous'):
        os.makedirs(target_folder_path + '/Miscellaneous')
        Config.write_into_config_file(miscellaneous)
    if not os.path.exists(target_folder_path + '/Documentary'):
        os.makedirs(target_folder_path + '/Documentary')
        Config.write_into_config_file(documentary)
    if not os.path.exists(target_folder_path + '/Directors'):
        os.makedirs(target_folder_path + '/Directors')
        Config.write_into_config_file(directors)
    if not os.path.exists(target_folder_path + '/user_interaction'):
        os.makedirs(target_folder_path + '/user_interaction')
        Config.write_into_config_file(directors)


def remove_unwanted_substring(file_name):
    for bad_string in unwanted:
        file_name = file_name.replace(bad_string, '')
    for character in special_characters:
        file_name = file_name.replace(character, ' ')
    for index_1 in range(len(unwanted_compound)):
        index_2 = index_1 + 1
        for index_2 in range(len(unwanted_compound)):
            if (unwanted_compound[index_1]) in file_name and (unwanted_compound[index_2]) in file_name:
                file_name = file_name.replace(unwanted_compound[index_1], '')
                file_name = file_name.replace(unwanted_compound[index_2], '')
    return file_name


def write_in_env_file(key, text, file):
    file.write(key, ":", text, "\n")
