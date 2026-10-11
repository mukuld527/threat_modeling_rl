from utils.preprocess import embed_notes
import pandas as pd
from models.ppo_agent import PPOAgent
import numpy as np
import os

# ------------------------------------------------------------------------------------
# Architect Notes Based on Labels (0=valid, 1=invalid, 2=clarification, 3=feedback)
# ------------------------------------------------------------------------------------
architect_notes = {
    0: "Security architect agrees with the application team's justification.",
    1: "Security architect disagrees and requests additional evidence.",
    2: "Security architect needs clarification on the justification provided.",
    3: "Security architect recommends revising the justification to meet standards."
}


# Load unlabeled test data
df = pd.read_csv("data/unlabeled_notes.csv")

# Use the correct column name
notes = df["application_team_note"].tolist()

# Embed notes 
embeddings = embed_notes(notes)

# Load trained agent
agent = PPOAgent(state_dim=768, action_dim=4)
agent.load("models/ppo_trained_agent.pth")   # <-- adjust path if needed

print("=== DEMO ON UNLABELED NOTES ===")

predicted_architect_notes = []
predicted_labels = []

# Iterate over each note and its corresponding embedding to get agent predictions and architect notes
for i, (note, emb) in enumerate(zip(notes, embeddings)):
    action = agent.act(emb)
    predicted_labels.append(action)

    architect_note = architect_notes[action]
    predicted_architect_notes.append(architect_note)

    print(f"\nNote {i+1}: {note}")
    print(f"Agent Prediction (0=valid,1=invalid,2=clarification,3=feedback): {action}")
    print(f"Architect Note: {architect_note}")

print("\n=== END OF DEMO ===")

# ------------------------------------------------------------------------------------
# Save results to new file
# ------------------------------------------------------------------------------------
df["security_architect_note"] = predicted_architect_notes
df["predicted_label"] = predicted_labels

os.makedirs("results", exist_ok=True)
output_path = "results/architect_predictions.csv"
df.to_csv(output_path, index=False)

print(f"\nSaved architect predictions to: {output_path}")













