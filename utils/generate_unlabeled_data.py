import pandas as pd
import random

# Countermeasure names for security controls
countermeasure_names = [
    "Configure HTTPS securely",
    "Implement secure session management",
    "Encrypt sensitive data using latest encryption mechanisms",
    "Enable audit logging for critical events",
    "Validate all user inputs",
    "Ensure secure deletion of sensitive data",
]

# Status options for countermeasure implementation by the application team
statuses = ["Fixed", "In Progress", "Not Applicable"]

# Application Team Notes (status-based for the application team's implementation of countermeasures)
app_fixed_notes = [
    "The control is fully implemented following enterprise guidelines.",
    "Required configurations were applied and validated in QA.",
    "Implementation aligns with architecture design and passed security checks.",
    "Feature updated to meet compliance requirements and verified by testing.",
    "Control implemented using recommended libraries and validated end-to-end."
]

# Notes for the "Not Applicable" status by the application team
app_not_applicable_notes = [
    "This control is not applicable because the application does not store sensitive data.",
    "The feature is internal-only and does not expose external endpoints.",
    "The application does not handle user authentication, making this control irrelevant.",
    "The system architecture does not include components requiring this control.",
    "The control is not applicable due to the application's read-only data flow."
]

# Notes for the "In Progress" status by the application team
app_in_progress_notes = [
    "The team is implementing this control and expects completion next sprint.",
    "Development is underway, and partial functionality is already in place.",
    "Control is being integrated into the service layer and requires additional testing.",
    "Implementation has started but dependencies are still pending.",
    "Work is in progress and updates will be provided after integration testing."
]

# Function to generate a single row of unlabeled data for RL inference
def generate_row(i):
    title = f"U{i+1}"
    name = random.choice(countermeasure_names)
    status = random.choice(statuses)

    # Application team note based on status
    if status == "Fixed":
        app_note = random.choice(app_fixed_notes)
    elif status == "Not Applicable":
        app_note = random.choice(app_not_applicable_notes)
    else:
        app_note = random.choice(app_in_progress_notes)

    # Architect note is intentionally empty for RL inference
    architect_note = ""

    return {
        "countermeasure_title": title,
        "countermeasure_name": name,
        "status": status,
        "application_team_note": app_note,
        "security_architect_note": architect_note
    }

# Generate 50 rows
rows = [generate_row(i) for i in range(50)]

df = pd.DataFrame(rows)
df.to_csv("data/unlabeled_notes.csv", index=False)

print("Generated data/unlabeled_notes.csv with 50 rows.")
