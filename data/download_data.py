#!/usr/bin/env python


def get_data(destin_dir = None, file_name = None):
    #import libraries
    import pandas as pd
    from sklearn.datasets import load_iris
    from pathlib import Path
    
    #load data
    data = load_iris()
    
    
    #load featuers and target variable
    X = data['data']
    y = data['target']
    target_names = data['target_names']
    feature_names = data['feature_names']
    
    
    #convert to pandas dataframes and 
    X = pd.DataFrame(X, columns=feature_names)
    y = pd.DataFrame(y)
    
    
    #merget them to a single dataframe
    df = pd.concat([X,y], axis=1).rename(columns={0:'target'})
    df.head()
    
    
    # clean up the column names
    df.columns = df.columns.str.strip(" (cm)").str.replace(" ", "_")
    df.head()
    
    # if a path is provided as an argument, file is written to that path
    # else the file is written to default location
    if not destin_dir:
        destin_dir = "data"
    destin_dir = Path(destin_dir)

    if not file_name:
        file_name = "train.csv"
    file_name = Path(file_name)

    file_full_path = Path.joinpath(destin_dir, file_name)
    print(file_full_path)

    df.to_csv(file_full_path, index=False)


if __name__ == "__main__":
    get_data()



