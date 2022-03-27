# Mello-Student-Guide
Mello is a student guidance tool that consists of two important parts -- a stock predictor and a career/education guide. The stock predictor predicts the price of a stock in the next 30 days by fetching the price of the stock from the past 12 years from Yahoo Finance. This way students can learn how to manage their money and gain financial independence with the use of a simple machine learning algorithm. The second part of Mello, the career and education guide, allows students to plug in the country where they might work, their college degree, and the years of experience, to estimate the salary. This tool allows students to choose what degree they want in their college life: a master's or bachelors.

Files:

tensorflow.yml = conda environment setup file

Untitled.ipynb = Jupyter Notebook for Stock Prediciton ML

app.py = webapp for Stock Prediction

keras_model.h5 = Sequential ML model with 50 epoch calculations for stock prediction

Salary&Job Prediction.ipynb = Jupyter Notebook for Salary Prediction

explore_page.py = webapp page to explore Salary data

predict_page.py = webapp page to be able to predict salary

survey_results_public.csv = dataset used for Salary prediction ML

salary.py = webapp page to navigate between all sub webapp pages (explore, stock prediction, salary prediction)

Instructions:

1) create a conda environment and run the tensorflow.yml file to get required packages for Mello
2) open a new terminal in folder and type :- "pip install --upgrade tensorflow" - upgrades Tensorflow to work with other packages like numpy, keras etc.
3) open a new terminal in folder and type :- "streamlit run app.py" - This is for the Stock Predicition WebApp
4) open a new terminal in folder and type :- "streamlit run salary.py" - This is for the Salary&Job Prediction WebApp


Note: 67000/69000 lines of code is just data from survey_results_public.csv
