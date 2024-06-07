# Tax-Advisor

## Project Assignment
A project assignment for entry level position.

## Description
A web application that utilizes a generative AI model from openai( https://openai.com/ ) 
to provide tax advice to users. <br>

More specifically, when the application pops out to your browser, the application provides to you
some instructions on how to use the application. <br>

There are two placeholders, "Income" placeholder and "Expenses" placeholder, and two buttons, 
"SUBMIT" button and "ADVICE NOW" button. With theese placeholders and buttons the user interacts 
with the application. First the user should type the amount of his income (integer value e.g 85000) 
and the amount of his epxenses (integer value e.g 16000). If the user dont type a value to the placeholder 
the application and the presses the "SUBMIT" button the application will point out that you should fill
the empty placeholder. <br>

By filling both placeholders, the user should press the "SUBMIT" button to submit his inputs to sqlite3 database.
Once you press the "SUBMIT" button the user will notice that the web page is starting refreshing for a few seconds 
(about 20-25 seconds). Thi is happening because of the AI's responding time. In the database when u press "SUBMIT"
button, are going to be inserted three values (income value, expenses value, advice). The application uses REST API, implemented with 
flask ( https://flask.palletsprojects.com/en/3.0.x/ ) and specifically "POST" endpoint, to get the income and expenses values 
from html file.  Then the application utilizes the generative AI model to generate an advice based on theese values.
TThen theese vaules (income, expenses, advice) are inserted into database  <br>

After the page refreshes, the user should press the "ADVICE NOW" button. Because the advice is already generated,
the only thing that application should do is to select the advice from the database, which advice is related 
with the last id. Then the application uses the REST API "GET" endpoint to pass the advice to html file and represent it
to user below the "SUBMIT" and "ADVICE NOW" buttons.





