import configparser
from tkinter import filedialog
from collections import defaultdict
import pandas as pd
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

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
    initial_guess = dict(config_state['INITIAL_TRANSITION'])
    transition_list = []
    transition_initial = []
    for state in state_set:
        for second_state in state_set:
            if state != second_state:
                transition_list.append(state + "_" + second_state)

    for transition in transition_list:
        if transition not in initial_guess.keys():
            transition_initial.append(float(1))
        else:
            transition_initial.append(float(initial_guess[transition]))
    initial_trans_dict = dict(zip(transition_list, transition_initial))
    return initial_trans_dict


def build_initial_states(state_set):
    state_file = filedialog.askopenfile(title="Select an Initial Guess File", filetypes=(("ini files", "*.ini"),
                                                                                         ("all files", "*.*")))
    config_state = configparser.ConfigParser()
    config_state.read(state_file.name)
    initial_guess = dict(config_state['INITIAL_STATE'])
    states_initial = []
    for state in state_set:
        if state not in initial_guess.keys():
            states_initial.append(float(1000))
        else:
            states_initial.append(float(initial_guess[state]))
    initial_states_dict = dict(zip(state_set.keys(), states_initial))
    return initial_states_dict


def import_experimental(transition):
    filedialog.askopenfile(title="Select the experimental data file for " + str(transition) + "transition.",
                           filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    pd_read = pd.read_csv('C:/Users/Pone/Documents/RedHat Assessment/Goalies.csv', error_bad_lines=False)
    return pd_read

# Varies the specified parameter by the input percentage and returns the updated list

# Checks the configuration specified against the experimental input


def check_config(transition_initial, state_initial, trans_interest, experimental_array):
    state_current = state_initial
    redundance = []
    trans_interest = list(trans_interest.keys())
    state_decay = []
    state2_decay = []
    while state_current[trans_interest[0].rpartition('_')[0]] != 0:
        for transition in transition_initial:
            state_to = transition.rpartition('_')[2]
            state_from = transition.rpartition('_')[0]
            if transition not in redundance:
                if float(state_current[state_from]) >= - float(transition_initial[transition]) and\
                        float(transition_initial[transition]) < 0 or \
                        float(state_current[state_to]) >= float(transition_initial[transition]) \
                        and float(transition_initial[transition]) > 0:
                    state_current[state_from] += transition_initial[transition]
                    redundance.append(state_to + '_' + state_from)
                    state_current[state_to] -= transition_initial[transition]

        state_decay.append(state_current[trans_interest[0].rpartition('_')[0]])
        state2_decay.append(state_current[trans_interest[1].rpartition('_')[0]])
    plt.plot(state_decay)
    plt.show()

# Main loop and logic for choosing parameters and step sizes


def main_loop():
    state_friends = build_states()
    print(state_friends)
    transition_friends = transitions_interested()
    print(transition_friends)
    transition_set = build_transitions(state_friends)
    print(transition_set)
    initial_states = build_initial_states(state_friends)
    print(initial_states)
    print(transition_set)

    check_config(transition_set, initial_states, transition_friends, 0)


main_loop()
