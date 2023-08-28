import pandas as pd
import env
import os
from sklearn.model_selection import train_test_split

def prep_telco(df):
    df['internet_service_type'] = df['internet_service_type'].fillna('No internet')
    dummy_df = pd.get_dummies(df[['gender','partner', 'dependents', 'phone_service', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type', 'multiple_lines', 'online_backup', 'online_security', 'device_protection']], drop_first=True).astype(int)
    df = pd.concat([df, dummy_df], axis=1)
    return df

def split_telco_data(df):
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.internet_service_type)
    train, validate = train_test_split(train_validate,
                                       test_size=.3,
                                       random_state=123,
                                       stratify=train_validate.internet_service_type)
    return train, validate, test


def prep_titanic(df):
    # df = df.drop_duplicates()
    # dummy_df = pd.get_dummies(df[['sex','embarked']], drop_first=True).astype(int)
    # df = pd.concat([df, dummy_df], axis=1)
    # df = df.drop(columns=['passenger_id', 'sex', 'embarked', 'class', 'deck', 'embark_town'])
    # df = df['age'] = df['age'].fillna(29)
    return df

def split_titanic_data(df):
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.survived)
    train, validate = train_test_split(train_validate,
                                       test_size=.3,
                                       random_state=123,
                                       stratify=train_validate.survived)
    return train, validate, test

def prep_iris(df):
    df = df.drop(columns= ['species_id', 'measurement_id'])
    df = df.rename(columns={'species_name': 'species'})
    dummy_df = pd.get_dummies(df[['species']], drop_first=True).astype(int)
    df = pd.concat([df, dummy_df], axis=1)
    return df

def split_iris_data(df):
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.species)
    train, validate = train_test_split(train_validate,
                                       test_size=.3,
                                       random_state=123,
                                       stratify=train_validate.species)
    return train, validate, test
