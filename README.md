# Spam mail detection

This project is a part of the Machine learning see live project by clicking this link https://spamemail.herokuapp.com/

<img src="Spam mail.gif" width="80%" height="80%">

#### -- Project Status: [Completed]

## Project Intro/Objective
The purpose of this project is to detect whether mail sent by person is spam or not.

### Methods Used
* Data gathering
* Data preprocessing
* Machine Learning
* Model evaluation
* Predictive Modeling
* Model deploying

### Technologies
* Python
* Numpy 
* Pandas
* jupyter
* joblib
* HTML
* CSS
* JavaScript
* Flask
* Heroku

## Project Description
This is project based on classification ml algorithm. 

Dataset used by this project is 'spam.csv' downloaded from kaggle. After downloading and importing dataset(in jupyter Notebook) i did data mapping like ham=0 and spam=1 and created one column 'sapm'.

After that i just divided my dataset into dependent and independent features. (Independent features=Message | Dependent feature=Spam) and split into training and testing data.

After that i did text preprocessing for that i used 'CountVectorizer'.

After that i created 'Multinomial naive bayes' model and used pipline.

I got 97% testing accuracy.

After that i saved model using 'joblib' library. After that I creted UI in flask and deployed on 'Heroku'.

## Needs of this project

- frontend developers
- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- writeup/reporting

## Contact
* Feel free to contact me any questions or if you are interested in contributing!


<h1 align=center>Thank You</h1>

