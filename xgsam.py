import xgboost as xgb
import pandas as pd
import numpy as np
from IPython.display import display
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

data = pd.read_csv('C:\\Users\\jaravin1\\Desktop\\ipl\\2017(1).csv')
#print(data.keys())
#print(data.iloc[:3])
#display(data.head())
csk = data[(data.winner==2)]
csk_wins = csk.iloc[:]
#print(csk_wins)
#print(data.keys())
print(csk.shape)
#print(data.describe)
X, y = data[['team1','team2','toss_winner']],data['winner']
#print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
res=xgb.XGBClassifier(seed = 82)
xg_reg = xgb.XGBRegressor(objective ='binary:logistic', colsample_bytree = 0.3, learning_rate = 0.1,max_depth = 5, alpha = 10, n_estimators = 10)
res.fit(X_train,y_train)
score = res.score(X_train, y_train)
score2 = res.score(X_test, y_test)
print("Training set accuracy: ", '%.3f'%(score*100))
print("Test set accuracy: ", '%.3f'%(score2*100))
#preds = xg_reg.predict(X_test)
#print(preds)
#rmse = np.sqrt(mean_squared_error(y_test, preds))


#print("RMSE: %f" % (rmse))
