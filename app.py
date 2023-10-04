from flask import Flask, render_template, request, jsonify
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from pandasai import SmartDataframe

'''
from pymongo import MongoClient

# Initialize the MongoDB client
client = MongoClient('mongodb+srv://gaurav:Gaurav%40123@cluster0.s31reuq.mongodb.net/?retryWrites=true&w=majority')  # Replace with your MongoDB server URI

# Select a database (create it if it doesn't exist)
db = client['Pandas_AI']  # Replace with your desired database name
'''
import pandasai as pai
# pai.clear_cache()s





import os
os.environ["OPENAI_API_KEY"] = "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"

#connection = duckdb.connect("cache_db.db")

# Your pandasAI setup
OPENAI_API_KEY = "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"
llm = OpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")
    # pandas_ai = PandasAI(llm,conversational=True)
    #df_data = pd.read_csv("airdata.csv")
temp = SmartDataframe("test.csv",config={"llm":llm, "enable_cache": False})
def chatting(prompt):
    # prompt = "Are there more females or males ?"
    response = temp.chat(prompt)
    #response = str(result)
    # print(response)
    return response


# response = pandas_ai.run(df_data,prompt=prompt)
app = Flask(__name__)
# Route to serve the chat interface
@app.route('/')
def chat():
    return render_template('index.html')

# Route to handle user messages and interact with LangChain
@app.route('/process_message', methods=['POST'])
def process_message():
    data = request.get_json()
    user_message = data.get('message')
    print(f"user message -> {user_message}")
    returnedAnswer = chatting(user_message)
    # Send the user message to LangChain for processing
    # bot_response = temp.chat(prompt=user_message)
    bot_response ="hello, it is a response"
    logger = app.logger
    logger.info('\nHello from the console! -> '+ bot_response)
    logger.info('\nUser message -> '+user_message)
    logger.info('\nreturned Answer  -> '+ returnedAnswer)
    logger.info('\nreturned Answer  -> '+ str(jsonify({'bot_response': str(returnedAnswer)})))
    #print(f"returned answer  -> {returnedAnswer}")
    # print(bot_response)

    # Return the bot's response as JSON
    return jsonify({'bot_response': str(returnedAnswer)})
    # return str(returnedAnswer)

if __name__ == '__main__':
    app.run(debug=True)
