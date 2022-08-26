import configparser         # To read configuration details from config.ini file
import json                 # To convert api response to json
import requests             # To make api request
import sqlite3              # Data is loaded in SQLITE3 Database 
import pandas as pd         # Pandas to perform data transformations

# Get API Key/s and Host/s data
def get_api_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    return config    

# Connect to Database
def connect_to_db():
    db_conn = None
    try:
        db_conn = sqlite3.connect('stockprices.db')
        db_cursor = db_conn.cursor()
    
        return db_conn, db_cursor
    except:
        print("ERROR: Could not connect to Database\n")

# Query the Stock price from AlphaVantage API
def query_api_data(ticker):
    
    conf = get_api_config("config.ini")

    headers = {
        "X-RapidAPI-Key":conf['api']['key'],
        "X-RapidAPI-Host":conf['api']['host']
    }

    querystring = {
        "function":"TIME_SERIES_DAILY",
        "symbol":ticker,
        "outputsize":"compact",
        "datatype":"json"
    }

    response = requests.request(method="GET", url=conf['api']['base_url'], headers=headers, params=querystring)
    
    return response.text
    
def transform_data(data):
    df_daily_price = pd.DataFrame(data_dict["Time Series (Daily)"]).T.reset_index()
    df_daily_price.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
    df_daily_price.insert(0, 'ticker', ticker, True)

    return df_daily_price

def create_table(db_conn, db_cursor):
    try:
        # Create a new table if not already created  
        db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily (
            ticker text NOT NULL,
            date text NOT NULL,
            open real,
            high real,
            low real,
            close real,
            volume integer,
            PRIMARY KEY (ticker, date))
    """)
        db_conn.commit()
    except:
        pass
    
    
    

def insert_records(df_data, db_conn):
    try:
        num_rows_created = df_data.to_sql(name='daily', con=db_conn,  if_exists='append', index=False)
        print("{} Record/s inserted\n".format(num_rows_created))
    except sqlite3.IntegrityError as err:
        print("Record/s already exists in Table\n")


if __name__ == "__main__":
    db_conn, db_cursor = connect_to_db()
    create_table(db_conn, db_cursor)

    # Stock Price data for following tickers are fetched
    tickers = ["TSLA", "IBM"]

    for ticker in tickers:
        # EXTRACT
        data_dict = json.loads(query_api_data(ticker))

        # TRANSFORM
        df_daily_price = transform_data(data_dict)

        # LOAD
        insert_records(df_daily_price, db_conn)
    
    # LOAD CSV File 
    df_db = pd.read_sql('SELECT * FROM daily', db_conn)
    df_db.to_csv('daily_prices.csv', index=False)

    # CLOSE Database connection
    db_conn.close()
    
