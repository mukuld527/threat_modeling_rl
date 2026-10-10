# Threat Modeling Reinforcement Learning Project

This project implements a PPO-based reinforcement learning agent that evaluates threat-modeling justification notes and classifies them as valid, invalid, or requiring clarification.

## Agent Training

The file data/notes.csv contains labeled data column label denotes these value
0: For valid notes

1: Invalid notes

2: Clarification notes

3: Feedback notes


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


#### Resolving environment issues

Multiple times I faced environment related issue while running this project. I followed below steps to resolved —

1. conda create -n rl python=3.10 -y

2. conda activate rl

3. pip install numpy pandas torch transformers matplotlib gymnasium

4. python data/generate_test_data.py

5. python train.py


## Project Structure

```text

threat_modeling_rl/
│
├── data/
│   ├── notes.csv                       # Historical notes and labels
│   ├── unlabeled_notes.csv             # Test data unlabeled
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


