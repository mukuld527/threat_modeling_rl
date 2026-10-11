import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from env.threat_env import ThreatModelingEnv
from models.ppo_agent import PPOAgent
from utils.preprocess import load_data, embed_notes
from utils.plot import (
    plot_rewards,
    plot_loss,
    plot_accuracy,
    plot_confusion_matrix,
    save_metrics_table
)

notes, labels = load_data("data/notes.csv")
embeddings = embed_notes(notes)

# Initialize the threat modeling environment with the loaded notes, labels, and embeddings
env = ThreatModelingEnv(notes, labels, embeddings)
# Load trained agent
agent = PPOAgent(state_dim=768, action_dim=4)

all_rewards = []
all_preds = []
all_true = []
losses = []
acc_values = []

# Training loop for the PPO agent over multiple episodes
for episode in range(50):
    state = env.reset()
    done = False
    episode_rewards = []
    states, actions, rewards = [], [], []

    while not done:
        action = agent.act(state)

        # Take a step in the environment with the chosen action
        next_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated

        all_preds.append(action)
        all_true.append(info["true_label"])

        states.append(state)
        actions.append(action)
        rewards.append(reward)
        episode_rewards.append(reward)

        state = next_state

    loss = agent.update(states, actions, rewards)
    losses.append(loss)

    # Episode accuracy
    ep_acc = accuracy_score(all_true, all_preds)
    acc_values.append(ep_acc)

    all_rewards.append(sum(episode_rewards))
    print(f"Episode {episode+1} Reward: {sum(episode_rewards)} Loss: {loss}")

# -----------------------------
# PERFORMANCE METRICS
# -----------------------------
accuracy = accuracy_score(all_true, all_preds)
precision = precision_score(all_true, all_preds, average="macro")
recall = recall_score(all_true, all_preds, average="macro")
f1 = f1_score(all_true, all_preds, average="macro")
cm = confusion_matrix(all_true, all_preds)

print("\n=== PERFORMANCE METRICS ===")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")
print("\nConfusion Matrix:")
print(cm)

# Save metrics table
save_metrics_table({
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1_score": f1
})

# -----------------------------
# GENERATE ALL REQUIRED PLOTS
# -----------------------------
plot_rewards(all_rewards)
plot_loss(losses)
plot_accuracy(acc_values)
plot_confusion_matrix(cm)

# -----------------------------
# SAVE TRAINED PPO AGENT
# -----------------------------
agent.save("models/ppo_trained_agent.pth")

print("\nSaved all plots and metrics in results/ folder.")




