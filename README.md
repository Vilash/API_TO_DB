# API_TO_DB
Load stock prices data from Alpha Vantage API to a SQLITE DB and then populate CSV file.


Objective is to perform data extraction using Python. [Alpha Vantage API](https://www.alphavantage.co/documentation/) is used to collect daily stock prices data for different tickers, load them to SQLITE3 DB and populate a CSV file thereafter.

### API <--> Python File <--> SQLITE DB --> CSV File

Pre-requisites
* Python3
* [Alpha Vantage API](https://www.alphavantage.co/documentation/) Account
* `request` library
* `pandas` library
* `configparser` library to get API key details

## To be able to run the code in this repo
* Clone this repo
* Subscribe to [Alpha Vantage API](https://www.alphavantage.co/documentation/) via [RapidAPI](https://rapidapi.com/alphavantage/api/alpha-vantage/) to get API Key
* Create a `config.ini` file:
  ```
  [api]
key=7e2293a2c6msh6560fea3ee95896p188930jsn3b6810001b47
host=alpha-vantage.p.rapidapi.com
base_url=https://alpha-vantage.p.rapidapi.com/query
  ```

