# Tax-Advisor

## Project Assignment
A project assignment for entry level position.

## Description
A web application that utilizes a generative AI model from openai( https://openai.com/ ) 
to provide tax advice to users. <br>

## Requirements
- If you run with Docker you don't need to install any requirements. Docker will make it automatically for you.
- If you run from terminal you need to install:
  - Flask
  - openai

## Usage
More specifically, when the application pops out to your browser, the application provides to you
some instructions on how to use the application. <br>

There are two placeholders, "Income" placeholder and "Expenses" placeholder, and two buttons, 
"SUBMIT" button and "ADVICE NOW" button. With theese placeholders and buttons the user interacts 
with the application. First the user should type the amount of his income (integer value e.g 85000) 
and the amount of his epxenses (integer value e.g 16000). If the user dont type a value to the placeholder 
and then presses the "SUBMIT" button the application will point out that you should fill
the empty placeholder. <br>

By filling both placeholders, the user should press the "SUBMIT" button to submit his inputs to sqlite3 database.
Once you press the "SUBMIT" button the user will notice that the web page is starting refreshing for a few seconds 
(about 20-25 seconds). Thi is happening because of the AI's responding time. In the database when u press "SUBMIT"
button, are going to be inserted three values (income value, expenses value, advice). The application uses REST API, implemented with 
flask ( https://flask.palletsprojects.com/en/3.0.x/ ) and specifically "POST" endpoint, to get the income and expenses values 
from html file.  Then the application utilizes the generative AI model to generate an advice based on theese values according to the project's needs
( e.g propert questions that a user could make to get back advice for his taxes payments, how much money he could save for his retirement and personal
entertainment, what he can do to reduce his taxes or how he can invest money ).
Subsequently theese vaules (income, expenses, advice) are inserted into database.  <br>

After the page refreshes, the user should press the "ADVICE NOW" button. Because the advice is already generated,
the only thing that application should do is to select the advice from the database, which advice is related 
with the last id. Then the application uses the REST API "GET" endpoint to pass the advice to html file and represent it
to user below the "SUBMIT" and "ADVICE NOW" buttons.

## Uploaded Files
- model folder:
  - dbCreator.py ( This python file creates the database and the table for taxes if they don't exist or makes they connection to the database and taxes table if they exist )
  - model.py ( This python file integrates the generative AI model that openai provides according to our dependences )
  - RestAPI.py ( This python file is the REST API that communicates with the html home page and the sqlite3-server )
  - __init__.py ( An typical empty __init__.py file )
 - view folder:
   - home.html ( This html file creates the home page of the application )
   - buttons.css ( This css file creates the style of the home page )

## How To Run
- If you run the application from visual studio:
  - Open the RestAPI.py file to vs code 
  - Press the run button
  - Open your localhost at the 5000 port and the home page will show up or copy the link of your localhost from your terminal and paste it to your browser.
- If you run the applicantion from terminal:
  - Open terminal
  - Run to your terminal:
    - cd yourPathDirectory/model
    - python RestAPI.py
  - Open your localhost at the 5000 port and the home page will show up or copy the link of your localhost from your terminal and paste it to your browser.
- If you run the applicantion from Docker:
  - Open terminal
  - Run to your terminal:
    - cd yourPathDirectory (where the Dockerfile exists)
    - docker build -t tax_advisor .
    - docker run -p 5000:5000 tax_advisor
  - Open your localhost at the 5000 port and the home page will show up or copy the link of your localhost from your terminal and paste it to your browser.








