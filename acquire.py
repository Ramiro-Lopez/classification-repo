import pandas as pd
import env
import os

""" 
Make a function named get_titanic_data that returns the 
titanic data from the codeup data science database as a pandas data frame. 
Obtain your data from the Codeup Data Science Database.
"""


def get_connection(db: str, user: str = env.user, host: str = env.host, password=env.password) -> str:
    return f"mysql+pymysql://{user}:{password}@{host}/{db}"


def get_titanic_data(file_name="titanic.csv") -> pd.DataFrame:
    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    query = "SELECT * FROM passengers"
    connection = get_connection("titanic_db")
    df = pd.read_sql(query, connection)
    df.to_csv(file_name, index=False)
    return df

"""
Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database as a pandas data frame. 
The returned data frame should include the actual name of the species in addition to the species_ids. 
Obtain your data from the Codeup Data Science Database.
"""

def get_iris_data(file_name="iris.csv") -> pd.DataFrame:
    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    query = """SELECT * 
               FROM species
               JOIN measurements
               USING (species_id)"""
    connection = get_connection("iris_db")
    df = pd.read_sql(query, connection)
    df.to_csv(file_name, index=False)
    return df

"""
Make a function named get_telco_data that returns the data from the telco_churn database in SQL. 
In your SQL, be sure to join contract_types, internet_service_types, payment_types tables with the customers table, 
so that the resulting dataframe contains all the contract, payment, and internet service options. 
Obtain your data from the Codeup Data Science Database.
"""
    
def get_telco_data(file_name="telco_churn.csv") -> pd.DataFrame:
    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    query = """SELECT * 
               FROM customers
               LEFT JOIN contract_types
               USING(contract_type_id)
               LEFT JOIN internet_service_types
               USING (internet_service_type_id)
               LEFT JOIN payment_types
               USING (payment_type_id)"""
    connection = get_connection("telco_churn")
    df = pd.read_sql(query, connection)
    df.to_csv(file_name, index=False)
    return df

