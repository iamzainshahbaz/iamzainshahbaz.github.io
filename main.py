from flask import Flask, render_template, request
import pickle
from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs
app = Flask(__name__)


context = "My Name is Dum-e. I am an AI. I do what I am told to. My User right now is also my programmer. I am getting better everyday. I like to mean something."


model = pickle.load(open('model_qna.pkl', 'rb'))

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def chatbot_response():
    msg = request.form["msg"]
    
    msg = [
    {
        "context": context,
        "qas": [
            {
                "question": msg,
                "id": "0",
                }
            ],
        }
    ]
    
    
    response, prob = model.predict(msg)
    response = response[0]['answer'][0]
    return str(response)

if __name__ == "__main__":
    app.run()