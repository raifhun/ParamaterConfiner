import scipy
import numpy
import configparser
from tkinter import filedialog
from collections import defaultdict
import pandas as pd

# Builds the state sets


def build_states():
    state_file = filedialog.askopenfile(title="Select a State Configuration File", filetypes=(("hdf5 files", "*.ini"),
                                                                                              ("all files", "*.*")))
    config_state = configparser.ConfigParser()
    config_state.read(state_file.name)
    state_set = dict(config_state['STATES'])
    return state_set

# Builds the transitions of interest for comparison to data


def transitions_interested():
    state_file = filedialog.askopenfile(title="Select a State Configuration File", filetypes=(("hdf5 files", "*.ini"),
                                                                                              ("all files", "*.*")))
    config_state = configparser.ConfigParser()
    config_state.read(state_file.name)
    trans_int = dict(config_state['TRANSITIONS'])
    return trans_int


def build_transitions(state_set):  # builds the transition dictionary in general for the states described
    state_file = filedialog.askopenfile(title="Select an Initial Guess File", filetypes=(("ini files", "*.ini"),
                                                                                         ("all files", "*.*")))
    config_state = configparser.ConfigParser()
    config_state.read(state_file.name)
    initial_guess = dict(config_state['INITIAL_GUESS'])
    transition_list = []
    transition_initial = []
    for state in state_set:
        for second_state in state_set:
            if state != second_state:
                transition_list.append(state + "_" + second_state)

    for transition in transition_list:
        if transition not in initial_guess.keys():
            transition_initial.append(1)
        else:
            transition_initial.append(initial_guess[transition])
    initial_trans_dict = dict(zip(transition_list, transition_initial))
    return initial_trans_dict


def import_experimental(state):
    filedialog.askopenfile(title="Select the experimental data file for " + str(transition) + "transition.",
                           filetypes=(("csv files", "*.csv"), ("all files", "*.*")))



# Varies the specified parameter by the input percentage and checks the output with the experimental data

# Main loop and logic for choosing parameters and step sizes


def main_loop():
    state_friends = build_states()
    print(state_friends)
    print(transitions_interested())
    print(build_transitions(state_friends))


main_loop()
