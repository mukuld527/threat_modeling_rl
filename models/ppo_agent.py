import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class PolicyNetwork(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim, 256),
            nn.ReLU(),
            nn.Linear(256, action_dim)
        )

    def forward(self, x):
        return self.fc(x)

class PPOAgent:
    def __init__(self, state_dim, action_dim, lr=3e-4):
        self.policy = PolicyNetwork(state_dim, action_dim)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=lr)

    def act(self, state):
        state = torch.tensor(state, dtype=torch.float32)
        logits = self.policy(state)
        probs = torch.softmax(logits, dim=-1)
        action = torch.multinomial(probs, 1).item()
        return action

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

