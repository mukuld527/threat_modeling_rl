# Threat Modeling Reinforcement Learning Project

This project implements a PPO-based reinforcement learning agent that evaluates threat-modeling justification notes and classifies them as valid, invalid, or requiring clarification.

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Add your notes dataset:
   data/notes.csv
   Columns: note, label

3. Train the agent:
   python train.py

4. View reward curve:
   reward_curve.png

5. Run demo:
   python demo.py

Project Structure —

```text

threat_modeling_rl/
│
├── data/
│   ├── notes.csv                       # historical notes + labels
│
├── env/
│   ├── threat_env.py                   # custom RL environment
│
├── models/
│   ├── ppo_agent.py                    # PPO agent
│
├── utils/
│   ├── preprocess.py                   # text preprocessing + embeddings
│   ├── plot.py                         # reward curve plotting
│   ├── countermeasure_generation.py    # for generating the list of threat modeling countermeasures
│
├── train.py                            # main training script
├── demo.py                             # agent demonstration script
├── requirements.txt                    # dependencies
└── README.md                           # instructions for running project

```
