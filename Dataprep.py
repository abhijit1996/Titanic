import pandas as pd 
import numpy as np
from sklearn import preprocessing
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
train = train.drop(['Name','Ticket','Cabin'],axis=1)
test = test.drop(['Name','Ticket','Cabin'],axis=1)
train['Age'] = train['Age'].fillna(0)
test['Age'] = test['Age'].fillna(0)
train['Embarked'] = train['Embarked'].fillna('S')
test['Embarked'] = test['Embarked'].fillna('S')
le = preprocessing.LabelEncoder()
le.fit(np.array(train.Sex))
train['Sex'] = le.transform(np.array(train.Sex))
test['Sex'] = le.transform(np.array(test.Sex))
le.fit(np.array(train.Embarked))
train['Embarked'] = le.transform(np.array(train.Embarked))
test['Embarked'] = le.transform(np.array(test.Embarked))
train.set_index('PassengerId',inplace=True)
test.set_index('PassengerId',inplace=True)
train.to_csv('train_clean.csv')
test.to_csv('test_clean.csv')