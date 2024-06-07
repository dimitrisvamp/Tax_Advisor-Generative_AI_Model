from flask import Flask, render_template, request
import os
from model import getAdvice
from dbCreator import dbConnector

# Path for html and css
view_path = os.path.join('..', 'view')
app = Flask(__name__, template_folder=view_path, static_folder=view_path)

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def inserDataToDB():

    # Get income and expenses from submit form
    income = request.form['income']
    expenses = request.form['expenses']

    # Get advice from AI 
    advice = getAdvice(income, expenses)

    # Insert data into SQLite database
    cursor, conn = dbConnector()
    data_to_db_query = "INSERT INTO tax_data(income, expenses, advice) VALUES(?, ?, ?)" 
    cursor.execute(data_to_db_query, (income, expenses, advice))
    conn.commit()
    conn.close()

    return render_template('home.html')

@app.route('/advice', methods=['GET'])
def exportAdviceToUser():

    # Select the advice of the last user's submission
    cursor, conn = dbConnector()
    select_user_advice_fromDB = "SELECT advice FROM tax_data ORDER BY id DESC LIMIT 1"
    cursor.execute(select_user_advice_fromDB)
    user_advice = cursor.fetchone()[0]
    user_advice = user_advice.replace("\n", "<br>")
  
    conn.commit()
    conn.close()

    return render_template('home.html', advice=user_advice)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
    