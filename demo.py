from env.threat_env import ThreatModelingEnv
from models.ppo_agent import PPOAgent
from utils.preprocess import load_data, embed_notes

notes, labels = load_data("data/notes.csv")
embeddings = embed_notes(notes)

env = ThreatModelingEnv(notes, labels, embeddings)
agent = PPOAgent(state_dim=768, action_dim=4)

state = env.reset()
done = False

print("=== DEMO START ===")
while not done:
    action = agent.act(state)
    print(f"Note: {notes[env.index]}")
    print(f"Agent Action: {action}")
    state, reward, done, _ = env.step(action)
print("=== DEMO END ===")

