# Jedha Final Project

This is the final project for Jedha Lyon [Fullstack Data Science bootcamp](https://www.jedha.co/campus/lyon/): Instacart data analysis and creation of a recommendation system.

## Data Used

This [dataset](https://www.kaggle.com/c/instacart-market-basket-analysis/) from Kaggle.

## Frameworks/Languages

Python, Flask, ...

## Regarding the INSTACART-DASH-APP

To show our results about our recommendation system, we decided to create a web app on Heroku. \
The folder above, contains all the files we needed to create that application. 

First of all, we have the "apps" folder : there are three .py files which represent the different pages on the application.
- the Home page : introducing our project on Instacart
- the EDA Graphs page :  please find some Exploratory Data Analysys about the Kaggle Instacart Dataset
- the Algo page : here you will find two tabs regarding our recommendation system results. The first tab compares the two algorithms we trained (Alternating Least Squares and Restricted Boltzman Machine) with historical purchases of the users trained. The second tab compares only the ALS results with new purchases a user did (those purchases have not be trained in the ALS model)
The "csv needed" folder is all the CSVs we created to get the graphs on the app. 

Secondly, the "assets" folder contains the images we present on the application. 

The "index.py" file is the one to run locally to get the application open. The other files are necassary to define the Dash stylesheet, and to build the application on Heroku.  