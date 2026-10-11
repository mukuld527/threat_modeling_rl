import pandas as pd
import torch
from transformers import BertTokenizer, BertModel

# Utility functions for loading data and generating BERT embeddings for application team notes
def load_data(path):
    df = pd.read_csv(path)
    return df["application_team_note"].tolist(), df["label"].tolist()

# Function to load application team notes and their corresponding labels from a CSV file
def embed_notes(notes):
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertModel.from_pretrained("bert-base-uncased")

    embeddings = []
    for text in notes:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        outputs = model(**inputs)
        cls_embedding = outputs.last_hidden_state[:, 0, :].detach().numpy().flatten()
        embeddings.append(cls_embedding)

    return embeddings
# Function to generate BERT embeddings for a list of application team notes
