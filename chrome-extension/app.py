from flask import Flask, request
import torch
from transformers import BertTokenizer
from transformers import BertForSequenceClassification, AutoModelForSequenceClassification
from flask_cors import CORS
import os
import sys

# Get the current working directory
cwd = os.getcwd()
cwd = '/'.join(cwd.split('/')[:-1])
# Construct the path to the checkpoint file using os.path.join
model_path = os.path.join(cwd, 'bert', 'checkpoints', 'bert-base-uncased_4000_0.pt')

app = Flask(__name__)
CORS(app)

# Load the BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)
state_dict = torch.load(model_path, map_location=torch.device('cpu'))
model.load_state_dict(state_dict['model_state_dict'])
# model = BertForSequenceClassification.from_pretrained('bert-base-uncased_4000_6.pt')

# Define a function to classify a list of sentences
def classify_sentences(sentences):
    # Tokenize the sentences and convert them to tensors
    inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
    # Pass the inputs through the model and get the predicted labels
    outputs = model(**inputs)
    _, predicted = torch.max(outputs.logits, dim=1)
    labels = ["negative", 'positive']

    response = []
    for i in range(len(sentences)):
        response.append({"input": sentences[i], "output": labels[predicted[i]]})

    # Return the response as a JSON response
    return response

# Define an endpoint for the API
@app.route('/classify', methods=['POST'])
def classify():
    # Get the list of sentences from the request
    sentences = request.json['sentences']

    if len(sentences) == 0:
        return {'labels': []}

    # Classify the sentences
    labels = classify_sentences(sentences)
    # Return the predicted labels as a JSON response
    return {'labels': labels}

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
