from flask import Flask, render_template, request, jsonify
from trello_integration import TrelloIntegration
from ai_assistant import AIAssistant
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
trello = TrelloIntegration()
ai_assistant = AIAssistant()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_task', methods=['POST'])
def create_task():
    data = request.json
    task_name = data['taskName']
    task_description = data['taskDescription']
    
    # Create a card in Trello
    todo_list_id = os.getenv('TRELLO_TODO_LIST_ID')
    card = trello.create_card(todo_list_id, task_name, task_description)
    
    return jsonify({"success": True, "card": card})

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    todo_list_id = os.getenv('TRELLO_TODO_LIST_ID')
    cards = trello.get_list_cards(todo_list_id)
    return jsonify(cards)

@app.route('/ask_assistant', methods=['POST'])
def ask_assistant():
    data = request.json
    question = data['question']
    response = ai_assistant.get_response(question)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)