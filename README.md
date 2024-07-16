# <h1 align="center"> StockInvestAPI </h1>

## Table of Contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Contents](#content)
* [Installation](#installation)
* [Features](#features)
* [Citation](#citation)
* [Creators](#creators)

## General Info

* To build ARIMA predicive model and send the stock prediction, the flask app is separately built.


## Technologies
Technologies used for this project:
* Python, Flask
* Python libraries: pandas_datareader, yfinance, statsmodels, numpy, sklearn


## Content
Content of the project folder:

```
 Top level of project folder:
├── .idea                    # .idea directory
├── .gitignore               # .gitignore file
├── app.py                   # Flask app file
├── README.md                # README.md file
├── requirement.txt          # required dependencies
└── train.py                 # ARIMA model file
          
```

## Installation
1. Open a terminal, go to the project directory and install flask by entering ```pip install Flask```.
2. Install all dependencies you need by entering ```pip install -r requirements.txt```.
3. Run the development server: ```flask run```
5. Open [http://localhost:5000](http://localhost:5000) with your browser to see the result.
6. Now you can check our application and start contributing!


## Features
* Receive the stock name/symbol through API `Get` method.
* Train the ARIMA model, which is for time series forecasting, using 1000 days of historical data and find optimal parameters based on RMSE(Root-Mean-Square Deviation).
* 1000 days data is retrieved from yahoo finance using yfinance library.
* Predict 10-day stock prices using ARIMA model with optimal parameters.


## Citation
* ARIMA model: https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html
* yahoo finance: https://pypi.org/project/yfinance/

## Creators
* *Soo Park* (https://github.com/Soohyeun)
