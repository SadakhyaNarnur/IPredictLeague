#data preprocessing
import pandas as pd
#produces a prediction model in the form of an ensemble of weak prediction models, typically decision tree
import xgboost as xgb
#the outcome (dependent variable) has only a limited number of possible values. 
#Logistic Regression is used when response variable is categorical in nature.
from sklearn.linear_model import LogisticRegression
#A random forest is a meta estimator that fits a number of decision tree classifiers 
#on various sub-samples of the dataset and use averaging to improve the predictive 
#accuracy and control over-fitting.
from sklearn.ensemble import RandomForestClassifier
#a discriminative classifier formally defined by a separating hyperplane.
from sklearn.svm import SVC
#displayd data
from IPython.display import display

data = pd.read_csv('C:\\Users\\jaravin1\\Desktop\\ipl\\IPL-ML-2018-master\\IPL-ML-2018-master\\Dataset\\ip.csv')
display(data.head())

#What is win rate of toss winning team ?

# Total number of matches.
n_matches = data.shape[0]

# Calculate number of features. -1 because we are saving one as the target variable (win/lose/draw)
n_features = data.shape[1] - 1

# Calculate matches won by home team.
n_tosswins = len(data[data.toss_winner == data.winner])

# Calculate win rate for home team.
win_rate = (float(n_tosswins) / (n_matches)) * 100

# Print the results
print ("Total number of matches: {}".format(n_matches))
print ("Number of features: {}".format(n_features))
print ("Number of matches won by toss winning team: {}".format(n_tosswins))
print ("Win rate of toss winning team: {:.2f}%".format(win_rate))

#what is win rate of home team ?
if data.city=='Banglore':
    home_team = 'Royal Challengers Bangalore'
if data.city=='Chennai':
    home_team = 'Chennai Super Kings'
if data.city=='Punjab':
    home_team = 'Kings XI Punjab'
if data.city=='Delhi':
    home_team = 'Delhi Capitals'
if data.city=='Mumbai':
    home_team = 'Mumbai Indians'
if data.city=='Rajasthan':
    home_team = 'Rajasthan Royals'
if data.city=='Kolkata':
    home_team = 'Kolkata Knight Riders'
if data.city=='Hyderabad':
    home_team = 'Sunrises Hyderabad'

home_wins = len([home_team == data.winner])
print (home_wins)
home_winrate = (float(home_wins)/(n_matches))*100
print (home_winrate)




