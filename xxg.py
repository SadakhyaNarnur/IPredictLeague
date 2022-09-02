from prediction import predict
from flask import Flask, render_template, request, flash
import os
import pandas as pd
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier

def predicttoss(home_team, away_team, city, toss_winner, toss_decision):
    data = pd.read_csv('./Dataset/matches_cleaned.csv')
    n_matches = data.shape[0]

    # Calculate number of features. -1 because we are saving one as the target variable (win/lose/draw)
    n_features = data.shape[1] - 1

    # Calculate matches won by home team.
    n_tosswins = len(data[data.toss_winner == data.winner])

    # Calculate win rate for home team.
    win_rate = (float(n_tosswins) / (n_matches)) * 100
    return win_rate


def predictseason(home_team, away_team, city, toss_winner, toss_decision):

    winner = predict(home_team, away_team, city, toss_winner, toss_decision).__str__()
    

