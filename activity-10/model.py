import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle

dataset=pd.read_csv('Salary_Data_SLR.csv')

X=dataset.iloc[:,0].values
Y=dataset.iloc[:,1].values

X=X.reshape(-1,1)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

regressor=LinearRegression()
regressor.fit(X_train,Y_train)

original=Y_test
prediction=regressor.predict(X_test)

print(r2_score(original,prediction))

m=open('model.pkl','wb')
pickle.dump(regressor,m)
m.close()
