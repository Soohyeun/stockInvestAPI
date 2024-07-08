import warnings
from pandas_datareader import data as pdr
import yfinance as yfin
import datetime
import statsmodels.tsa.arima.model as sma
import numpy as np
from sklearn.metrics import mean_squared_error

warnings.filterwarnings("ignore")

def getStock(stk, ttlDays):
    numDays = int(ttlDays)
    # Only gets up until day before during
    # trading hours
    dt        = datetime.date.today()
    # For some reason, must add 1 day to get current stock prices
    # during trade hours. (Prices are about 15 min behind actual prices.)
    dtNow     = dt + datetime.timedelta(days=1)
    dtNowStr  = dtNow.strftime("%Y-%m-%d")
    dtPast    = dt + datetime.timedelta(days=-numDays)
    dtPastStr = dtPast.strftime("%Y-%m-%d")
    yfin.pdr_override()
    df = pdr.get_data_yahoo(stk, start=dtPastStr, end=dtNowStr)
    return df


def buildModel(df, ar, i, ma):
    model = sma.ARIMA(df['Close'], order=(ar, i, ma)).fit()
    return model


def predictAndEvaluate(model, test, train, title):
    # print("\n***" + title)
    # print(model.summary())
    start       = len(train)
    end         = start + len(test) -1
    predictions = model.predict(start=start, end=end, dynamic=True)
    mse = mean_squared_error(predictions, test)

    rmse = np.sqrt(mse)
    # print("RMSE: " + str(rmse))
    return rmse, predictions


def findBestmodel(train, test):
    modelStats = []
    min_rmse = 1000000000000
    best_model = None
    for ar in range(0, 5):
        for ma in range(0, 5):
            model = buildModel(train, ar, 0, ma)
            title = str(ar) + "_0_" + str(ma)
            rmse, predictions = predictAndEvaluate(model, test['Close'], train['Close'], title)
            if min_rmse >= rmse:
                min_rmse = rmse
                best_model = model
            modelStats.append({"ar": ar, "ma": ma, "rmse": rmse})
    return best_model


def predict(model, lenData):
    print(model.summary())
    start       = lenData
    end         = start + 9
    predictions = model.predict(start=start, end=end, dynamic=True)
    return predictions


def get_ten_days_predicton(stock_name):
    ##################################################################
    # CONFIGURATION SECTION
    NUM_DAYS = 1000
    TEST_DAYS = 10
    ##################################################################

    stockDf = getStock(stock_name, NUM_DAYS)
    lenData = len(stockDf)

    dfTrain = stockDf.iloc[0:lenData - TEST_DAYS, :]
    dfTest = stockDf.iloc[lenData - TEST_DAYS:, :]

    best_model = findBestmodel(dfTrain, dfTest)

    predictions = predict(best_model, lenData)
    return predictions.tolist()


predictions = get_ten_days_predicton('NVDA')
print(predictions)

