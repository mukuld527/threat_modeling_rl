import pandas as pd
import torch
from transformers import BertTokenizer, BertModel

def load_data(path):
    df = pd.read_csv(path)
    return df["note"].tolist(), df["label"].tolist()

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

