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
    titanic_df = titanic_df.drop(columns=['passenger_id', 'pclass', 'embarked', 'deck'])
    med_age = titanic_df.age.median()
    titanic_df.age = titanic_df.age.fillna(med_age)
    return titanic_df

def prep_telco():
    telco_df = get_telco_data()
    telco_df = telco_df.drop(columns = ['contract_type_id', 'contract_type_id.1', 
                         'internet_service_type_id', 'internet_service_type_id.1', 
                         'payment_type_id.1', 'payment_type_id', 'customer_id'])
    return telco_df

def impute_vals(train, val, test):
    
    town_mode = train.embark_town.mode()
    
    train.embark_town = train.embark_town.fillna(town_mode)
    val.embark_town = val.embark_town.fillna(town_mode)
    test.embark_town = test.embark_town.fillna(town_mode)
    
    med_age = train.age.median()
    
    train.age = train.age.fillna(med_age)
    val.age = val.age.fillna(med_age)
    test.age = test.age.fillna(med_age)
    
    return train, val, test


def train_val_test(df, strat, seed=42):
    train, val_test = train_test_split(df, train_size=0.7, random_state=seed, stratify=df[strat])
    val, test = train_test_split(val_test, train_size=0.5, random_state=seed, stratify=val_test[strat])
    return train, val, test
    
    
def eval_p(p, alpha = 0.05, seed = 42):
    if p < alpha: 
        print(f'The result is siginificant! We reject the null hypothesis with a p_value of {round(p, 3)}.')
    else:
        print(f'We fail to reject the null hypothesis with a p value of {round(p, 3)}.')


def metrics():
    accuracy = '(TP + TN) /	(TP + TN + FP + FN)'
    recall = 'TP / (TP + FN)'
    true_positive_rate = 'TP / (TP + FN)'
    false_positive_rate = 'FP / (FP + TN)'
    true_negative_rate = 'TN / (TN + FP)'
    false_negative_rate = 'FN / (FN + TP)'
    precision = 'TP / (TP + FP)'
    f1_score = '2 * (precision * recall) / (precision + recall)'
    support = 'TP + FN'
    data = {
        'Metric': ['Accuracy', 'Recall', 'True Positive Rate', 'False Positive Rate', 'True Negative Rate', 'False Negative Rate', 'Precision', 'F1-Score', 'Support'],
        'Value': [accuracy, recall, true_positive_rate, false_positive_rate, true_negative_rate, false_negative_rate, precision, f1_score, support]
    }
    
    metrics_df = pd.DataFrame(data)
    return metrics_df
    

def rubric():
    data = {
        '': ['Actual Positive', 'Actual Negative'],
        'Predicted Positive': ['True Positive (TP)', 'False Positive (FP)'],
        'Predicted Negative': ['False Negative (FN)', 'True Negative (TN)'],
    }

    rubric = pd.DataFrame(data)
    rubric.set_index('', inplace=True)
    
    return rubric


def calculate_metrics(TP, TN, FP, FN):
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    recall = TP / (TP + FN)
    true_positive_rate = TP / (TP + FN)
    false_positive_rate = FP / (FP + TN)
    true_negative_rate = TN / (TN + FP)
    false_negative_rate = FN / (FN + TP)
    precision = TP / (TP + FP)
    f1_score = 2 * (precision * recall) / (precision + recall)
    support = TP + FN
    
    data = {
        'Metric': ['Accuracy', 'Recall', 'True Positive Rate', 'False Positive Rate', 'True Negative Rate', 'False Negative Rate', 'Precision', 'F1-Score', 'Support'],
        'Value': [accuracy, recall, true_positive_rate, false_positive_rate, true_negative_rate, false_negative_rate, precision, f1_score, support]
    }
    
    metrics_df = pd.DataFrame(data)
    return metrics_df
