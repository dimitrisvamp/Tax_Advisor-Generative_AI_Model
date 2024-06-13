import openai
import os 

openai.api_key = 'YOUR_OPENAI_API_KEY'

def getAdvice(income, expenses):

    # The default question to gpt engine from developer
    prompt = f'''
    You are a tax advisor and you will get as input {income} for the income of customer
    and {expenses} as his expenses. 

    First of all i want you to mention the tax scale 
    that customer's income belongs to according to Greek tax scale and how much money the customer 
    is going to pay to taxes. After that advise the user much money per year according to his income
    he should save for his retirement and how much for personal entertainment.
    Then advise the user how he can invest a piece of his income to increase it and provide him 
    relevant strategies to spend less money to taxes according to his income. Also you have to 
    advise the user relevant and different strategies so he can reduce his expenses. 

    Provide your advices and your tips as a clean and cosine manner in a sequence text without any labels.
    '''
    print('\nProccessing your advice...\n')
    print('\nThis may take a few seconds, please wait!\n')
    response = openai.chat.completions.create(
        model='gpt-4-turbo-2024-04-09',  # Specify the engine
        messages=[{"role": "system", "content": "You are a tax advisor."},
                  {"role": "user", "content": prompt}],   # User's input
        max_tokens=500,  # Adjust the token count as needed
        n=1,             # Number of output responses
        temperature=0.7, 
    )

    advice = response.choices[0].message.content

    return advice




    
