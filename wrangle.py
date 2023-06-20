import os
import pandas as pd
from env import get_db_url

def new_telco_data():
    '''
    This reads the telco data from the Codeup db into a df
    '''
    sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    
    # Read in DataFrame from Codeup.
    df = pd.read_sql(sql_query, get_db_url('telco_churn'))
    
    return df

def get_telco_data():
    '''
    This reads in telco data from Codeup database, writes data to
    a csv if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('telco.csv'):
        
        # read in data from csv file if one exists
        df = pd.read_csv('telco.csv', index_col=0)
        
    else:
        
        # Read data from db into a DataFrame
        df = new_telco_data()
        
        # Cache to .csv
        df.to_csv('telco.csv')
        
    return df

def clean_telco(df):
    '''
    This gets rid of columns not used in the project and creates dummy variables for use in the model
    '''
    # this drops unnecessary columns
    df = df.drop(columns =['payment_type_id','internet_service_type_id','contract_type_id', 'customer_id', 'gender', 'senior_citizen', 'partner', 'tenure', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'total_charges', 'internet_service_type', 'payment_type'])

    # this creates dummy variables
    dummy_df = pd.get_dummies(df[['dependents', 'contract_type', 'billing_type', 'churn']], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    return df


def split_data(df, test_size=.2, validate_size=.25, col_to_stratify=None, random_state=None):
    '''
    This splits data into test,train and validate data
    '''
    # This takes in a default variable or a default variable to determine target variable for stratification
    if col_to_stratify == None:
    # this splits the data
        train_validate, test = train_test_split(df, test_size=test_size, random_state=random_state)
        train, validate = train_test_split(train_validate,
                                       test_size=validate_size,
                                       random_state=random_state,)
    else:                                                        
        train_validate, test = train_test_split(df, test_size=test_size, random_state=random_state, stratify=df[col_to_stratify])
        train, validate = train_test_split(train_validate,
                                       test_size=validate_size,
                                       random_state=random_state,
                                       stratify=train_validate[col_to_stratify])
    return train, validate, test