# Time Series Analysis and Traditional Forecasting Algorithms

# Introduction:
Time Series Analysis is a statistical technique used to analyze and forecast data that is collected over time at regular intervals. It involves studying patterns, trends, and seasonality in time-dependent data to make predictions for future values. This documentation covers the basics of time series analysis, including Autocorrelation and Partial Autocorrelation, and explores three traditional forecasting algorithms: Autoregressive (AR), Moving Average (MA), Autoregressive Moving Average (ARMA), and Autoregressive Integrated Moving Average (ARIMA). These algorithms are applied to two datasets: monthly sunspots and daily minimum temperatures.

# Datasets:

**Monthly Sunspots Dataset:** The monthly sunspots dataset contains information about the number of sunspots recorded each month. It can be used to study the periodicity and seasonality of sunspot activity.

**Daily Minimum Temperatures Dataset:** The daily minimum temperatures dataset contains information about the minimum temperatures recorded daily. It can be used to analyze and forecast temperature patterns over time.

# Basics of Time Series Analysis:

**Autocorrelation (ACF):**
Autocorrelation measures the linear relationship between a time series and its lagged values. It helps to identify the presence of periodic patterns in the data. The ACF plot displays the correlation coefficient at various lags, showing the relationship between the time series and its past values.

**Partial Autocorrelation (PACF):**
Partial Autocorrelation removes the influence of intermediate lags and measures the direct relationship between a time series and its lagged values. PACF helps identify the number of AR terms in an ARIMA model.

# Difference between Correlation and Causation:
Correlation measures the statistical relationship between two variables, but it does not imply causation. A high correlation between two variables indicates that they are related in some way, but it does not prove that changes in one variable cause changes in the other. Causation involves demonstrating a cause-and-effect relationship, which requires additional evidence and experimentation.

# Traditional Forecasting Algorithms:

**Autoregressive (AR) Model:**
The AR model uses the past values of a time series to predict future values. It assumes that the future value depends linearly on its past values and a random error term. The order of the AR model, denoted as AR(p), indicates the number of lagged values used for prediction.

**Moving Average (MA) Model:**
The MA model uses the past forecast errors to predict future values. It assumes that the future value depends linearly on the past errors and a random error term. The order of the MA model, denoted as MA(q), indicates the number of past forecast errors used for prediction.

**Autoregressive Moving Average (ARMA) Model:**
The ARMA model combines the AR and MA models. It uses both the past values of the time series and the past forecast errors to predict future values. The order of the ARMA model, denoted as ARMA(p, q), indicates the number of lagged values and past forecast errors used for prediction.

**Autoregressive Integrated Moving Average (ARIMA) Model:**
The ARIMA model extends the ARMA model by including a differencing step to make the time series stationary. It includes three components: autoregression (AR), differencing (I), and moving average (MA). The order of the ARIMA model, denoted as ARIMA(p, d, q), indicates the number of lagged values, differencing orders, and past forecast errors used for prediction.

# Application to Datasets:

I applied the AR, MA, ARMA, and ARIMA algorithms to the two datasets: monthly sunspots and daily minimum temperatures. The models were trained and evaluated on the data to make predictions for future values.

# Root Mean Squared Error (RMSE) Results:

**Dataset 1: Monthly Sunspots**

- ARMA: 14.602575
- AR: 17.915120
- ARIMA: 19.983888
- MA: 34.770561

The best model for Dataset 1 (Monthly Sunspots) is the ARMA model, as it has the lowest RMSE value of 14.602575.

**Dataset 2: Daily Minimum Temperatures**

- ARMA: 0.842455
- ARIMA: 0.870322
- AR: 1.103359
- MA: 1.465316

The best model for Dataset 2 (Daily Minimum Temperatures) is the ARMA model, as it has the lowest RMSE value of 0.842455.

# Conclusion:

Time series analysis, including Autocorrelation and Partial Autocorrelation, is crucial for understanding patterns and seasonality in time-dependent data. The traditional forecasting algorithms (AR, MA, ARMA, and ARIMA) allow us to predict future values based on past observations. By applying these algorithms to the monthly sunspots and daily minimum temperatures datasets, we can gain insights into sunspot activity patterns and temperature trends over time. The RMSE results indicate the accuracy of each model's predictions on the respective datasets.