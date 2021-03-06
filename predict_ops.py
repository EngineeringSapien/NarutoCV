import itertools
import global_variables as glob_var
import numpy as np


def get_top_predictions(ordered_predictions):
    top_signs, top_signs_percents = [], []
    for i in range(2):
        top_signs.append(list(ordered_predictions)[-(i+1)])
        top_signs_percents.append(list(ordered_predictions.values())[-(i+1)])

    return top_signs, top_signs_percents


def order_predictions(labeled_predictions):
    ordered_predictions = {}
    for key, value in sorted(labeled_predictions.items(), key=lambda item: item[1]):
        ordered_predictions.update({key: value})

    return ordered_predictions


def label_predictions(labels, predictions):
    labeled_predictions = dict(zip(labels, predictions[0]))

    return labeled_predictions


def get_sequence_of_predictions(current_sequence, predictions):
    current_sequence.append(predictions)

    return current_sequence


def get_permutations_of_predictions(current_sequence):
    permutation = list(itertools.product(*current_sequence))

    return permutation


def get_top_signs(labels, predictions):
    labeled_predictions = label_predictions(labels, predictions)
    ordered_predictions = order_predictions(labeled_predictions)
    top_signs, top_signs_percents = get_top_predictions(ordered_predictions)

    return top_signs


def get_predictions(accumulated_predictions, prediction, sequence):
    average_prediction = accumulated_predictions / glob_var.mean_cutoff
    accumulated_predictions = np.zeros_like(prediction)
    top_signs = get_top_signs(glob_var.signs, average_prediction)
    sequence = get_sequence_of_predictions(sequence, top_signs)

    return accumulated_predictions, sequence, top_signs


def get_avererage_prediction(accumulated_predictions):
    average_prediction = accumulated_predictions / glob_var.mean_cutoff
    accumulated_predictions_reset = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype='float64')
    return average_prediction, accumulated_predictions_reset

