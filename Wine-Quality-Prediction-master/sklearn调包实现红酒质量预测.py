import os
import sys
import numpy as np 
import pandas as pd 

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

import matplotlib as mpl 
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

def evaluate_regression_model(y_true, y_pred):
    """
    Evaluate a regression model using various metrics.

    Parameters:
    y_true (array): Actual values.
    y_pred (array): Predicted values.

    Returns:
    dict: Dictionary containing evaluation metrics.
    """
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    return {
        "MSE": mse,
        "RMSE": rmse,
        "MAE": mae,
        "R2 Score": r2
    }



#对数据集中的样本属性进行分割，制作X和Y矩阵 
def feature_label_split(pd_data):
    #行数、列数
    row_cnt, column_cnt = pd_data.shape
    #生成新的X、Y矩阵
    X = np.empty([row_cnt, column_cnt-1])       #生成两个随机未初始化的矩阵
    Y = np.empty([row_cnt, 1])
    for i in range(0, row_cnt):
        row_array = redwine_data.iloc[i, ]
        X[i] = np.array(row_array[0:-1])
        Y[i] = np.array(row_array[-1])
    return X, Y


#把特征数据进行标准化为均匀分布
def uniform_norm(X_in):
    X_max = X_in.max(axis=0)
    X_min = X_in.min(axis=0)
    X = (X_in-X_min)/(X_max-X_min)
    return X


#主函数
if __name__ == "__main__":
    
    #读取样本数据
    redwine_data = pd.read_csv("winequality-red.csv", sep=";")
    #样本数据进行X、Y矩阵分离
    X, Y = feature_label_split(redwine_data)
    #对X矩阵进行归一化
    unif_X = uniform_norm(X)
    #对样本数据进行训练集和测试集的划分
    unif_trainX, unif_testX, train_Y, test_Y = train_test_split(unif_X, Y, test_size=0.3, random_state=0)
    
    
    #模型训练
    model = Ridge()     #L2正则的线性回归
    model.fit(unif_trainX, train_Y)
    
    #模型评估
    print("训练集上效果评估 >>")
    train_pred = model.predict(unif_trainX)
    results = evaluate_regression_model(train_Y, train_pred)
    print(results)

    print("\n测试集上效果评估 >>")
    test_pred = model.predict(unif_testX)
    results = evaluate_regression_model(test_Y, test_pred)
    print(results)