from utils.preprocess import embed_notes
import pandas as pd
from models.ppo_agent import PPOAgent
import numpy as np

# Load unlabeled test data
df = pd.read_csv("data/unlabeled_notes.csv")
notes = df["note"].tolist()

# Embed notes
embeddings = embed_notes(notes)

# Load trained agent
agent = PPOAgent(state_dim=768, action_dim=4)

print("=== DEMO ON UNLABELED NOTES ===")

for i, (note, emb) in enumerate(zip(notes, embeddings)):
    action = agent.act(emb)
    print(f"\nNote {i+1}: {note}")
    print(f"Agent Prediction (0=valid,1=invalid,2=clarification,3=feedback): {action}")

print("\n=== END OF DEMO ===")
