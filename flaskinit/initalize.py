import argparse

import os
import shutil


def create_flask_app(root_directory, app_list):
    """

    :param root_directory: root_direct of application
    :param list_apps: list of apps to be created with an application
    :return:
    """

    if not os.path.exists(root_directory):
        os.makedirs(root_directory)

    current_path = os.path.abspath(os.path.dirname(__file__))

    # path to project_structue of sample flask application
    project_structure_path = os.path.join(current_path,
                                          "../project_structure/")

    # path to app_structure stores the directory structure of domain specific
    # apps ,all apps will have similar structure as app_structure
    app_structure_path = os.path.join(current_path,
                                      "../project_structure/app_structure")

    # Copy common directories from project_structure
    copytree(project_structure_path, root_directory)
    shutil.rmtree(root_directory + '/app_structure')

    # Copy app directories from app_structure
    for app in app_list:
        app_dir_path = '{}/{}'.format(root_directory, app)
        copytree(app_structure_path, app_dir_path)


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            if not os.path.exists(d):
                shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


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
                             'if not provided defaults '
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


if __name__ == '__main__':
    create_flask_app('/Users/sohitkumar/code/', ['hello', 'hello1'])
