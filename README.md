Project Structure —
threat_modeling_rl/
│
├── data/
│   ├── notes.csv                 # historical notes + labels
│
├── env/
│   ├── threat_env.py             # custom RL environment
│
├── models/
│   ├── ppo_agent.py              # PPO agent
│
├── utils/
│   ├── preprocess.py             # text preprocessing + embeddings
│   ├── plot.py                   # reward curve plotting
│
├── train.py                      # main training script
├── demo.py                       # agent demonstration script
├── requirements.txt              # dependencies
└── README.md                     # instructions for running project
