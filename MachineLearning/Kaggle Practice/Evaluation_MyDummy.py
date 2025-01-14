from sklearn.base import BaseEstimator
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class MyDummyClassifier(BaseEstimator):
    # fit() 메서드는 아무것도 학습하지 않음 (그냥 여자일 때 생존으로 예측하면 되니까)
    def fit(self, x, y=None):
        pass

    # predict() 메서드는 단순히 Sex 피처가 1이면 0, 그렇지 않으면 1로 예측함
    def predict(self, x):
        pred = np.zeros((x.shape[0], 1))
        for i in range(x.shape[0]):
            if x['Sex'].iloc[i] == 1:
                pred[i] = 0
            else:
                pred[i] = 1
        return pred

def encode_features(dataDF):
    features = ['Cabin', 'Sex', 'Embarked']
    for feature in features:
        le = LabelEncoder()
        le.fit(dataDF[feature])
        dataDF[feature] = le.transform(dataDF[feature])
    return dataDF

# Null 처리
def fillna_mean(df, data):
    df[data].fillna(df[data].mean(), inplace=True)
    return df

def fillna_n(df, data):
    df[data].fillna('N', inplace=True)
    return df

def fillna_zero(df, data):
    df[data].fillna(0, inplace=True)
    return df

#  불필요한 속성 제거
def drop_features(df):
    df.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)
    return df

# 레이블 인코딩 수행
def format_features(df):
    df['Cabin'] = df['Cabin'].str[:1]
    features = ['Cabin', 'Sex', 'Embarked']
    for feature in features:
        le = LabelEncoder()
        le = le.fit(df[feature])
        df[feature] = le.transform(df[feature])
    return df

def transform_features(df):
    df = fillna_mean(df, 'Age')
    df = fillna_n(df, 'Cabin')
    df = fillna_n(df, 'Embarked')
    df = fillna_zero(df, 'Fare')
    df = drop_features(df)
    df = format_features(df)
    return df

titanic_df = pd.read_csv('./data/train.csv')
y_titanic_df = titanic_df['Survived']
x_titanic_df = titanic_df.drop('Survived', axis=1)
x_titanic_df = transform_features(x_titanic_df)
x_train, x_test, y_train, y_test = train_test_split(x_titanic_df, y_titanic_df, test_size=0.2, random_state=11)

myclf = MyDummyClassifier()
myclf.fit(x_train, y_train)

mypredictions = myclf.predict(x_test)
# print(mypredictions)  : 여자일 때 생존으로만 예측한 값.
print('Dummy Classifier 정확도 : {0:.4f}'.format(accuracy_score(y_test, mypredictions)))