# Acquisition

import os

import pandas as pd

from env import get_connection

#1) Make a function named get_titanic_data that returns the titanic data from the codeup data science database as a pandas data frame. 
#Obtain your data from the Codeup Data Science Database.

#creating a function; get_titanic_data to return all columns from the passengers table and saving it as a csv file
def get_titanic_data():

    filename = 'titanic.csv'

    if os.path.isfile(filename):
    
        return pd.read_csv(filename)

    else:

        url = get_connection('titanic_db')

        query = '''
                SELECT *
                FROM passengers
                '''

        titanic = pd.read_sql(query, url)

        titanic.to_csv(filename, index = 0)

        return titanic

#2) Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database as a pandas data frame.
#The returned data frame should include the actual name of the species in addition to the species_ids. Obtain your data from the Codeup Data Science Database.

#creating a function; get_iris_data to return all columns from the measurements and species table and saving it as a csv file
def get_iris_data():

    filename = 'iris.csv'

    if os.path.isfile(filename):

        return pd.read_csv(filename)

    else: 

        url = get_connection('iris_db')

        query = '''
                SELECT *
                FROM measurements
                LEFT JOIN species ON species.species_id = measurements.species_id
                '''

        iris = pd.read_sql(query, url)

        iris.to_csv(filename, index = 0)

        return iris

#3) Make a function named get_telco_data that returns the data from the telco_churn database in SQL. In your SQL, be sure to join contract_types,
#internet_service_types, payment_types tables with the customers table, so that the resulting dataframe contains all the contract, payment, and internet service options.
#Obtain your data from the Codeup Data Science Database.

#creating a function; get_telco_data to return all columns from the customers, contract_types, IST, and payment types table and saving it as a csv file
def get_telco_data():

    filename = 'telco.csv'

    if os.path.isfile(filename):

        return pd.read_csv(filename)

    else: 

        url = get_connection('telco_churn')

        query = '''
                SELECT *
                FROM customers
                LEFT JOIN contract_types ON contract_types.contract_type_id = customers.contract_type_id
                LEFT JOIN internet_service_types ON internet_service_types.internet_service_type_id = customers.internet_service_type_id
                LEFT JOIN payment_types ON payment_types.payment_type_id = customers.payment_type_id
                '''
    
        telco = pd.read_sql(query, url)

        telco.to_csv(filename, index = 0)  

        return telco

#4) Once you've got your get_titanic_data, get_iris_data, and get_telco_data functions written, now it's time to add caching to them.
#To do this, edit the beginning of the function to check for the local filename of telco.csv, titanic.csv, or iris.csv. If they exist, use the .csv file. 
#If the file doesn't exist, then produce the SQL and pandas necessary to create a dataframe, then write the dataframe to a .csv file with the appropriate name.


#verifying that the titanic.csv file was created from the previous function.
def get_titanic_data_2():

    filename = 'titanic.csv'

    if os.path.isfile(filename):
    
        return pd.read_csv(filename)

    else:

        print('file not found')


#verifying that the iris.csv file was created from the previous function.
def get_iris_data_2():

    filename = 'iris.csv'

    if os.path.isfile(filename):

        return pd.read_csv(filename)

    else: 

        print('file not found')


#verifying that the telco.csv file was created from the previous function.
def get_telco_data_2():

    filename = 'telco.csv'

    if os.path.isfile(filename):

        return pd.read_csv(filename)

    else: 

        print('file not found')











