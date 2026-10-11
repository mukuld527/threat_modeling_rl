import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

# Ensure results folder exists 
os.makedirs("results", exist_ok=True)

# Plotting utility functions for visualizing training results and performance metrics
def plot_rewards(rewards):
    plt.figure(figsize=(8,5))
    plt.plot(rewards)
    plt.title("Training Reward Curve")
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.savefig("results/reward_curve.png")
    plt.close()

# Plotting utility function for visualizing training loss curve
def plot_loss(losses):
    plt.figure(figsize=(8,5))
    plt.plot(losses)
    plt.title("Training Loss Curve")
    plt.xlabel("Episode")
    plt.ylabel("Loss")
    plt.savefig("results/loss_curve.png")
    plt.close()

# Plotting utility function for visualizing accuracy over episodes
def plot_accuracy(acc_values):
    plt.figure(figsize=(8,5))
    plt.plot(acc_values)
    plt.title("Accuracy Over Episodes")
    plt.xlabel("Episode")
    plt.ylabel("Accuracy")
    plt.savefig("results/accuracy_curve.png")
    plt.close()

# Plotting utility function for visualizing the confusion matrix
def plot_confusion_matrix(cm):
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.savefig("results/confusion_matrix.png")
    plt.close()

# Utility function for saving performance metrics as a CSV file
def save_metrics_table(metrics_dict):
    import pandas as pd
    df = pd.DataFrame([metrics_dict])
    df.to_csv("results/performance_metrics.csv", index=False)
