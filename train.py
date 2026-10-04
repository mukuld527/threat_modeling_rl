import numpy as np
from env.threat_env import ThreatModelingEnv
from models.ppo_agent import PPOAgent
from utils.preprocess import load_data, embed_notes
from utils.plot import plot_rewards

notes, labels = load_data("data/notes.csv")
embeddings = embed_notes(notes)

env = ThreatModelingEnv(notes, labels, embeddings)
agent = PPOAgent(state_dim=768, action_dim=4)

all_rewards = []

for episode in range(50):
    state = env.reset()
    done = False
    episode_rewards = []
    states, actions, rewards = [], [], []

    while not done:
        action = agent.act(state)
        next_state, reward, done, _ = env.step(action)

        states.append(state)
        actions.append(action)
        rewards.append(reward)
        episode_rewards.append(reward)

        state = next_state

    loss = agent.update(states, actions, rewards)
    all_rewards.append(sum(episode_rewards))
    print(f"Episode {episode+1} Reward: {sum(episode_rewards)} Loss: {loss}")

plot_rewards(all_rewards)

