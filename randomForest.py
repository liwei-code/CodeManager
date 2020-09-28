# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import  pandas as pd
import numpy as np
import  matplotlib
from sklearn.model_selection import GridSearchCV
from  sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import  os
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = pd.read_csv("iris.data",header = None)
    x,y = data[np.arange(4)],data[4]
    # x= x[[2,3]]
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)
    if os.path.exists('rf.model'):
        print("模型加载......")
        model = joblib.load('rf.model')
    else:
        print("模型训练......")
        y = LabelEncoder().fit_transform(y)
        rf = RandomForestClassifier(n_estimators=20,criterion="entropy",max_depth=5,min_samples_split=7,min_samples_leaf=3,random_state=2020131)
        model = GridSearchCV(rf,param_grid={'max_depth':np.arange(3,7),
                                    'min_samples_split':np.arange(2,9,2),
                                    'min_samples_leaf':np.arange(1,5)})
    model.fit(x_train,y_train)
    y_t = model.predict(x_train)
    print(accuracy_score(y_train,y_t))
    y_pred = model.predict(x_test)
    print(accuracy_score(y_test,y_pred))
    joblib.dump(model,'rf.model')
    # result = y_pred == y_test
    # print(result)
    # print(pd.value_counts(result))
    # print("正确率：",np.mean(result))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
