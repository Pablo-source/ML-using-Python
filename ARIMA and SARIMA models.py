#!/usr/bin/env python
# coding: utf-8

# ## Time series analysis in Python
# ### Friday 13rh November 2020

# This notebook describes a practical forecasting script in Python. Using univariate time series analysis and Maplotlib python libraries to disaply the results

# We will focus on *univatiate* time series analysis. Only one time dependent variable is modelled using ARIMA and SARIMA models 

# ### ARIMA model

# An autoregressive integrated moving average (ARIMA) model is a generalization of an autoregressive moving average (ARMA) model. Both of these models are fitted to time series data either to better understand the data or to predict future points in the series (forecasting). ARIMA models are applied in some cases where data show evidence of non-stationarity, where an initial differencing step (corresponding to the "integrated" part of the model) can be applied one or more times to eliminate the non-stationarity.[1]
# 
# The AR part of ARIMA indicates that the evolving variable of interest is regressed on its own lagged (i.e., prior) values. The MA part indicates that the regression error is actually a linear combination of error terms whose values occurred contemporaneously and at various times in the past.[2] The I (for "integrated") indicates that the data values have been replaced with the difference between their values and the previous values (and this differencing process may have been performed more than once). The purpose of each of these features is to make the model fit the data as well as possible.
# 
# Non-seasonal ARIMA models are generally denoted ARIMA(p,d,q) where parameters p, d, and q are non-negative integers, p is the order (number of time lags) of the autoregressive model, d is the degree of differencing (the number of times the data have had past values subtracted), and q is the order of the moving-average model. 

# ### SARIMA model

# Seasonal Autoregressive Integrated Moving Average, SARIMA or Seasonal ARIMA, is an extension of ARIMA that explicitly supports univariate time series data with a seasonal component.
# 
# It adds three new hyperparameters to specify the autoregression (AR), differencing (I) and moving average (MA) for the seasonal component of the series, as well as an additional parameter for the period of the seasonality.

# #### Seasonal Elements  of the SARIMA model
# Seasonal ARIMA models are usually denoted ARIMA(p,d,q)(P,D,Q)m, where m refers to the number of periods in each season, and the uppercase P,D,Q refer to the autoregressive, differencing, and moving average terms for the seasonal part of the ARIMA model.[3][4]There are four seasonal elements that are not part of ARIMA that must be configured; they are:
# 
# 

# - P: Seasonal autoregressive order.
# - D: Seasonal difference order.
# - Q: Seasonal moving average order.
# - m: The number of time steps for a single seasonal period.

# **Program structure**

# As a self-contained project, I will analyse univariate time series data in a set of steps described below. I will start with exploratory analysis of the data and I will end by plotting the forecasted and actual values of the original time series.

# The steps described below can be split into three main analysis stages: a) Data exploration, 2) Modelling and forecasting 3) Choosing best performing model 4) Plotting the results

# In[81]:


# Get working directory
# Get WD


# In[82]:


get_ipython().run_line_magic('pwd', '')


# Analysis stages
# 1. Load dataset (from a Github account)
# 2. Perform exploratory analysis on the data
# 3.Prepare data for Time Series analysis
# 4. Check for stationarity of the data. Run Dickey Fuller test
# 5. Building a Loop to display Dickey fuller test
# 6. Explaring the  loop we just built
# 7. Differencing our data to make it stationary
# 8. ARIMA model 
# 9. Setup an SARIMA MODEL.  Includind seasonal order (1,1,1,12)
# 10. Forecast accuracy measure. Mean Absolute Percentage Error (MAPE).Future sessions
# 
# 

# https://towardsdatascience.com/the-data-science-process-a19eb7ebc41b

# ### 1. Load dataset (from a Github account)

# We are going to get the public available dataset for chanmpagne monthly sales from a *github* repository

# This database dedscribes the monthly sales of perrin freres champagne. 
# - CSV file from Github repository: perrin-freres-monthly-champagne.csv 

# You can obtain some extra information about this and other datasets from the above kaggle website

# We can also access a few other available dataset from Kaggle website
# https://www.kaggle.com/anupamshah/perrin-freres-monthly-champagne-sales

# The way you load CSV files from Github into python is by pointing to the URL on the github repository that hosts that file

# We use Pandas function read_csv() function from Pandas library to load in the data as a Dataframe

# In[84]:


import pandas as pd


# In[85]:


import numpy as np


# Now that we have loaded Pandas library we can load it using read_csv function

# In[7]:


# Load champagne sales from GITHUB repository
# Champagne Sales dataset. Load csv file
Sales = pd.read_csv('https://raw.githubusercontent.com/ethen8181/programming/master/time_series/keras/perrin-freres-monthly-champagne-.csv') 


# In[8]:


type(Sales)


# In[9]:


len(Sales)


# In the same way, we could load any dataset available in github 

# In[10]:


# PASSENGER DATASET. Load csv file 
Dataset = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv')  


# In[11]:


Dataset.plot()


# In[12]:


Sales.head()


# ### 2. Perform exploratory analysis on the data

# #### 2.1 First check dataset structure by looking at the first and last set of rows

# In[13]:


Sales.head()


# In[14]:


Sales.tail()


# The values in row 105 need to be removed before we start our analysis

# #### 2.1 Change column names

# We use colums() function to rename actual dataframe colum names 

# In[15]:


Sales.columns=["Month","Sales"]
Sales.head()


# In[16]:


Sales.tail()


# ### 3.Prepare data for Time Series analysis

# Now we drop the last record of the dataset

# In[17]:


#  Cleaning up the data
# We drop value using the ROWS axis (axis=0), remember column axis (axis=1)
Sales.drop(105,axis=0,inplace=True)


# In[18]:


Sales.tail()


# You may use the syntax below to check the data type of a particular column in Pandas DataFrame

# In[19]:


Sales['Month'].dtypes


# In[20]:


# Convert Month into Datetime
Sales['Month']=pd.to_datetime(Sales['Month'])


# In[21]:


Sales['Month'].dtypes


# In[22]:


Sales.head()


# Now as you can see the Month variable displays a full date with days months and years

# **Set Index**, We define Month as our index column in this dataframe

# In[23]:


Sales.set_index("Month",inplace=True)


# In[24]:


Sales.head()


# We can obtain a description of the current dataset by using the describe() function

# In[25]:


Sales.describe()


# #### 3.1 Plot the data

# We can produce a quick plot of the data by using the .plot() function 

# In[26]:


Sales.plot()


# As we can see in the above plot. Python has applied a default format to axis, line and plot legend. Perfect to scoping the shape of our data

# ### 4. Check for stationarity of the data. Run Dickey Fuller test

# One condition for Time Series analysis is that the data should be **stationary** to apply most TS forecasting models. This data looks seasonal *At some particular time periods, it inccreases or decreases, repeating this trehn on a yearly basics*, it presents some trend *trend is upwards on some months and dowward on some other months"

# We can test for stationarity using the *Dickey Fuller test*

# In[27]:


from statsmodels.tsa.stattools import adfuller


# We test the following null hypothesis H0
# H0 Null Hyp - Data is non stationary
# H1 Alternative Hyp - Data is stationary

# - H0: Null Hypothesis: Data is non stationary

# - H1: Alternative Hypothesis: Data is stationary

# If p value is less or equal than 0.05 then we reject null hypothesis, so data *is* stationary

# If p value is greater than 0.05 then we can't reject the null hypothesis, so data is *NOT* stationary

# In[28]:


adfuller(Sales)


# Out of the eight different outputs produced by the the Dickey Fuller test, we will focus on the first four. The second output *p-value* is the most important one to assess the stationarity of a TS, as it is used to assess the test statistic.

# - *ADF Test statistic*: Value of the ADFuller test itself

# - *P-VALUE*: P-value for the test statistic. 

# - *lags used*: Number of lags used to compute the test statistic

# - *Number of observations*: Number of observations involved in the test statistic

# For later use we can create a list that will help us to understand the output of this statistical test

# In[29]:


labels = ['ADF Test statistic','p-value','lags used','Number of observations']


# *DIckey Fuller test interpretation*

# HO: Null Hypothesis: Time series is *NOT* stationary

# H1: Alternative Hypothesis: Time series *IS* stationary

# If *p-value* is <= 0.05 (95% significance): Strong evidence against the Null hypothesis. We can reject the Null Hypothesis and accept the Alternative Hypothesis. So our Time series *IS STATIONARY*

# If *p-value* is > 0.05 (95% significance): Weak evidence against the Null hypothesis. We can't reject the Null Hypothesis. Time series has a unit root, indicating it is *NON STATIONRARY*

# An alpha of 0.05 is used as a cutoff for significance. If the *p-value* is less than 0.05, we reject the null hypothesis, and conclude that our time series is *STATIONARY*

# in our previous example, we obtained a p-value of  0.3639157716602417,indicating out TS data is NON-STATIONARY

# In[ ]:





# ### 5. Building a Loop to display Dickey fuller test

# We can save all these results into a list object called results, from the previous line of code, we load the statsmodel library to use the adfuller test function. We can create two list into two easy steps to store the Dickey fuller test resutls and assign some labels to it

# In[30]:


from statsmodels.tsa.stattools import adfuller


# In our first step. We can save that test statistic into a apecial type of list called tuple  to store the results

# In[31]:


results = adfuller(Sales)


# In[32]:


results


# In[33]:


type(results)


# In[34]:


# Recall the wrap up of adfuller test in a new object called results
results = adfuller(Sales)


# Then as a second step, we can build another list that will include the lables for each of the test outputs

# In[35]:


labels = ['ADF Test statistic','p-value','lags used','Number of observations']


# In[36]:


labels


# In[37]:


type(labels) 


# Then we can create a loop to join it all

# So then we can combine them in a loop

# In[38]:


for label,value in zip(labels,results):
    print(label+':'+str(value))


# We can include test results as printed outputs

# In[39]:


for label,value in zip(labels,results):
    print(label+':'+str(value))
# We can add a conditional statement to ease loop output interpretation
if results[1] <= 0.05:
     print("Dickey fuller p-value is",results[1], "below or equal to 0.05.there  is strong evidence against null hypotesis.Indicating the Time Series it is STATIONARY")
else:
     print("Dickey fuller p-value is",results[1], "Greater than 0.05. Weak evidence against null hypothesis.Indicating the Time Series  is non-stationary")


# In[ ]:





# ### 6. Explaring the  loop we just built

# We introduce a loop to retrive the results of the Dickey Fuller test. As we previously saw, the *for loop* in python is defined by a *colon* to declare the loop and an *indedntation* to specify the *action* to run in the loop:

# From previous section we have stored Dickey Fuller test results ina list called results. We can loop through each of its contents by using this list in a loop

# In[40]:


results = adfuller(Sales)


# In[41]:


results


# - *ADF Test statistic*: Value of the ADFuller test itself
# - *P-VALUE*: P-value for the test statistic. 
# - *lags used*: Number of lags used to compute the test statistic
# - *Number of observations*: Number of observations involved in the test statistic

# #### 6.1 Dickey Fuller test output values

# The for loop will display each element from results object. So we arbitraty choose word "value" to run loop through all different results object elements. 

# In[42]:


for value in results:
    print(value)


# But We could assign any name to loop through the "results" object elements, for example, we could call it "potato".

# In[43]:


for potato in (results):
    print(potato)


# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# - The **colon** at the end of the first line signals the start of a block of statements.
# - Python uses **indentation** rather than {} or begin / end to show nesting. Any consistent indentation is legal. 

# #### 6.2 Labels for Dickey Fuller test

# So we arbitraty choose word "label" to run loop through all different label object elements.

# In[44]:


for label in(labels):
    print(label)


#  But We could assign any name to loop through the "label" object elements, for example, we could call it "parsnip".

# for parsnip in(labels):
#     print(parsnip)

# #### 6.3 Using the ZIP function to bind labels and results together

# We can use the **ZIP** function for parallel iteration

# We can combine those outputs using the *zip()* function 

# Python’s zip() function creates an iterator that will aggregate elements from two or more iterables.

# This function is useful for parallel iteration

# In[45]:


numbers = [1,2,3]


# In[46]:


type(numbers)


# In[47]:


letters = ['a','b','c']


# In[48]:


type(letters)


# We can **combine** all output from the Dickey fuller test by using the **Zip function**

# In[49]:


zipped = zip(numbers,letters)


# In[50]:


zipped


# In[51]:


list(zipped)


# In our particular example we want to create a matrix that combines Dickey fuller test output values with meaningful labels to ease test interpretation

# In[52]:


results = adfuller(Sales)


# In[53]:


labels = ['ADF Test statistic','p-value','lags used','Number of observations']


# In[54]:


for label,value in zip(labels,results):
    print(label+':'+str(value))


# The second statement pring(label+':'+str(value)), simply prints together in a single statement the labels and test values, values must be turned into a string object for the contatenation of the labels and values objects to work

# #### 6.4 Accessing individual elelments within a loop in Python 

# Inside loops, the same indexing system applies as the one we saw for lists. First element is defined by 0, second by 1 and so on. 

# In[55]:


Exploring loops


# In[56]:


for value in (results):
    print(value)


# This means that to access the p-value from inside the loop, we should index it by [1] the second object position within the set of objects contained in the Dikey fuller test tupplet object

# We can print the P-value from the results object

# In[57]:


for value in (results):
    print(results[1])


# #### 6.5 Including an IF statement at the end of the loop 

# Finally, we can include an IF ELSE statement at the end of the loop to print the result of the dickey fuller test. IF ELSE statements in python are also declared by using a colon

# Python relies on **indentation** (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

# In[58]:


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# THis is how we would include the IF ELSE statement *after* our loop ends

# If *p-value* is <= 0.05 (95% significance): Strong evidence against the Null hypothesis. We can reject the Null Hypothesis and accept the Alternative Hypothesis. So our Time series *IS STATIONARY*

# Combinacion de un LOOP y un IF ELSE statement

# In[59]:


for value in (results):
    # Access individual elements from result objec
    # ADF Test statistic result[0]
    # p-value results[1]
    # lags used results[2]
    # Number of observations results[3]
    #print(results)
    
    print(results[1])
# Anyadir un conditional (IF STATEMENT) fuera del LOOP
if results[1] <= 0.05:
     print("Dickey fuller p-value is",results[1], "below or equal to 0.05.there  is strong evidence against null hypotesis.Indicating the Time Series it is STATIONARY")
else:
     print("Dickey fuller p-value is",results[1], "Greater than 0.05. Weak evidence against null hypothesis.Indicating the Time Series  is non-stationary")


# This is the final loop and IF ELSE statement we just built some steps ago

# In[60]:


for label,value in zip(labels,results):
    print(label+':'+str(value))
# We can add a conditional statement to ease loop output interpretation
if results[1] <= 0.05:
     print("Dickey fuller p-value is",results[1], "below or equal to 0.05.there  is strong evidence against null hypotesis.Indicating the Time Series it is STATIONARY")
else:
     print("Dickey fuller p-value is",results[1], "Greater than 0.05. Weak evidence against null hypothesis.Indicating the Time Series  is non-stationary")


# ### 7. Differencing our data to make it stationary

# From our original Sales dataset, we create a new variable called "Sales First Difference"

# If we substract the previous value to each actual value in our Sales Time series, we will be differencing once the original time series, and this might make the series to be stationary. 

# In[61]:


Sales['Sales First Difference']=Sales['Sales']-Sales['Sales'].shift(1)


# In[62]:


Sales['Sales'].shift(1)


# In[63]:


Sales.head(14)


# In[64]:


Plot this first differenced dataset for Sales data


# In[65]:


Sales['Sales First Difference'].plot()


# In[ ]:





# As you can see, we have stationaized, removed the trend from the original Sales TS
# 

# In[66]:


Sales.plot()


# When using differencing we shift one position that time series, substracting to each value the previous values in the TS

# In[67]:


Sales.head(10)


# As we can see that our data has one year cyle of upward and downward trend, we meed to opt for a **seasonal** difference, to take into account the trend contained into **12 months of data**, or a **whole year period**. 

# To account for this yearly seasonality, we will be shifting by **12 months** instead than by 1 month. 

# In[68]:


Sales['Sales Seasonal Difference']=Sales['Sales']-Sales['Sales'].shift(12)


# In[69]:


Sales.head(20)


# In[70]:


results_seaonal = adfuller(Sales['Sales Seasonal Difference'].dropna())


# In[71]:


results_seaonal


# In[72]:


labels_seasonal = ['ADF Test statistic','p-value','lags used','Number of observations']


# In[73]:


for label,value in zip(labels_seasonal,results_seaonal):
    print(label+':'+str(value))
# We can add a conditional statement to ease loop output interpretation
if results_seaonal[1] <= 0.05:
     print("Dickey fuller p-value is",results_seaonal[1], "below or equal to 0.05.there  is strong evidence against null hypotesis.Indicating the Time Series it is STATIONARY")
else:
     print("Dickey fuller p-value is",results_seaonal[1], "Greater than 0.05. Weak evidence against null hypothesis.Indicating the Time Series  is non-stationary")


# Now the data shifted 12 months is **not** seasonal: p value <0.05

# In[74]:


Sales['Sales Seasonal Difference'].plot()


# Compare this to the original TS, which was Seasonal. 

# In[75]:


Sales['Sales'].plot()


# Comparing all two data transformations we have done so far

# In[76]:


Sales.plot(label="Sales TS data first differemcing and seasonal")


# ## 8. ARIMA model 

# ### ARIMA model is made of AR and MA models

# ARIMA models are actually a combination of two, (or three if you count differencing as a model) processes that are able to generate series data. Those two models are based on an Auto Regressive (AR) process and a Moving Average process. Both AR and MA processes are stochastic processes. 
# The ARIMA model has got three parameters 
# ARIMA(p,d,q)

# **AR** model, parameter (p) = **Autocorrelation plot**
# 
# 
# 

# **I** parameter (I) = **Differencing order**
# 

# **MA** model, parameter (q) = **Partial Autocorrelation plot**

# ## AUTO REGRESSIVE MODEL (AR)

# The auto-regressive AR model part of the ARIMA model, provides information about past correlations into the time series. How previous lags are correlated with actual and most recent lags. The auto-regressive model takes into effect the lags t-1, t-2 in the time series on the current time series value

# We use this model to look into the auto-correlation, how many past lags are correlated with today's t0 values in the time series

# $y_i = c + \sum_{i=1}^{p}\varphi_i y_{t-1} + \varepsilon_t = \dots$ = $y_i = c + \varphi_1 y_{t-1} + \varphi_2 y_{t-2} +...+ \varphi_p y_{t-p} + \varepsilon_t$

# ## MOVING AVERAGE (MA)

# The moving average (MA) part of the ARIMA model, looks into the moving average of past n periods to determine 

# ### Identification of AR and MA parameters

# **ACF (Autocorrelation Factor)**
# It is the correlation between the observations at the current time spot and observations at the previous time spots.

# 
# **PACF (Partial Auto-correlation Factor)**
# The correlation between the observations at two time spots given that we consider both observations are correlated to the observations at the other time spots. For example, today’s stock price can be correlated to the day before yesterday, and yesterday can also be correlated to the day before yesterday. Then, PACF of the yesterday is the real correlation between today and yesterday after taking out the influence of the day before yesterday.

# - Use **PACF** plot to determine the significant term used in the *AR* model: ARIMA (**AR (Auto-regressive)**: **P parameter**; I integraged: D parameter; MA (Moving Average):Q parameter)

# - Use **ACF** plot to determine the significant term used in the *MA* model: ARIMA (AR (Auto-regressive): P parameter; I integraged: D parameter; **MA (Moving Average)**:**Q parameter**)

# In[115]:


from pandas.plotting import autocorrelation_plot
autocorrelation_plot(Sales['Sales'])


# - Use **PACF** plot to determine the significant term used in the *AR* model: ARIMA (**AR (Auto-regressive)**: **P parameter**; I integraged: D parameter; MA (Moving Average):Q parameter)

# A partial autocorrelation is a summary of the relationship between an observation in a time series with observations at prior time steps with the relationships of intervening observations removed.The autocorrelation for an observation and an observation at a prior time step is comprised of both the direct correlation and indirect correlations. These indirect correlations are a linear function of the correlation of the observation, with observations at intervening time steps.
# 
# It is these indirect correlations that the partial autocorrelation function seeks to remove.

# * We plot the first difference from the sales dataset to obtain the Sales['Sales First Difference'].plot()

# In[126]:


from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(Sales['Sales First Difference'].iloc[13:],lags=15)


# Conclusion: *P* parameter can be set up to *2* as the second lag stands out the CI area 

# - Use **ACF** plot to determine the significant term used in the *MA* model: ARIMA (AR (Auto-regressive): P parameter; I integraged: D parameter; **MA (Moving Average)**:**Q parameter**)

# In[127]:


from statsmodels.graphics.tsaplots import plot_acf
plot_acf(Sales['Sales First Difference'].iloc[13:],lags=15)


# Conclusion: *Q* parameter can be set up to *2* as the second lag stands out the CI area 

# In[ ]:


# For a non-seasonal model
# p =2 # d=1 #q=2


# ## Create an ARIMA MODEL.  ARIMA(2,1,2)

# In[128]:


###  Fit the model 


# In[129]:


from statsmodels.tsa.arima_model import ARIMA


# In[130]:


### Create an ARIMA model 


# In[131]:


model=ARIMA(Sales['Sales'],order=(2,1,2))


# Once we have created the model, we use the model.fit() function to fit the model to the data. The model_fit object stores all model parameters

# In[132]:


# Fit model to the data
model_fit = model.fit()


# In[133]:


model_fit


# The model_fit object can be chained with other functions such as summary() function to display model summary

# In[134]:


# Get model summary
model_fit.summary()


# Then we can use this ARIMA model to forecast 13 days of sales, for example: 

# In[135]:


We create a new variable in our Sales dataset called forecast to include our forecasted values 


# We use again the model_fit object we created earlier. As in other Python analysis steps, we can chain those those functions, by using model_fit.predict() so we use the predict() function after the model_fit command has been executed

# In[136]:


Sales['forecast']=model_fit.predict(start=90, end=103,dynamic=True)


# In[138]:


Sales.tail()


# From the above dataset, we can create a new one to subset just Sales and forecast values

# Again we have chained in Python the subsetting of the main dataset and the creation of a new plot

# In[139]:


Sales[['Sales','forecast']].plot(figsize=(12,8))


# *conclusion*: We can see from the plot that the ARIMA model didn not pick up the upward and downward trends of the main data. This is why we aer going to try a model with a seasonal component in it. 

# ## 9. Seasonal Arima model (SARIMA).  Includind seasonal order (1,1,1,12)

# Seasonal ARIMA models are usually denoted ARIMA(p,d,q)(P,D,Q)m, where m refers to the number of periods in each season, and the uppercase P,D,Q refer to the autoregressive, differencing, and moving average terms for the seasonal part of the ARIMA model.[3]

# We build this SARIMA model based on the ARIMA model we created earlier. Remember we found the best ARMIMA  parameters p,d,q for this data were, (2,1,2). So we extend this model to make our SARIMA model

# ### 9.1 Create a SARIMA model

# We need to import a new library in Python to run this model

# In[141]:


import statsmodels.api as sm


# In[ ]:


Now we can create our SARIMA model


# In[143]:


SARIMA_model = sm.tsa.statespace.SARIMAX(Sales['Sales'],order=(2,1,2),seasonal_order=(1,1,1,12))


# Fit model

# In[144]:


SARIMA_results = SARIMA_model.fit()


# Now that we have created the SARIMA model, then we can forecast our results

# We will create a new variable called 'forecastSARIMA' to save the forecasted values in our original Sales dataset

# In[145]:


Sales['forecastSARIMA']= SARIMA_results.predict(start=90,end=103,dynamic=True)


# Finally we plot the results subseting required variables (Sales,forecastSARIMA) from the SARIMA model

# In[146]:


Sales[['Sales','forecastSARIMA']].plot(figsize=(12,8))


# And in the plot above, we can see how the SARIMA model improved the forecast accuracy we observed earlier in the ARIMA model. 

# **Note:** In further sessions we will build our own functions to compute the forecast accuracy measure called MAPE to compare validation and forecasted dataset values

# ## 10. Forecast accuracy measure. Mean Absolute Percentage Error (MAPE).Future sessions

# Just as a small example on how you would build your own MAPE function 

# The mean absolute percentage error (MAPE) is a statistical measure of how accurate a forecast system is. It measures this accuracy as a percentage, and can be calculated as the average absolute percent error for each time period minus actual values divided by actual values.

# In[148]:


def accuracy_MAPE(Actual,Forecast):
    MAPE_calc = (abs((Actual-Forecast)/Actual).sum()/len(Actual))*100
    MAPE_value = print(f"SARIMA model MAPE value in percent{MAPE_calc}")
    return MAPE_value


# We can then use this function with both Validation and Forecast datasets in the future

# In[ ]:


accuracy_MAPE(Validation,Forecast)

