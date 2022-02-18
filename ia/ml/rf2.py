import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
param_range = {
 'n_estimators': [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000],
 'bootstrap': [True, False],
 'max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, None],
 'max_features': ['auto', 'sqrt'],
 'min_samples_leaf': [1, 2, 4],
 'min_samples_split': [2, 5, 10],
 'n_estimators': [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
 
 }




model = RandomForestRegressor(n_jobs=8)

def split_data(df):
    X = df.iloc[:,:-1]
    y = df.iloc[:,-1]
    return X,y

def grid_search(X,y):
    results = GridSearchCV(
        model,
        param_grid = param_range,
        cv = 5
    )
    results.fit(X,y)
    estimator = results.best_estimator_
    params = results.best_params_
    return estimator, params


if __name__ == '__main__':
    df = pd.read_csv('export.csv')
    X,y = split_data(df)
    estimator, params = grid_search(X,y)
    resultados = [estimator, params]
    print(resultados)

    
    