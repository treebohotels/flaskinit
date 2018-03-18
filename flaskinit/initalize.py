import argparse
import os

from flaskinit import config


def create_flask_app(root_directory, app_list):
    """

    :param root_directory: root_direct of application
    :param list_apps: list of apps to be created with an application
    :return:
    """

    if not os.path.exists(root_directory):
        os.makedirs(root_directory)

    # Creating directories
    create_directories(root_directory,
                       config.DIRECTORIES['COMMON_DIRECTORIES'])

    for app in app_list:
        create_directories('{}/{}'.format(root_directory, app),
                           config.DIRECTORIES['APP_DIRECTORIES'])

    # Creating files within  directories
    create_requirement_files('{}/{}'.format(root_directory,
                                            config.DIRECTORIES[
                                                'COMMON_DIRECTORIES'][
                                                'REQUIREMENTS_DIR']))
    create_app_file('{}/{}'.format(root_directory,
                                   config.DIRECTORIES[
                                       'COMMON_DIRECTORIES'][
                                       'APP_DIR']))


def create_directories(root_directory, directory_map):
    for key, value in directory_map.items():
        if not os.path.exists(root_directory + value):
            os.makedirs(root_directory + value)


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


def create_requirement_files(path):
    """
    creates requirements files(base,local,prod) in requirement directory
    :param path:
    :return:
    """

    if not os.path.exists(path):
        os.makedirs(path)

    file_names = ['base.txt', 'local.txt', 'prod.txt', 'staging.txt']
    for file_name in file_names:
        file_path = path + file_name
        if not os.path.isfile(file_path):
            touch(file_path)


def create_app_file(path):
    """
    :param directory: creates app.py in a given directory location
    :return:
    """

    file_path = path + 'app.py'
    if not os.path.isfile(file_path):
        f = open(file_path, 'w')
        f.write('from flask import Flask\n\n')
        f.write('app = Flask(__name__)\n\n')
        f.write('@app.route(\'/\')\n')
        f.write('def hello_world():\n')
        f.write('\treturn \'Hello World!\'\n\n')
        f.write('if __name__ == \'__main__\':\n')
        f.write('\tapp.run()\n')
        f.close()


def create_app():
    """
    this is the entry point for the flaskinit command
    takes root_directory and list of apps from command line and initializes
    flask application directory structure
    :return:
    """
    parser = argparse.ArgumentParser(description='Initialize flask '
                                                 'application')

    parser.add_argument('-n', dest='name',
                        help='Name of your project', required=True)

    parser.add_argument('-p', dest='path',
                        help='Root directory of your application, '
                             'if not provided defaults'
                             'to current working directory ')

    parser.add_argument('-a', dest='apps', nargs='+',
                        help='List of apps to be created within your '
                             'application',
                        required=True)

    args = vars(parser.parse_args())
    apps = args['apps']
    name = args['name']
    path = args['path']

    if args['path'] is None:
        # initialize app in current directory if root_directory
        # is not specified
        create_flask_app('{}/{}'.format(os.getcwd(), name), apps)
    else:
        create_flask_app(path + name, apps)
