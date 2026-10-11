import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Proximal Policy Optimization (PPO) Agent for Reinforcement Learning
class PolicyNetwork(nn.Module):
    # Initialize the policy network with the given state and action dimensions
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim, 256),
            nn.ReLU(),
            nn.Linear(256, action_dim)
        )

    # Forward pass through the policy network to obtain action logits
    def forward(self, x):
        return self.fc(x)

# Proximal Policy Optimization (PPO) Agent class that uses the PolicyNetwork for action selection and updates its policy based on collected experiences.
class PPOAgent:
    # Initialize the PPO agent with the policy network and optimizer
    def __init__(self, state_dim, action_dim, lr=3e-4):
        self.policy = PolicyNetwork(state_dim, action_dim)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=lr)

    # Save the current policy and optimizer state to a file
    def save(self, path):
        torch.save({
            "policy_state_dict": self.policy.state_dict(),
            "optimizer_state_dict": self.optimizer.state_dict()
        }, path)
        print(f"Model saved to {path}")

    # Load the policy and optimizer state from a file    
    def load(self, path):
        checkpoint = torch.load(path, map_location=torch.device("cpu"))
        self.policy.load_state_dict(checkpoint["policy_state_dict"])
        self.optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
        self.policy.eval()  # Set the policy network to evaluation mode after loading
        print(f"Model loaded from {path}")

    # Select an action based on the current policy and state
    # Act function that takes the current state and returns an action based on the policy network's output
    def act(self, state):
        state = torch.tensor(state, dtype=torch.float32)
        logits = self.policy(state)
        probs = torch.softmax(logits, dim=-1)
        action = torch.multinomial(probs, 1).item()
        return action

    # Update the policy network based on collected experiences (states, actions, rewards)
    # This function computes the loss using the selected actions and rewards, performs backpropagation, and updates the policy network's parameters.
    def update(self, states, actions, rewards):
        states = torch.tensor(states, dtype=torch.float32)
        actions = torch.tensor(actions)
        rewards = torch.tensor(rewards, dtype=torch.float32)

        logits = self.policy(states)
        log_probs = torch.log_softmax(logits, dim=-1)
        selected_log_probs = log_probs[range(len(actions)), actions]

        loss = -(selected_log_probs * rewards).mean()

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return loss.item()

