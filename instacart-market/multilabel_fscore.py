# coding: utf-8

def multilabel_fscore(y_true, y_pred):
    y_true, y_pred = set(y_true), set(y_pred)
    precision = sum([1 for i in y_pred if i in y_true]) / len(y_pred)
    recall = sum([1 for i in y_true if i in y_pred]) / len(y_true)
    return (2 * precision * recall) / (precision + recall)


