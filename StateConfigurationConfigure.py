# The config module for setting the states and transitions of interest in the solver

import configparser
from collections import OrderedDict
from tkinter import filedialog

# 'config' is defined below for short-hand purposes in this file

config = configparser.ConfigParser()


config['STATES'] = {

    'Er1': '4I15/2',
    'Er2': '4I13/2',
    'Er3': '4I11/2',
    'Er4': '4I9/2',
    'Er5': '4F9/2',
    'Er6': '4S3/2',
    'Er7': '2H11/2',
    'Er8': '4F7/2',
    'Yb1': '2F7/2',
    'Yb2': '2F5/2'
}


config['TRANSITIONS'] = {

    'Er5_Er1': 'Red',
    'Er6_Er1': 'S',
    'Er7_Er1': 'H',

}

config['INITIAL_TRANSITION'] = {
    'Er1_Er5': 3,
    'Er1_Er4': 1.5,
    'Er5_Yb2': 50,
    'Er4_Yb2': 50,
    'Er4_Er5': 2.5,
    'Er3_Er8': 6
}

config['INITIAL_STATE'] = {
    'Er1': 1000,
    'Er2': 300,
    'Er3': 150,
    'Er4': 200,
    'Er7': 500,
    'Er5': 12000,
    'Yb2': 20000
}


file_path = filedialog.asksaveasfile(title="Select a Save Location",
                                     filetypes=(("ini files", "*.ini"), ("all files", "*.*")), defaultextension='.ini')
print(file_path)
with open(file_path.name, 'w') as configfile:
    config.write(configfile)
