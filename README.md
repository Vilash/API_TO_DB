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
  key=your-api-key-from-rapid-api
  host=alpha-vantage.p.rapidapi.com
  base_url=https://alpha-vantage.p.rapidapi.com/query
  ```
  
* Since we are using SQLITE3 DB a lightweight, serverless, no fuss DB we don't need to install any DB Client. Python comes with one out-of-the-box.

* Create a new virtual environment, activate it and install the requirements from `requirements.txt`:
  ```
  python3 -m venv /path/to/new/virtual/environment
  source /newvirtualenvironment/bin/activate
  pip install -r requirements.txt install the required dependencies from `requirements.txt`
  ```

* The only API headers data to be provided are as follows:
  ```headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": api_host
  ```
  from the config.ini file, the code reads it anyway, just make sure to update the api key as stated earlier.
 
* There are four query parameters we are sending with api call however symbol parameter is most important as we will be interacting/changing it to data for different tickers
 ```
 querystring = {
        "function":"TIME_SERIES_DAILY",
        "symbol":ticker,
        "outputsize":"compact",
        "datatype":"json"
    }
 ```
  

