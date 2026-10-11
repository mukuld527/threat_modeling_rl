import gym
import numpy as np
from gym import spaces

# Threat Modeling Environment for Reinforcement Learning using OpenAI Gym
class ThreatModelingEnv(gym.Env):
    # Threat Modeling Environment for Reinforcement Learning
    def __init__(self, notes, labels, embeddings):
        super(ThreatModelingEnv, self).__init__()

        self.notes = notes
        self.labels = labels
        self.embeddings = embeddings
        self.index = 0

        # State = embedding vector (768 dims from BERT)
        self.observation_space = spaces.Box(
            low=-np.inf, high=np.inf, shape=(768,), dtype=np.float32
        )

        # Actions: 0=valid, 1=invalid, 2=clarification, 3=feedback        
        self.action_space = spaces.Discrete(4)

    #The environment follows the OpenAI Gym interface with reset and step functions.
    def reset(self):
        self.index = 0
        return self.embeddings[self.index]

    #Step function for the environment
    def step(self, action):
        true_label = self.labels[self.index]

        # Reward logic — Determine the reward based on the action and true label
        # 0 — valid, 1 — invalid, 2 — clarification, 3 — feedback
        if action == true_label:
            reward = 1.0
        elif action == 2 and true_label == 2:
            reward = 0.3
        elif action == 3 and true_label == 3:
            reward = 0.2
        else:
            reward = -0.5

        self.index += 1
        terminated = self.index >= len(self.notes)
        truncated = False  # no time limit, so always False

        # Prepare the next state based on whether the episode has terminated
        next_state = (
            self.embeddings[self.index] if not terminated else np.zeros(768)
        )

        # Return the next state, reward, termination status, truncation status, and additional info
        return next_state, reward, terminated, truncated, {"true_label": true_label}













