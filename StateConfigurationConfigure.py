## The config module for general_api_pull.py

import configparser
from collections import OrderedDict
from tkinter import filedialog

# 'config' is defined below for short-hand purposes in this file

config = configparser.ConfigParser()


config['STATES'] = {

    'N1': '4I15/2',
    'N2': '4I13/2',
    'N3': '4I11/2',
    'N4': '4I9/2',
    'N5': '4F9/2',
    'N6': '4S3/2',
    'N7': '2H11/2',
    'N8': '4F7/2',
    'Yb1': '2F7/2',
    'Yb2': '2F5/2'
}


config['TRANSITIONS'] = {

    'N5_1': 'Red',
    'N6_1': 'S',
    'N7_1': 'H',

}


file_path = filedialog.asksaveasfile(title="Select a Save Location",
                                     filetypes=(("ini files", "*.ini"), ("all files", "*.*")), defaultextension='.ini')
print(file_path)
with open(file_path.name, 'w') as configfile:
    config.write(configfile)
