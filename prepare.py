import os
import pandas as pd

from sklearn.model_selection import train_test_split
from env import get_connection
from acquire import get_iris_data, get_titanic_data, get_telco_data

def prep_iris():
    iris_df = get_iris_data()  
    iris_df = iris_df.drop(columns=['species_id', 'measurement_id'])
    iris_df = iris_df.rename(columns={'species_name': 'species'})
    return iris_df

def prep_titanic():
    titanic_df = get_titanic_data()
    titanic_df = titanic_df.drop(columns=['passenger_id', 'pclass', 'embarked'])
    return titanic_df

def prep_telco():
    telco_df = get_telco_data()
    telco_df = telco_df.drop(columns = ['contract_type_id', 'contract_type_id.1', 
                         'internet_service_type_id', 'internet_service_type_id.1', 
                         'payment_type_id.1', 'payment_type_id'])
    return telco_df

def train_val_test(df, strat, seed=42):
    train, val_test = train_test_split(df, train_size=0.7, random_state=seed, stratify=df[strat])
    val, test = train_test_split(val_test, train_size=0.5, random_state=seed, stratify=val_test[strat])
    return train, val, test
    
def eval_p(p, alpha = 0.05, seed = 42):
    if p < alpha: 
        print(f'The result is siginificant! We reject the null hypothesis with a p_value of {round(p, 3)}.')
    else:
        print(f'We fail to reject the null hypothesis with a p value of {round(p, 3)}.')