
import gym
import numpy as np
from gym import spaces

class ThreatModelingEnv(gym.Env):
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

    def reset(self):
        self.index = 0
        return self.embeddings[self.index]

    def step(self, action):
        true_label = self.labels[self.index]

        # Reward logic from Part 1
        if action == true_label:
            reward = 1.0
        elif action == 2 and true_label == 2:
            reward = 0.5
        elif action == 3:
            reward = 0.25
        else:
            reward = -1.0

        self.index += 1
        done = self.index >= len(self.notes)

        next_state = (
            self.embeddings[self.index] if not done else np.zeros(768)
        )

        return next_state, reward, done, {}
